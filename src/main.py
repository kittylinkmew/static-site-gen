import os
import shutil
import sys

from copystatic import copy_files_recursive
from textnode import TextNode, TextType


def main():
    if os.path.exists("./public"):
        shutil.rmtree("./public")
        copy_files_recursive("./static", "./public")


if __name__ == "__main__":
    sys.exit(main())
