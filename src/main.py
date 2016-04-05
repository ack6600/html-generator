import argparse
from html_parser import html_parser

parser = argparse.ArgumentParser(description='Generates html')
parser.add_argument('style',type=str)
args = parser.parse_args()
parser = html_parser()
with open(args.style, 'r') as read:
  parser.feed(read.read())
