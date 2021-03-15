from json import dump


with open("nginx_logs.txt", "r", encoding="utf-8") as t:
    dict = collections.Counter()

    for c in t:
        c = c.split()[0]
        dict[c] += 1

    ip, rq = dict.most_common(1)[0][0], dict.most_common(1)[0][1]
    print(f"Спамер {ip} - {rq} запросов")