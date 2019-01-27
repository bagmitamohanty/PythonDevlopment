s1 = input ("Enter Score between 0.0 & 1.0:")
score = float(s1)
if score > 1.0 or score < 0.0:
	print("Not Valid score")
elif score >= 0.9 and score < 1.0:
    print("A")
elif score >= 0.8 and score < 0.9:
    print("B")
elif score >= 0.7 and score < 0.8:
    print("C")
elif score >= 0.6 and score < 0.7:
    print("D")
else:
    print("Fail")
