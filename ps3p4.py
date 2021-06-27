print("enter the amount of tickets that you wanna buy")
nct = int(input())
if nct >= 25:
    ppt = 50
else:
    if nct > 10 and nct < 24:
        ppt = 60
    else:
        if nct > 5 and nct < 9:
            ppt = 70
        else:
            if nct < 5:
                ppt = 75
            else:
                ppt = 0
total = nct * ppt
print("The number of tickets you bought is = " + str(nct))
print("The cost per tickets is = " + str(ppt))
print("and now the your total cost is........ $" + str(total))
