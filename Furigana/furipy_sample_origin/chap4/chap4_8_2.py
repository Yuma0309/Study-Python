def addCharge(bill):
    if bill < 0:
        return 0
    return int(bill * 1.07)


print(addCharge(-1000))
