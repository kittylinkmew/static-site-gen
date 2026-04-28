import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

        child_node2 = LeafNode("span","child")
        parent_node2 = ParentNode(None,[child_node2])
        with self.assertRaises(ValueError):
            parent_node2.to_html()

        parent_node3 = ParentNode("div",None)
        with self.assertRaises(ValueError):
            parent_node3.to_html()

        child_node4 = LeafNode("p","Hello World!")
        parent_node4 = ParentNode("div",[child_node4],{"href": "https://www.google.com"})
        self.assertEqual(parent_node4.to_html(),'<div> href="https://www.google.com"<p>Hello World!</p></div>')


    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

if __name__ == "__main__":
    unittest.main()
