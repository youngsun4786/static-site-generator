import os
import shutil

def copy_files_recursive(src, dest):
    
    if not os.path.exists(dest):
        os.mkdir(dest)

    # get all items in the source directory
    items = os.listdir(src)

    for item in items:
        src_path = os.path.join(src, item)
        dest_path = os.path.join(dest, item)

        # if the item is a file, copy it directly
        if os.path.isfile(src_path):
            shutil.copy(src_path, dest_path)
        # if the items is a directory, recursively copy its contents
        elif os.path.isdir(src_path):
            copy_files_recursive(src_path, dest_path)



