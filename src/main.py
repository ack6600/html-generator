import argparse
from html.parser import HTMLParser as hp

parser = argparse.ArgumentParser(description='Generates html')
parser.add_argument('style',type=str)
args = parser.parse_args()
parser = hp()
print(parser)
