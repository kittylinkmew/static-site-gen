import unittest

from blocks import BlockType, block_to_block_type, markdown_to_blocks


class Test_blocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_block_type_heading(self):
        block = "# Hello World"
        assert block_to_block_type(block) == BlockType.HEADING

        block2 = "### Hello Heading"
        assert block_to_block_type(block2) == BlockType.HEADING

    def test_block_to_block_type_quote(self):
        block = ">This is a quote.\n>This is the second part of the quote."
        assert block_to_block_type(block) == BlockType.QUOTE

    def test_block_to_block_type_code(self):
        block = "```\nThis is a code block\n```"
        assert block_to_block_type(block) == BlockType.CODE

    def test_block_to_block_type_unorderedlist(self):
        block = "- This is a list.\n- It is unordered.\n- It has three items."
        assert block_to_block_type(block) == BlockType.UNORDERED_LIST

    def test_block_to_block_type_orderedlist(self):
        block = "1. This is a list.\n2. It is ordered.\n3. It has three items."
        assert block_to_block_type(block) == BlockType.ORDERED_LIST

    def test_paragraph(self):
        block = "This is a normal paragraph.\nIt has multiple lines.\nI hate writng tests so much."
        assert block_to_block_type(block) == BlockType.PARAGRAPH

    def test_block_paragraph(self):
        block = "######## This looks like a heading but it is a paragraph."
        assert block_to_block_type(block) == BlockType.PARAGRAPH

        block2 = "```This looks like code.\nIt is missing the final back ticks."
        assert block_to_block_type(block2) == BlockType.PARAGRAPH


if __name__ == "__main__":
    unittest.main()
