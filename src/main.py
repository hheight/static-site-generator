import os
import shutil

from copystatic import copy_files

dest_dir = "./public"
source_dir = "./static"

def main():
    if os.path.exists(dest_dir):
       shutil.rmtree(dest_dir)

    copy_files(source_dir, dest_dir)


main()
