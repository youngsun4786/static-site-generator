from textnode import TextNode, TextType
from copystatic import copy_files_recursive
from gencontent import generate_pages_recursive
import os
import shutil


DIR_PATH_STATIC = "./static"
DIR_PATH_PUBLIC = "./public"
DIR_PATH_CONTENT = "./content"
TEMPLATE_PATH = "./template.html"


def main():
    # delete the contents of destination directory first
    if os.path.exists(DIR_PATH_PUBLIC):
        print("Deleting public directory...")
        shutil.rmtree(DIR_PATH_PUBLIC)

    print("Copying static files to public directory...")
    copy_files_recursive(DIR_PATH_STATIC, DIR_PATH_PUBLIC)

    print("Generating page...")
    generate_pages_recursive(
            DIR_PATH_CONTENT,
            TEMPLATE_PATH,
            DIR_PATH_PUBLIC,
    )



if __name__ == "__main__":
    main()
