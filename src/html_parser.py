from html.parser import HTMLParser
from collections import namedtuple
class html_parser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        self.TagObj = namedtuple('tag','tag,attrs')
    def handle_starttag(self,tag,attrs):
        tag_obj = self.TagObj(tag,attrs)
        self.tags.append(tag_obj)
    def handle_endtag(self,tag):
        tag_obj = self.TagObj(tag,None)
        self.tags.append(tag_obj)
