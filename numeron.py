import random

num = [0,1,2,3,4,5,6,7,8,9]
number = []
eat = 0
bite = 0
clear = 0
a = 0
challenge_num = 0

random.shuffle(num)

for i in num:
    num.remove(i)
    number.append(i)
    if len(num) < 8:
        break

print(number)

while eat < 3:
    x = 0
    a = 0
    num_x = int(input("3桁の数字を入力してください>>"))
    num1 = num_x / 100
    num1 = int(num1)
    num2 = num_x / 10 - num1 * 10
    num2 = int(num2)
    num3 = num_x - num1 * 100 -num2 * 10
    num3 = int(num3)
    
    print(num1,num2,num3)

    for x in number:
        if a == 0:
            if num1 == x:
                eat += 1
            elif num2 == x:
                bite += 1
            elif num3 == x:
                bite += 1
        if a == 1:
            if num1 == x:
                bite += 1
            elif num2 == x:
                eat += 1
            elif num3 == x:
                bite += 1
        if a == 2:
            if num1 == x:
                bite += 1
            elif num2 == x:
                bite += 1
            elif num3 == x:
                eat += 1
        a += 1

    challenge_num += 1

    if eat < 3:
        print(f"{eat}EAT,{bite}BITE")
        eat = 0
        bite = 0

print("おめでとうございます\nクリアです")
print(f"あなたがクリアするまで{challenge_num}回かかりました")