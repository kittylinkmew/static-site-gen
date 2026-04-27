import unittest

from htmlnode import HTMLNode, LeafNode

class TestHtmlNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p","Hello")
        self.assertEqual(node.tag,"p")

        node2 = HTMLNode("p","Hello")
        self.assertEqual(node.value,"Hello")

        node3 = HTMLNode("p","Hello",None,{"href": "https://www.google.com", "target": "_blank",})
        result = node3.props_to_html()
        self.assertEqual(result, ' href="https://www.google.com" target="_blank"')

    def test_leaf_to_html_p(self):
        node = LeafNode("p","Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

        node2= LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node2.to_html(), '<a href="https://www.google.com">Click me!</a>')

        node3= LeafNode("p", None, {"href": "https://www.google.com"})
        with self.assertRaises(ValueError):
            node3.to_html()


if __name__ == "__main__":
    unittest.main()
