import os

from block_markdown import markdown_to_html_node
from inline_markdown import extract_title


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from { from_path } to { dest_path } using { template_path }")

    with open(from_path, encoding="utf-8") as f:
        markdown_file_content = f.read()

    with open(template_path, encoding="utf-8") as f:
        template_file_content = f.read()

    markdown_html_string = markdown_to_html_node(markdown_file_content).to_html()
    page_title = extract_title(markdown_file_content)

    updated_template_html = template_file_content.replace("{{ Title }}", page_title).replace("{{ Content }}", markdown_html_string)

    if not os.path.isdir(os.path.dirname(dest_path)):
        os.makedirs(os.path.dirname(dest_path))

    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(updated_template_html)
