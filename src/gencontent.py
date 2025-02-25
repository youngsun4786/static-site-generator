import os
import pathlib
from block_markdown import markdown_to_html_node

def generate_page(src, template, dest):
    print(f"* {src} {template} -> {dest}")
    src_file = open(src, "r")
    markdown_content = src_file.read()
    src_file.close()

    template_file = open(template, "r")
    template_content = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)
    template_content = template_content.replace("{{ Title }}", title)
    template_content = template_content.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest, "w")
    to_file.write(template_content)

def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("no title found")


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):

    for entry in os.listdir(dir_path_content):
        src_path = os.path.join(dir_path_content, entry)
        dest_path = os.path.join(dest_dir_path, entry)
        
        if os.path.isfile(src_path):
            generate_page(src_path, template_path, dest_path.replace(".md", ".html"))
        else:
            generate_pages_recursive(src_path, template_path, dest_path)
