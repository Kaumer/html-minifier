import unittest
from pathlib import Path

from html_minifier import Minifier
from html_minifier import DjangoMinifier


class TestMinify(unittest.TestCase):

    ext_min = "_min"
    file_name = "base"
    _file = "{0}.html"
    location = "html"

    def setUp(self):
        path = Path(__file__).parent
        file_name = ""
        names = (self.file_name, self.ext_min)
        html_vars = ["html", "html_min"]
        for i, name in enumerate(names):
            file_name = ''.join([file_name, name])
            _file = self._file.format(file_name)
            f = path.joinpath(self.location, _file).open()
            setattr(self, html_vars[i], f.read())
            f.close()

    def test_minifier(self):
        mini = Minifier(self.html)
        self.assertEqual(mini.minify(), self.html_min)


class TestMinifyDjango(TestMinify):

    file_name = "django"

    def test_minifier(self):
        mini = DjangoMinifier(self.html)
        self.assertEqual(mini.minify(), self.html_min)
