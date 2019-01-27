fr = input("Enter Fahrenheit Temperature:")
try:
  fahr = float(fr)
except:
    print("Not valid input")
    exit()

cel = (fahr-32.0) * 5/9
print (cel)
