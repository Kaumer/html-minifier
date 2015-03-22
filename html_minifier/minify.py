#encoding:utf-8
import re

class Minifier(object):

    def __init__(self, html):
        self.html = html

    def stripWhitespace(self, html):
        return html.strip()

    def collapseWhitespace(self, html):
        return re.sub(r"\s+", " ", html)

    def removeWhitespaceTags(self, html):
        regex = re.compile(r"(>\s|\s<|(}|>)\s({|<))")
        match = regex.search(html)
        while match:
            html = ''.join([
                    html[:match.start()],
                    match.group().replace(" ", ""),
                    html[match.end():]])
            match = regex.search(html)
        return html

    def minify(self):
        html = self.html
        html = self.stripWhitespace(html)
        html = self.collapseWhitespace(html)
        html = self.removeWhitespaceTags(html)
        return html
