import unittest

from inline_markdown import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitDelimiter(unittest.TestCase):
    def test_code_delim(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ]
         )

    def test_code_delim_double(self):
        node = TextNode("This is text with a `code block` word and `another one`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word and ", TextType.TEXT),
                TextNode("another one", TextType.CODE),
            ]
         )

    def test_bold_delim(self):
        node = TextNode("This is text with a **bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)

        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ]
         )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and _italic_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )

    def test_italic_delim(self):
        node = TextNode("This is text with a _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)

        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ]
         )

    def test_is_not_text_type(self):
        node = TextNode("This is code", TextType.CODE)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)

        self.assertEqual(
            new_nodes,
            [
                TextNode("This is code", TextType.CODE),
            ]
         )

    def test_invalid_markdown(self):
        node = TextNode("This is text with a _italic word", TextType.TEXT)

        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "_", TextType.ITALIC)


if __name__ == "__main__":
    unittest.main()
