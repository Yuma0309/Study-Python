def add_charge(bill):
    if bill < 0:
        return 0
    return int(bill * 1.07)


print(add_charge(-1000))