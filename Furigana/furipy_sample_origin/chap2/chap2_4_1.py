text = input('数字を入力せよ')
if text.isdigit():
    print(100 - int(text))
else:
    print('数字ではない')
