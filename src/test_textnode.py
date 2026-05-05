import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

        node3 = TextNode("Blah blah blah!", TextType.ITALIC)
        node4 = TextNode("Blah blah blah!", TextType.TEXT)
        self.assertNotEqual(node3,node4)

        node5 = TextNode("Are we testing?",TextType.BOLD, url = None)
        node6 = TextNode("Are we testing?",TextType.BOLD, url = None)
        self.assertEqual(node5,node6)

        node7 = TextNode("I'm a test.",TextType.TEXT)
        node8 = TextNode("I'm a test.",TextType.TEXT)
        self.assertEqual(node7,node8)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is bold.", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag,"b")
        self.assertEqual(html_node.value, "This is bold.")

    def test_link(self):
        node = TextNode("Alt text", TextType.IMAGE, "https://images.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag,"img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "https://images.com","alt":"Alt text"})
if __name__ == "__main__":
    unittest.main()
