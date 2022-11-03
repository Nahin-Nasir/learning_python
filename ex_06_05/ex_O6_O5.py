# slicing and extracting from string

str = 'X-DSPAM-Confidence: 0.8475 '
colpos = str.find(':')
print(colpos)
data = str[colpos + 1:]
value = float(data)
print(value)
