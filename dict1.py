fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
counts = dict()
for line in fh:
    line = line.rstrip()
    if not line.startswith("From "): continue
    words = line.split()
    counts[words[1]] = counts.get(words[1],0) + 1

largest = -1
key = None
for k,v in counts.items():
    if v > largest:
        largest = v
        key = k
print(key,largest)
