arr1 = list()
for i in range(5):
    arr1.append(i)
 calculate(arr1)

def calculate(arr):
    sum = 0
    for i in arr:
        if i % 2 != 0:
            sum = sum + 1