import collections

with open("nginx_logs.txt", "r", encoding="utf-8") as t:
    cortege = ((raw.split()[0], raw.split()[5][1:], raw.split()[6]) for raw in t)
    for c in cortege:
        print(c)