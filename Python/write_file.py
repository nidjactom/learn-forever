from io import UnsupportedOperation

print('Default Windows 10 encoding "cp1252".')
with open('written.txt', mode='w') as out_file:
    out_file.write('This is the first line of the text.\n')

with open('written.txt', mode='a') as append_file:
    append_file.write('This line is appended at the end.\n')

with open('written.txt', mode='r') as in_file:
    print(in_file.read())


lines = (
    'Line1\n', 'Line2\n',
    'Line3\n', 'Line4\n'
    )

try:
    out_file = open('without.txt', mode='w', buffering=1, encoding='us')
    out_file.writelines(lines)
    out_file.flush()
finally:
    out_file.close()

