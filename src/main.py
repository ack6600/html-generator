import argparse
from html_parser import html_parser
from html_writer import html_writer

parser = argparse.ArgumentParser(description='Generates html')
parser.add_argument('style',type=str)
args = parser.parse_args()
parser = html_parser()
with open(args.style, 'r') as read:
    parser.feed(read.read())
writer = html_writer(parser.tags)
