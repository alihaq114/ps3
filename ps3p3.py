print("Enter the principle amount of a CD")
prn = float(input())
print("enter the year of maturity of CD")
years = int(input())
if prn > 100000 and years == 5:
    ir = 0.006
else:
    if prn > 50000 and prn < 100000 and years == 10:
        ir = 0.005
    else:
        if prn > 50000 and prn < 100000 and years == 5:
            ir = 0.004
        else:
            ir = 0.002
iffy = prn * ir
print("your principle is = " + str(prn))
print("your intrest rate = " + str(ir))
print("your intrest for the first year is = " + str(iffy))
