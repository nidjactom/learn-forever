def is_perfect_cube(x):
    x = abs(x)
    print(int(round(x ** (1. / 3))) ** 3 == x)
    return

is_perfect_cube(63)
