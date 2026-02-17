import os
import shutil

def copy_files(source_dir, dest_dir):
    if not os.path.exists(source_dir):
        raise Exception("Source directory does not exists")
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)

    # copy files
    for item in os.listdir(source_dir):
        source_item_path = os.path.join(source_dir, item)
        dest_item_path = os.path.join(dest_dir, item)

        if os.path.isfile(source_item_path):
            shutil.copy(source_item_path, dest_item_path)
        else:
            copy_files(source_item_path, dest_item_path)
