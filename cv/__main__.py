import argparse
import logging

from cv import Document, pdf, tex, html


builders = dict()
for module in [pdf, tex, html]:
  builder = module.Builder()
  builders[builder.name] = builder
formats = builders.keys()

ap = argparse.ArgumentParser('cv')
ap.add_argument('formats', choices=formats, nargs='+',
                metavar='format', help='{%s}' % ','.join(formats))
ap.add_argument('--verbose', '-v', action='store_true')
args = ap.parse_args()

if args.verbose:
  logging.basicConfig(level=logging.DEBUG)

doc = Document()
for format in args.formats:
  logging.info('Building "%s"...' % format)
  builders[format].run(doc)
  logging.info('Done')
