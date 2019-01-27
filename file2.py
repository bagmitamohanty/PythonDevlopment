# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
i = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    line = line.rstrip()
    i += 1
    atpos= line.find(":")
    data = line[atpos+1:]
    nbr = float(data)
    total = total + nbr
print("Average spam confidence:", total/i)
