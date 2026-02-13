import unittest

from leafnode import LeafNode
from parentnode import ParentNode


class TestParentNode(unittest.TestCase):
    def test_values(self):
        children = [LeafNode("b", "bold")]
        node = ParentNode("div", children)
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.children, children)
        self.assertEqual(node.props, None)

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_props(self):
        props = {
            "class": "primary",
            "type": "button",
        }
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("button", [child_node], props)
        self.assertEqual(parent_node.to_html(), '<button class="primary" type="button"><span>child</span></button>')

    def test_to_html_without_tag(self):
        children = [LeafNode("b", "bold")]
        node = ParentNode("", children)

        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_without_children(self):
        node = ParentNode("p", [])

        with self.assertRaises(ValueError):
            node.to_html()

    def test_repr(self):
        children = [LeafNode("b", "bold")]
        node = ParentNode("p", children)
        self.assertEqual(node.__repr__(), "ParentNode(p, children: [LeafNode(b, bold, None], None)")


if __name__ == "__main__":
    unittest.main()
