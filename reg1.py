import re
hand = open("regex_sum_133333.txt")
tot = 0
for line in hand:
    line = line.rstrip()
    x = re.findall('[0-9]+',line)
    if len(x) < 0:
        break
    for nbr in x:
        tot = tot + int(nbr)
print(tot)
