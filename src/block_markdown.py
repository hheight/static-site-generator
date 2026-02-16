def markdown_to_blocks(markdown):
    blocks = []

    for block in markdown.split("\n\n"):
        if block != "":
            blocks.append(block.strip())

    return blocks
