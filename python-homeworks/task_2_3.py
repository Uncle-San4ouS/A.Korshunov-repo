input_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for i, o in enumerate(input_list):
    if o.replace("+", "").replace("-", "").isdigit():
        if o.isdigit():
            input_list[i] = f'"{int(o):02}"'
        else:
            input_list[i] = f'"{o[0]}{int(o[1:]):02}"'

print(input_list)
print("".join(input_list))