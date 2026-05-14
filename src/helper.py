from textnode import TextType, TextNode
import re

#delimiter function that seperates nodes by type using characters
def split_nodes_delimiter(old_nodes, delimiter, text_type):

    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        nodes = node.text.split(delimiter)
        if len(nodes) % 2 == 0:
            raise Exception("invalid Markdown syntax")

        for index, text in enumerate(nodes):
            if text.strip():
                if index % 2== 0:
                    node = TextNode(text, TextType.TEXT)
                    new_nodes.append(node)
                else:
                    node = TextNode(text, text_type)
                    new_nodes.append(node)
    return new_nodes

#function that takes raw markdown text and returns a list of tuples for images
def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)",text)
    return matches


#function that takes raw markdown text and returns a list of tuples for links
def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)",text)
    return matches
