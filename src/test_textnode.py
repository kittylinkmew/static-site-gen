import unittest

from textnode import TextNode, TextType


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

if __name__ == "__main__":
    unittest.main()
