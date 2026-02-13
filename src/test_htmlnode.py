import unittest

from htmlnode import LeafNode, ParentNode, HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_values(self):
        node = HTMLNode("<div>", "Wow")
        self.assertEqual(node.tag, "<div>")
        self.assertEqual(node.value, "Wow")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_repr(self):
        child_node = HTMLNode()
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = HTMLNode("p", "Paragraph text", [child_node], props)
        self.assertEqual(node.__repr__(), "HTMLNode(p, Paragraph text, children: [HTMLNode(None, None, children: None, None], {'href': 'https://www.google.com', 'target': '_blank'}")

    def test_props_to_html(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = HTMLNode(props=props)
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_props_to_html_is_none(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), '')

    def test_leaf_repr(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = LeafNode("p", "Paragraph text", props)
        self.assertEqual(node.__repr__(), "LeafNode(p, Paragraph text, {'href': 'https://www.google.com', 'target': '_blank'}")

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Paragraph text")
        self.assertEqual(node.to_html(), '<p>Paragraph text</p>')

    def test_leaf_to_html_props(self):
        props = {
            "class": "primary",
            "type": "button",
        }
        node = LeafNode("button", "Submit", props)
        self.assertEqual(node.to_html(), '<button class="primary" type="button">Submit</button>')

    def test_leaf_to_html_no_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Plain text")
        self.assertEqual(node.to_html(), "Plain text")

    def test_parent_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_parent_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_parent_to_html_with_props(self):
        props = {
            "class": "primary",
            "type": "button",
        }
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("button", [child_node], props)
        self.assertEqual(parent_node.to_html(), '<button class="primary" type="button"><span>child</span></button>')

    def test_parent_to_html_without_tag(self):
        children = [LeafNode("b", "bold")]
        node = ParentNode(None, children)

        with self.assertRaises(ValueError):
            node.to_html()

    def test_parent_to_html_without_children(self):
        node = ParentNode("p", None)

        with self.assertRaises(ValueError):
            node.to_html()

    def test_parent_repr(self):
        children = [LeafNode("b", "bold")]
        node = ParentNode("p", children)
        self.assertEqual(node.__repr__(), "ParentNode(p, children: [LeafNode(b, bold, None], None)")


if __name__ == "__main__":
    unittest.main()
