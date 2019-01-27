s1 = input ("Enter Score between 0.0 & 1.0:")

try:
  score = float(s1)
except:
  print("Bad Score")
  exit()

def computegrade(score):
    if score > 1.0:
        print("Not Valid score")
    elif score >= 0.9 and score < 1.0:
        print("Grade A")
    elif score >= 0.8 and score < 0.9:
        print("Grade B")
    elif score >= 0.7 and score < 0.8:
        print("Grade D")
    else:
        print("Fail")

computegrade(score)
