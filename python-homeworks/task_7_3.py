import os
from shutil import copytree

def dir_copy():
    dir_from = 'my_project'
    dir_to = 'templates'

    for root, dir, file in os.walk(dir_from):
        if root.find(dir_to) > 0 and len(file) == 0:
            copytree(os.path.join(root), dir_to, dirs_exist_ok=True)

if __name__ == '__main__':
    dir_copy()