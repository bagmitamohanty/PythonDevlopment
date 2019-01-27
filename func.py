
hour = input("Enter Hours:")
rate = input("Enter Rate:")

try:
    hr = float(hour)
    rt = float(rate)
except:
    print("Not valid input")
    exit()

def computepay(hr,rt):
    if hr > 40:
        pay = ((hr - 40) * (1.5 * rt)) + (40 * rt)
    else:
        pay = (hr * rt)

    return pay

calc = computepay(hr,rt)
print ("Pay:", calc)
