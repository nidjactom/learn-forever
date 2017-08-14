import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://cimpp03.netact.nsn-rdnet.net/mpp/static/packages/netact/product/99.17.07.0.445/netact-release')

counts = dict()
for line in fhand:
    words = line.decode().split(',')
    for word in words:
        counts[word] = counts.get(word,0) +1
print(counts)
