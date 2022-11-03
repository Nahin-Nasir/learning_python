# taking input from user and calculating using if else

sh = input('Enter Hours:')
sr = input('Enter Rate:')
fh = float(sh)
fr = float(sr)
if fh <= 40:
    print('regular')
    pay = fh * fr
    print('Payment', pay)
else:
    print('Overtime Hours payment rate 1.5x regular')
    r_pay = 40 * fr
    ot_pay = (fh - 40) * (fr * 1.5)
    t_pay = ot_pay + r_pay
    print('Payment', t_pay)
