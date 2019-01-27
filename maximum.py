largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    try:
        n1 = int(num)
    except:
        print("Invalid input")
        continue
    if largest is None or n1 > largest:
        largest = n1
    if smallest is None or n1 < smallest:
        smallest = n1
print("Maximum is", largest)
print("Minimum is", smallest)
