from json import dump
from itertools import zip_longest

with open("users.csv", "r", encoding="cp1251") as u:
    with open("hobby.csv", "r", encoding="cp1251") as h:

        if len(u.readlines()) > len(h.readlines()):
            with open("user_hobby.txt", "w", encoding="cp1251") as t:
                u_h = zip_longest(u, h, fillvalue=None)
                dict = {str(p[0]).strip(): (p[1].strip()) for p in u_h}

                dump(dict, t, ensure_ascii=False, indent=4)
            print(dict)
        else:
            exit(1)