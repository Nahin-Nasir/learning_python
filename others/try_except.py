num = input('enter a number here :')
try:
    e_number = int(num)
except:
    e_number = -1

if e_number > 0:
    print("Number Submitted")
else:
    print('not a number')
