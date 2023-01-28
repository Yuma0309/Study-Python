text = input('年齢は？')
if text.isdigit():
    age = int(text)
    if age < 20:
        if age >= 6 and age <= 15:
          print('未成年（義務教育)')
        else:
            print('未成年')
