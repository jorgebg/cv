import subprocess
import sys


import cv
from cv import tex


class Builder(cv.Builder):

  def run(self, doc=None):
    builder = tex.Builder()
    builder.run(doc)
    result = subprocess.run(
        'xelatex cv.tex',
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd=builder.build_dir,
        shell=True
    )
    if result.stdout.find(b'Output written on cv.pdf') == -1:
        print(result.stdout)
        sys.exit(1)
