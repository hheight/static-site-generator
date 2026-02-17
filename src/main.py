import os
import sys
import shutil

from copystatic import copy_files
from generatepage import generate_pages_recursive

dir_path_public = "docs"
dir_path_static = "static"
dir_path_content = "content"
template_path = "template.html"
basepath = sys.argv[1] if len(sys.argv) > 1 else "/"

def main():
    if os.path.exists(dir_path_public):
       shutil.rmtree(dir_path_public)

    copy_files(dir_path_static, dir_path_public)

    generate_pages_recursive(dir_path_content, template_path, dir_path_public, basepath)

main()
