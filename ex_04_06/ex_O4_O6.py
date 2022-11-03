# creating functions

def compute(hours, rate):
    print("in compute", hours, rate)
    if hours > 40:
        reg = 40 * rate
        otp = (hours - 40.0) * (rate * 0.5)
        pay = reg + otp

    else:
        pay = hours * rate

    # print("calculated payment",pay)
    return pay


sh = input("enter Hours:")
sr = input("enter rate: ")
fh = float(sh)
fr = float(sr)

xp = compute(fh, fr)
print("Pay:", xp)
