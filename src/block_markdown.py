from enum import Enum
from textnode import text_node_to_html_node
from htmlnode import ParentNode
from inline_markdown import text_to_textnodes

class BlockType(Enum):
    PARAGRAPH = "paragraph",
    HEADING = "heading",
    CODE = "code",
    QUOTE = "quote",
    UNORDERED_LIST = "unordered_list",
    ORDERED_LIST = "ordered_list",
    



def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)

    return filtered_blocks


def block_to_block_type(block):
    lines = block.split("\n")
    if block.startswith(("#", "##", "###", "####", "#####", "######")):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE

    if len(lines) == len(list(filter(lambda line : line.startswith(">"), lines))):
        return BlockType.QUOTE
    
    if len(lines) == len(list(filter(lambda line : line.startswith(("-", "*")) and line[1] == " ", lines))):
        return BlockType.UNORDERED_LIST

    is_ordered = True
    if lines[0].startswith("1. "):
        for i in range(len(lines)):
            num = int(lines[i][0])
            if not (num == i + 1 and lines[i][1:3] == ". "):
                is_ordered = False

        if is_ordered:
            return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH




def markdown_to_html_node(markdown):
    # 1. split the markdown into blocks
    blocks = markdown_to_blocks(markdown)
    children = []
    # 2. loop over each block
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)

    return ParentNode("div", children, None)

def block_to_html_node(block):
    # 2a. find the block type
    block_type = block_to_block_type(block)
    match block_type:
        case BlockType.PARAGRAPH:
            return paragraph_to_html_node(block)
        case BlockType.HEADING:
            return heading_to_html_node(block)
        case BlockType.CODE:
            return code_to_html_node(block)
        case BlockType.QUOTE:
            return quote_to_html_node(block)
        case BlockType.UNORDERED_LIST:
            return ulist_to_html_node(block)
        case BlockType.ORDERED_LIST:
            return olist_to_html_node(block)
        case _:
            raise ValueError("invalid block type")

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children

def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def heading_to_html_node(block): 
    level = block.count("#")
    if level + 1 >= len(block):
        raise ValueError("invalid header block")
    title = block[level + 1:]
    children = text_to_children(title)
    return ParentNode(f"h{level}", children)

def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("invalid code block")
    code = block[4:-3]
    children = text_to_children(code)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])

def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("invalid quote block")
        # strip any remaining trailing/leading whitespaces
        new_lines.append(line.strip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)

def ulist_to_html_node(block):
    lines = block.split("\n")
    html_items = []
    for line in lines:
        children = text_to_children(line[2:])
        html_items.append(ParentNode("li", children))    
    return ParentNode("ul", html_items)


def olist_to_html_node(block):
    lines = block.split("\n")
    html_items = []
    for line in lines:
        children = text_to_children(line[3:])
        html_items.append(ParentNode("li", children))    
    return ParentNode("ol", html_items)


        











