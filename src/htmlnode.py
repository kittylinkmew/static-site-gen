

class HTMLNode:
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None or not self.props:
            return ""
        html_string = ""
        for key, value in self.props.items():
            html_string = html_string + " " + key + '="' + value + '"'

        return html_string

    def __repr__(self):
        return (f"HTMLNode({self.tag},{self.value},{self.children},{self.props})")


class LeafNode(HTMLNode):
    def __init__(self,tag,value,props=None):
        super().__init__(tag,value,None,props)

    def to_html(self):
        if not self.value:
            raise ValueError("All leaf nodes must have a value.")
        if self.tag == None:
           return self.value

        if self.props != None:
            props_string = self.props_to_html()
            return "<"+self.tag+props_string+">"+self.value+"</"+self.tag+">"
        return "<"+self.tag+">"+self.value+"</"+self.tag+">"

    def __repr__(self):
        return (f"LeafNode({self.tag},{self.vale},{self.props})")
