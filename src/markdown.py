from blocks import *
from helper import *
from htmlnode import *
from textnode import *


def markdown_to_html_node(markdown):
    split_markdown = markdown_to_blocks(markdown)
    block_nodes = []

    for block in split_markdown:
        type = block_to_block_type(block)

        if type == BlockType.PARAGRAPH:
            lines = block.split("\n")
            paragraph = " ".join(lines)
            children = text_to_children(paragraph)
            node = ParentNode("p", children)
            block_nodes.append(node)

        elif type == BlockType.HEADING:
            level = 0
            for char in block:
                if char == "#":
                    level += 1
                else:
                    break
            strip_block = block.lstrip("#").strip()
            children = text_to_children(strip_block)
            node = ParentNode(f"h{level}", children)
            block_nodes.append(node)

        elif type == BlockType.QUOTE:
            block_split = block.split("\n")
            stripped = []
            for line in block_split:
                strip_line = line.lstrip("> ")
                stripped.append(strip_line)

            content = " ".join(stripped)
            children = text_to_children(content)
            node = ParentNode("blockquote", children)
            block_nodes.append(node)

        elif type == BlockType.ORDERED_LIST:
            split_blocks = block.split("\n")
            children = []
            for line in split_blocks:
                parts = line.split(". ", 1)
                text = parts[1]
                child = text_to_children(text)
                li_node = ParentNode("li", child)
                children.append(li_node)
            node = ParentNode("ol", children)
            block_nodes.append(node)

        elif type == BlockType.UNORDERED_LIST:
            split_blocks = block.split("\n")
            children = []

            for line in split_blocks:
                stripped_line = line.lstrip("- ")
                child = text_to_children(stripped_line)
                li_node = ParentNode("li", child)
                children.append(li_node)
            node = ParentNode("ul", children)
            block_nodes.append(node)

        elif type == BlockType.CODE:
            text = block[4:-3]
            raw = TextNode(text, TextType.TEXT)
            child = text_node_to_html_node(raw)

            code_node = ParentNode("code", [child])
            pre_node = ParentNode("pre", [code_node])
            block_nodes.append(pre_node)

    return ParentNode("div", block_nodes)


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []

    for node in text_nodes:
        html_node = text_node_to_html_node(node)
        children.append(html_node)

    return children
