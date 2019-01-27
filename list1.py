fname = input("Enter file name: ")
fh = open(fname)

lst = list()
for line in fh:
    line = line.rstrip()
    words = line.split()
    for word in words:
        lst.append(word)
        a = set(lst)
print(sorted(a))
