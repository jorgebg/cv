import subprocess
import logging
from sys import stderr, stdout


import cv
from cv import tex

class Logger:
    def __init__(self, level):
        self.level = level

    def write(self, msg):
        logfinf.log(self.level, msg)
        return len(s)

    def fileno(self):
        return stderr.fileno()

class Builder(cv.Builder):

  def run(self, doc=None):
    builder = tex.Builder()
    builder.run(doc)
    subprocess.check_call(
        'xelatex cv.tex',
        stdout = Logger(logging.INFO),
        stderr = Logger(logging.ERROR),
        cwd=builder.build_dir,
        shell=True
    )
