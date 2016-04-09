from html.parser import HTMLParser
from collections import namedtuple
class html_parser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
    def handle_starttag(self,tag,attrs):
        self.tags.append(html_tag(tag,attrs))
    def handle_endtag(self,tag):
        self.tags.append(html_tag(tag,None))
class html_tag():
    def __init__(self,type,attrs):
        self.type = type
        self.attrs = attrs
