fname = input("Enter file name: ")
count=0
hours = dict()
fh = open(fname)
for line in fh:
    line.rstrip()
    if line.startswith('From '):
        pieces = line.split()
        piece = pieces[5].split(':')        
        hours[piece[0]] = hours.get(piece[0],0) + 1
for key, value in sorted(hours.items()):
    print(key,value)

