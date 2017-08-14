from pprint import PrettyPrinter

matrix_a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]

matrix_b = [
    [2, 4, 5],
    [12, 15, 18],
    [28, 32, 36]
    ]

matrix_add = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
    ]

rows = range(len(matrix_a))
cols = range(len(matrix_a[0]))

for row in rows:
    for col in cols:
        matrix_add[row][col] = matrix_a[row][col] + matrix_b[row][col]

pp = PrettyPrinter()
pp.pprint(matrix_add)
