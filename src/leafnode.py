from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props=props)

    def to_html(self):
        if not self.value:
            raise ValueError("Leaf node must have a value")
        if not self.tag:
            return self.value
        props_html = self.props_to_html() if self.props else None

        if props_html:
            return f"<{self.tag} {props_html}>{self.value}</{self.tag}>"

        return f"<{self.tag}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props}"
