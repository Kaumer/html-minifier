import unittest
from html_minifier import Minifier

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.html = """<!DOCTYPE html>
                    <html>
                    <head>
                        <title> 1 2 3 4 5</title>
                    </head>
                    <body>
                     esto es una prueba
                    </body>
                    </html>"""

    def test_shuffle(self):
        # make sure the shuffled sequence does not lose any elements
        mini = Minifier(self.html)
        self.assertEqual(mini.minify(), 
            "<!DOCTYPE html><html><head><title>1 2 3 4 5</title></head><body>esto es una prueba</body></html>")
