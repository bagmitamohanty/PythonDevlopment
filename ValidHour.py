
while True:
    hr = input("Enter Hours:")
    rt = input("Enter Rate:")
    if hr == "Done":
        break
    try:
        pay = float(hr) * float(rt)
    except:
        print("Not valid numbers")
        continue

print (pay)
