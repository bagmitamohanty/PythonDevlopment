fname = input("Enter file name: ")
fh = open(fname)

for line in fh:
  line = line.rstrip()
  print(line.upper())
