import re
import sys
from functools import namedtuple

import mistune
import jinja2

import cv
from cv.templated import Templated


ESCAPE_CHARS = {
    '&':  r'\&',
    '%':  r'\%',
    '$':  r'\$',
    '#':  r'\#',
    '_':  r'\letterunderscore{}',
    '{':  r'\letteropenbrace{}',
    '}':  r'\letterclosebrace{}',
    '~':  r'\lettertilde{}',
    '^':  r'\letterhat{}',
    '\\': r'\letterbackslash{}',
}

def escape(text, quote=False, smart_amp=True):
    return "".join([ESCAPE_CHARS.get(char, char) for char in text])

class Environment(jinja2.Environment):
    def __init__(self):
        super().__init__('%{', '}', '#{', '}', '%', "\n")
        self.filters.update({
            'def': self.def_filter,
            'e': escape,
            'escape': escape
        })

    def def_filter(self, defs):
        result = ""
        for key, value in defs.items():
            value = escape(value)
            template = self.from_string(r"\def\#{key}{#{value | e}}")
            result += template.render(key=key, value=value) + "\n"
        return result


class Renderer(mistune.Renderer):
  ENV = Environment()
  _t = Templated(ENV)

  @_t
  def block_code(self, code, lang=None):
    return \
    r"""
    \begin{verbatim}
    #{code}
    \end{verbatim}
    """
  @_t
  def block_quote(self, text):
    return \
    r"""
    \begin{quote}
    #{text}
    \end{quote}
    """

  @_t
  def header(self, text, level, raw=None):
    if level > 3:
      raise NotImplemented()

    section = ('sub' * (level - 1)) + 'section'
    return \
    r"""
    \#{section}{#{text}}
    """, vars()
  @_t
  def hrule(self):
    return \
    r"""
    \hrule
    """
  @_t
  def list(self, body, ordered=True):
    env = 'enumerate' if ordered else 'itemize'
    return \
    r"""
    \begin{#{env}}
    #{body}
    \end{#{env}}
    """, vars()
  @_t
  def list_item(self, text):
    return \
    r"""
    \item #{text}
    """
  @_t
  def paragraph(self, text):
    return \
    r"""
    #{text} \par
    """
  @_t
  def double_emphasis(self, text):
    return r"\textbf{#{text}}"
  @_t
  def emphasis(self, text):
    return r"\emph{#{text}}"
  @_t
  def codespan(self, text):
    return r"\texttt{#{text}}"
  @_t
  def linebreak(self):
    return r"\\"
  @_t
  def autolink(self, link, is_email=False):
    if is_email:
      raise NotImplemented()
    web = re.compile(r'^https?://').sub('', link)
    web = escape(web)
    return r"\web{#{web}}", vars()
  @_t
  def link(self, link, title, text):
    return r"\anchor{#{link}{#{title}}"


class CVRenderer(Renderer):
  _t = Renderer._t

  Section = namedtuple('Section', ['env', 'text', 'level', 'raw'])

  def __init__(self, *args, **kwargs):
    self.sections = []
    super().__init__(*args, **kwargs)

  def end(self):
      return "\n".join(self.endenv())

  def endenv(self, level=0):
      envs = []
      while self.sections and level <= self.sections[-1].level:
        ended = self.sections.pop()
        if ended.level < 2:
            template = self.ENV.from_string(r"\end{#{env}}")
            envs.append(template.render(**ended._asdict()))
      return envs

  def beginenv(self, section):
      envs = []
      if section.level > 1:
          envs.append(super().header(section.text, section.level, section.raw))
      if section.level < 2:
          template = self.ENV.from_string(r"\begin{#{env}}")
          envs.append(template.render(**section._asdict()))
      return envs

  @_t
  def hrule(self):
    return \
    r"""
    \hrulefill
    """

  @_t
  def block_quote(self, text):
    env = 'quote'
    if self.sections:
        env = '{}_{}'.format(self.sections[-1].env, env)
    return \
    r"""
    \begin{#{env}}#{text}
    \end{#{env}}
    """, vars()
  @_t
  def header(self, text, level, raw=None):
    endenv = self.endenv(level)

    if level > 1:
        i = -len('section')
        rootenv = self.sections[0].env
        sectionenv = rootenv[:i] + ('sub' * (level - 1)) + rootenv[i:]
    else:
        sectionenv = text.lower().replace(' ', '_') + '_section'

    section = self.Section(sectionenv, text, level, raw)
    self.sections.append(section)

    beginenv = self.beginenv(section)

    return "\n".join(endenv + beginenv)


class Parser(mistune.Markdown):

    def output(self, text, rules=None):
        return super().output(text, rules) + self.renderer.end()


class Builder(cv.Builder):

  def __init__(self):
    parser = Parser(renderer=CVRenderer(), hard_wrap=True)
    super().__init__(parser = parser, env=Renderer.ENV)

  def run(self, doc):
      _escape = mistune.escape
      mistune.escape = escape
      super().run(doc)
      mistune.escape = _escape
