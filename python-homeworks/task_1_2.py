cubes_list = []
cubes_list_add = []
sum_all = 0

for i in range(1, 1001, 2):
    cubes_list.append(i ** 3)

for ind, val in enumerate(cubes_list):
    sum_digits = 0
    while val > 0:
        sum_digits += val % 10
        val //= 10
    if sum_digits % 7 == 0:
        sum_all += cubes_list[ind]

print(sum_all)

for a in cubes_list:
    cubes_list_add.append(a + 17)

sum_all = 0

for ind, val in enumerate(cubes_list_add):
    sum_digits = 0
    while val >0:
        sum_digits += val % 10
        val //= 10
    if sum_digits % 7 == 0:
        sum_all += cubes_list_add[ind]

print(sum_all)






