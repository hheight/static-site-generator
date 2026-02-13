import unittest

from htmlnode import HTMLNode


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



if __name__ == "__main__":
    unittest.main()
