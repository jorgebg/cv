import re
import shutil
import os

import mistune
import yaml
import jinja2


class Document:

  def __init__(self, filename='cv.md'):
    with open(filename) as file:
      self.content = file.read()

    parts = self.parse(self.content)

    self.context = {}

    self.context['page'] = yaml.load(parts['frontmatter'])
    self.body = jinja2.Template(parts['body']).render(**self.context)

  def parse(self, content):
    pattern = r'---(?P<frontmatter>.*?)---(?P<body>.*)'
    m = re.search(pattern, content, re.DOTALL)

    return m.groupdict()


class Builder:
  def __init__(self, renderer=None, parser=None, env=None, doc=None):
    self.doc = doc

    self.name = self.__module__.split('.')[-1]
    self.build_dir = os.path.join('build', self.name)
    self.templates_dir = os.path.join('templates', self.name)
    self.source_file = 'cv.' + self.name

    self.renderer = renderer or mistune.Renderer()
    self.parser = parser or mistune.Markdown(renderer=self.renderer, hard_wrap=True)

    self.env = env or jinja2.Environment()
    self.env.filters['markdownify'] = self.markdownify_filter
    self.env.loader = jinja2.FileSystemLoader(self.templates_dir)

  def markdownify_filter(self, src):
    return self.parser.render(src)

  def render(self):
    doc = self.doc
    doc.context['body'] = self.parser.render(doc.body)
    template = self.env.get_template(self.source_file)
    output = template.render(doc.context)
    return output

  def run(self, doc):
    self.doc = doc
    self.clean()
    shutil.copytree(self.templates_dir, self.build_dir)
    output = self.render()
    filename = os.path.join(self.build_dir, self.source_file)
    with open(filename, 'w') as file:
      return file.write(output)

  def clean(self):
    try:
      shutil.rmtree(self.build_dir)
    except FileNotFoundError:
      pass
