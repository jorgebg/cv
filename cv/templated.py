import inspect
import types
from textwrap import dedent

from jinja2 import Environment

class Templated:
  def __init__(self, env):
    self.env = env or Environment()

  def render(self, source, **data):
    return self.env.from_string(source).render(**data)

  def __call__(self, func):
    return self.decorator(func)

  def decorator(self, func):
    argspec = inspect.getargspec(func)

    def _render(*args, **kwargs):
      rendered = ""
      data = dict(zip(argspec.args, args), **kwargs)
      source = func(*args, **kwargs)
      if source:
          if isinstance(source, tuple):
            source, newdata = source
            data.update(newdata)
          source = dedent(source)
          template = self.env.from_string(source)
          del data[argspec.args[0]]  # self
          rendered = template.render(**data)
      return rendered

    return _render
