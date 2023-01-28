import chap4func
data = [
    {'name': '山本', 'bill': 40000, 'crg': True},
    {'name': '吉田', 'bill': 25000, 'crg': False}
]
for record in data:
    bill = record['bill']
    if record['crg']:
        bill = chap4func.add_charge(bill)
    chap4func.create_mail(record['name'], bill)
