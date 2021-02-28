prices = [57.8, 46.51, 97, 32, 27.05, 43, 12.48, 17, 9.12, 100.1, 27, 55.55, 892.99, 1400, 99.99]

print(f"\n\n{'*'*35} A_1\n")

for i in prices:
    rub, kop = str(f"{i:.2f}").split(".")
    print(f"{rub} руб {int(kop):02d} коп,", end=" ")