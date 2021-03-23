
import os
import django
from collections import defaultdict

def dir_info():
    dir_root = django.__path__[0]
    file_django = defaultdict(int)

    for root, dir, file in os.walk(dir_root):
        for f in file:
            size = 10 ** len(str(os.stat(os.path.join(root, f)).st_size))
            file_django[size] += 1

    for size, nums in sorted(file_django.items()):
        print(f'{size}: {nums}')

dir_info()