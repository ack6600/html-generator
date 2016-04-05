from html.parser import HTMLParser
class html_parser(HTMLParser):
  def handle_starttag(self, tag, attrs):
    print(tag, attrs)
