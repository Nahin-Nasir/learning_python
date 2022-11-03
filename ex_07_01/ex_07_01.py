# reading files
filename = input('Enter a file name:')
try:
    fh = open(filename)

except:
    print('File not available')
    quit()

count = 0
for lines in fh:
    linestrip = lines.rstrip()
    print(linestrip.upper())
    count = count + 1
print('Total Lines in the text:', count)
