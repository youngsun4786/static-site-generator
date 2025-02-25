class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise Exception("NotImplementedError")

    def props_to_html(self):
        
        if self.props is None:
            return ""
        
        props_html = ""

        if self.props:
            for key, value in self.props.items():
                props_html += f' {key}="{value}"'
            
        return props_html


    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Invalid HTML: no value")

        if self.tag is None:
            return self.value

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):

    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Invalid HTML: no tag")

        if self.children is None or len(self.children) == 0:
            raise ValueError("Invalid HTML: children missing")

        children_html = ""
        for child in self.children:
            children_html += child.to_html()

        return f"<{self.tag}>{children_html}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
