# FizzBuzz問題
# ①1から100までの数字を画面に表示する
# ②数字が3の倍数のときは数字の代わりに「Fizz」と表示する
# ③数字が5の倍数のときは数字の代わりに「Buzz」と表示する
# ④数字が3かつ5の倍数のときは数字の代わりに「FizzBuzz」と表示する

for i in range(1, 101):
    if i%3==0 and i%5==0:
        print("FizzBuzz!")
    elif i%3==0:
        print("Fizz!")
    elif i%5==0:
        print("Buzz!")
    else:
        print(i)