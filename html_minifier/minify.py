#encoding:utf-8
import re

class Minifier(object):

    _re_for_Whitespace = r"\s+"
    _re_for_white_space_in_tags = r"((}|>)\s({|<))"
    _re_for_commets = r"<!--(?!\[if.*?\]).*?(?!\[endif.*?\])-->"

    def __init__(self, html=""):
        self.html = html
        self.convert_to_space = re.compile(self._re_for_Whitespace)
        self.remove_commets = re.compile(self._re_for_commets)
        self.remove_spaces_in_tags = re.compile(self._re_for_white_space_in_tags)
        self.remove_bracket_less = re.compile(r"\s<")
        self.remove_bracket_greater = re.compile(r">\s")

    def stripWhitespace(self, html):
        return html.strip()

    def collapseWhitespace(self, html):
        return self.convert_to_space.sub(" ", html)

    def removeWhiteSpacesBrackets(self, html):
        html = self.remove_bracket_greater.sub(">", html)
        return self.remove_bracket_less.sub("<", html)

    def removeWhitespaceTags(self, html):

        regex = self.remove_spaces_in_tags
        match = regex.search(html)
        while match:
            html = ''.join([
                    html[:match.start()],
                    match.group().replace(" ", ""),
                    html[match.end():]])
            match = regex.search(html)
        return html

    def removeComments(self, html):
        return self.remove_commets.sub("", html)

    def minify(self):
        html = self.html
        html = self.stripWhitespace(html)
        html = self.collapseWhitespace(html)
        html = self.removeComments(html)
        html = self.removeWhiteSpacesBrackets(html)
        html = self.removeWhitespaceTags(html)
        return html
