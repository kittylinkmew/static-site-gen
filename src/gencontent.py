import os

from htmlnode import *
from markdown import markdown_to_html_node


def extract_title(markdown):
    for line in markdown.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    raise Exception("No title was found.")


def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    markdown_file = open(from_path)
    markdown_file_content = markdown_file.read()
    markdown_file.close()
    template_file = open(template_path)
    template_path_content = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_file_content)
    html_string = node.to_html()

    title = extract_title(markdown_file_content)

    result = (
        template_path_content.replace("{{ Title }}", title)
        .replace("{{ Content }}", html_string)
        .replace('href="/', f'href="{basepath}"')
        .replace('src="/', f'src="{basepath}')
    )

    directory = os.path.dirname(dest_path)
    os.makedirs(directory, exist_ok=True)

    dest_file = open(dest_path, "w")

    dest_file.write(result)
    dest_file.close()


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):

    for entry in os.listdir(dir_path_content):
        full_path = os.path.join(dir_path_content, entry)

        if os.path.isfile(full_path):
            if entry.endswith(".md"):
                html_name = entry.replace(".md", ".html")
                dest_file_path = os.path.join(dest_dir_path, html_name)
                generate_page(full_path, template_path, dest_file_path, basepath)
        else:
            new_dest_dir = os.path.join(dest_dir_path, entry)
            generate_pages_recursive(full_path, template_path, new_dest_dir, basepath)
