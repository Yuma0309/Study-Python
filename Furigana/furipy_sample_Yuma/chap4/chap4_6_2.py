import chap4func
data = [
    {'name': '山本', 'bill': 40000, 'crg': True},
    {'name': '吉田', 'bill': 25000, 'crg': False}
]
for recoad in data:
    bill = recoad['bill']
    if recoad['crg']:
        bill = chap4func.add_charge(bill)
    chap4func.create_mail(recoad['name'], bill)