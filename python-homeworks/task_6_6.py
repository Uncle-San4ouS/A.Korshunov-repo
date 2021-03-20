import argv

with open('bakery.csv', 'a', encoding='utf-8') as cheesecake_a:
    with open('bakery.csv', 'r', encoding='utf-8') as cheesecake_r:
        if len(argv) > 1 and [n for n in argv[1:] if n.replace('.', '').isdigit()]:
            if len(argv) == 3:
                print(*cheesecake_r.read().split()[int(argv[1]) - 1:int(argv[2])], sep='\n')
            if ',' in argv[1] or '.' in argv[1]:
                cheesecake_r.read()
                print(argv[1], file=cheesecake_a)
            else:
                print(*cheesecake_r.readlines()[int(argv[1]) - 1:], sep='')
        else:
            print(cheesecake_r.read())