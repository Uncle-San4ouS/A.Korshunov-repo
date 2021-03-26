def val_checker(l_f):
    def _val_checker(f):
        def wrapper(n):
            if l_f(n):
                print(f(n))
            else:
                raise ValueError(f'incorrect value {n}')
        return wrapper
    return _val_checker

@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3

try:
    a = calc_cube(5)
except ValueError as err:
    print(err)