from itertools import islice
n = int(input("Введите граничное число: "))

nums_gen = (num * 1 for num in range(1, n + 1, 2))

print(*islice(nums_gen, n))