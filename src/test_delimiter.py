import unittest

from delimiter import split_nodes_delimiter
from textnode import TextType , TextNode

class TestInlineMarkdown(unittest.TestCase):
    def test_code_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)

    def test_bold_delimiter(self):
        node = TextNode("This is text with a **bold block** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bold block", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)

    def test_italic_delimiter(self):
        node = TextNode("This is text with a _italic block_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("italic block", TextType.ITALIC),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)

    def test_not_text_type_text(self):
        node = TextNode("**This text is all bold**", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node],"**",TextType.BOLD)
        expected = [TextNode("**This text is all bold**", TextType.BOLD)]

        self.assertEqual(new_nodes, expected)

    def test_no_delimiter_in_text(self):
        node = TextNode("This is just plain text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [TextNode("This is just plain text", TextType.TEXT)]

        self.assertEqual(new_nodes, expected)

    def test_unmatched_delimiter(self):
        node = TextNode("I an tired **bold text of testing", TextType.TEXT)
        with self.assertRaises(Exception):
            new_nodes = split_nodes_delimiter([node],"**",TextType.CODE)




if __name__ == "__main__":
    unittest.main()
