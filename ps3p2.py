print("enter part number")
pn = int(input())
print("enter how many you bought")
qty = float(input())
if pn == 10 or pn == 55:
    up = 1.0
else:
    if pn == 99:
        up = 2.0
    else:
        if pn == 80 or pn == 70:
            up = 3.0
        else:
            up = 5.0
total = up * qty
print("Part number is = " + str(pn))
print("Your quanity of order is = " + str(qty))
print("Unit price = " + str(up))
print("And finally your total price is = " + str(total))
