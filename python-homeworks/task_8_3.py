from functools import wraps

def type_logger(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        nums = [a for a in (*args, *kwargs.values())]
        n = [f'{f.__name__}({a}: {type(a)})' for a in nums]
        print(*n, *f(*args, **kwargs), sep=',\n')
    return wrapper

@type_logger
def calc_cube(*x, **y):
    nums = [a for a in (x, y.values()) if isinstance(a, int) or isinstance(a, float)]
    return [i for i in nums]

#r = calc_cube(3, 15, 10.2, 64, b=53.6, c=7)
#r = calc_cube(1, {'num':8}, (3, 'word'), {7, 9}, [20, 15], 'raw', car='BMW_X5')
#help(calc_cube)
print(calc_cube.__name__)
