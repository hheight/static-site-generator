import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_values(self):
        node = LeafNode("div", "Wow")
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Wow")
        self.assertEqual(node.props, None)

    def test_repr(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = LeafNode("p", "Paragraph text", props)
        self.assertEqual(node.__repr__(), "LeafNode(p, Paragraph text, {'href': 'https://www.google.com', 'target': '_blank'}")

    def test_to_html_p(self):
        node = LeafNode("p", "Paragraph text")
        self.assertEqual(node.to_html(), '<p>Paragraph text</p>')

    def test_to_html_props(self):
        props = {
            "class": "primary",
            "type": "button",
        }
        node = LeafNode("button", "Submit", props)
        self.assertEqual(node.to_html(), '<button class="primary" type="button">Submit</button>')

    def test_to_html_no_value(self):
        node = LeafNode("p", "")
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_no_tag(self):
        node = LeafNode("", "Plain text")
        self.assertEqual(node.to_html(), "Plain text")



if __name__ == "__main__":
    unittest.main()
