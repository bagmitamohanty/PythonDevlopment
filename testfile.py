fname = input("Enter file name")

if fname == "":
    fname = "test.txt"

try:
    fhand = open(fname)
except:
    print("File not exists")
    exit()

#inp = fhand.read()
#print(len(inp))

count = 0
for line in fhand:
    line = line.rstrip()
    line = line.split()
    for word in line:
        count += 1
        print(word)

print("count", count)
