fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
counts = dict()
for line in fh:
    line = line.rstrip()
    if not line.startswith("From "): continue
    words = line.split()
    hour = words[5]
    hr = hour.split(":")
    counts[hr[0]] = counts.get(hr[0],0) + 1

lst = list()
for key,val in list(counts.items()):
    lst.append((key,val))

lst.sort()
for key,val in lst:
    print(key,val)
