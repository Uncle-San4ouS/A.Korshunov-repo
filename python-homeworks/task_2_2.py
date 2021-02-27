input_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
output_list = []

for i in input_list:
    if i.replace("+", "").replace("-", "").isdigit():
        if i.isdigit():
            output_list.append(f"'{int(i):02}'")
        else:
            output_list.append(f"'{i[0]}{int(i[1:]):02}'")
    else:
        output_list.append(i)

print(output_list)
print("".join(output_list))