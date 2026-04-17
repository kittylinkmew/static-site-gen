import sys
from textnode import TextNode
from textnode import TextType

def main():
    my_test = TextNode("This is a test.",TextType.TEXT,"https://mytest.com")
    print(my_test)

if __name__ == "__main__":
    sys.exit(main())
