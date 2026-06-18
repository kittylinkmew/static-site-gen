import unittest

from gencontent import extract_title


class Test_Gencontent(unittest.TestCase):
    def test_extract_title(self):
        markdown_input = """# My Project Title\n
    This is a description paragraph.\n"""
        self.assertEqual(extract_title(markdown_input), "My Project Title")

    def test_exception(self):
        markdown_input = """This is just text.\n
    ## Only an H2 heaader here.\n"""
        with self.assertRaises(Exception) as context:
            extract_title(markdown_input)

        self.assertEqual(str(context.exception), "No title was found.")
