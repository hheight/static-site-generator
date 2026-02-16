import re
from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        sections = old_node.text.split(delimiter)

        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")

        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                new_nodes.append(TextNode(sections[i], text_type))

    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_image(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        extracted_images = extract_markdown_images(old_node.text)

        if len(extracted_images) == 0:
            new_nodes.append(old_node)
            continue

        remaining_text = old_node.text

        for i in range(len(extracted_images)):
            image_alt = extracted_images[i][0]
            image_url = extracted_images[i][1]
            sections = remaining_text.split(f"![{image_alt}]({image_url})", 1)

            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))

            new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_url))

            remaining_text = sections[1]
        if remaining_text != "":
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        extracted_links = extract_markdown_links(old_node.text)

        if len(extracted_links) == 0:
            new_nodes.append(old_node)
            continue

        remaining_text = old_node.text

        for i in range(len(extracted_links)):
            link_text = extracted_links[i][0]
            link_url = extracted_links[i][1]
            sections = remaining_text.split(f"[{link_text}]({link_url})", 1)

            if len(sections) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))

            new_nodes.append(TextNode(link_text, TextType.LINK, link_url))

            remaining_text = sections[1]
        if remaining_text != "":
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))

    return new_nodes

def text_to_textnodes(text):
    node = TextNode(text, TextType.TEXT)
    return split_nodes_image(
                split_nodes_link(
                    split_nodes_delimiter(
                        split_nodes_delimiter(
                            split_nodes_delimiter(
                                [node], "`", TextType.CODE
                            ), "**", TextType.BOLD
                        ), "_", TextType.ITALIC
                    )
                )
            )
