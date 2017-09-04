import itertools
arr = list(map(int, input().split()))
value = 0
count2 = 0
countg = 0
arr1 = list()
arraytot = list()
while value < arr[0]:
    arr1.append(input()[:arr[1]+1])
    value = value + 1

for pair in itertools.combinations(arr1,2):

    team = int(pair[0],2) | int((pair[1]),2)
    teamb = bin(team)[2:].zfill(arr[1])
    tot = 0
    for binary in teamb:
        tot = tot + int(binary)
    arraytot.append(tot)

largest = max(arraytot)
i=0
for i in arraytot:
    if i > 2:
       count2 = count2 + 1
    if i == largest:
        countg = countg + 1

print(count2)
print(countg)


