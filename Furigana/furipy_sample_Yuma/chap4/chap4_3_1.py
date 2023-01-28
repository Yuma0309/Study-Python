def create_mail (receiver, bill) :
    msg = f'''{receiver}様
PT企画の斉藤です。
今月の請求額は{bill}円です。
'''
    print(msg)


create_mail('山本', 40000)