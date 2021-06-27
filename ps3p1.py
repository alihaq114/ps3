print("what is the quanity of widgets bought")
qty = int(input())
if qty > 10000:
    up = 10
else:
    if qty > 5000 and qty < 10000:
        up = 20
    else:
        up = 30
ep = qty * up
tax = ep * 0.007
total = ep + tax
print("your extened price = " + str(ep))
print("your tax = " + str(tax))
print("your total cost is = " + str(total))
