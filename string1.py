text = "X-DSPAM-Confidence:    0.8475"
atpos= text.find(":")
data = text[atpos+5:]
nbr = float(data)
print(nbr)
