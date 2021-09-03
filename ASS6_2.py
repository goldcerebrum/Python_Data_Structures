text = "X-DSPAM-Confidence:    0.8475"
beginning = text.find('0')

end = text.find('5')

number = text[beginning : end+1]
number = float(number)
print(number)
