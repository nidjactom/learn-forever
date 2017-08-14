import re

filename = input('Input the filename: ')
fh = open(filename)

lines = fh.read()
numbers = re.findall('\d+',lines)
numbers = list(map(int, numbers))
length = len(numbers)
print(sum(numbers))
print(length)
