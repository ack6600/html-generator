from html.parser import HTMLParser
class html_parser(HTMLParser):
    def handle_starttag(self,tag,attrs):
        self.tags.append(html_tag(tag,attrs))
    def handle_endtag(self,tag):
        self.tags.append(html_tag(tag,None))
class html_tag():
    def __init__(self,type,attrs):
        self.type = type
        self.attrs = attrs

