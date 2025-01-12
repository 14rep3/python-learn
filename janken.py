import random
i = ["g","y","p"]
print("じゃんけんをします")
print("最初はグーじゃんけん・・・")
x = input("グーの場合はg、チョキの場合y、パーの場合pを入力してください")
if x == "g":
    y = random.choice(i)
    if y == "g":
        print("CPUはグーを出しました")
        print("あいこです")
    elif y == "y":
        print("CPUはチョキを出しました")
        print("プレイヤーの勝ちです")
    elif y == "p":
        print("CPUはパーを出しました")
        print("あなたの負けです")

if x == "y":
    y = random.choice(i)
    if y == "g":
        print("CPUはグーを出しました")
        print("あいこです")
    elif y == "y":
        print("CPUはチョキを出しました")
        print("プレイヤーの勝ちです")
    elif y == "p":
        print("CPUはパーを出しました")
        print("プレイヤーの負けです")

if x == "p":
    y = random.choice(i)
    if y == "g":
        print("CPUはグーを出しました")
        print("プレイヤーの勝ちです")
    elif y == "y":
        print("CPUはチョキを出しました")
        print("プレイヤーの負けです")
    elif y == "p":
        print("CPUはパーを出しました")
        print("あいこです")

if x != "g" and x != "y" and x != "p":
    print("半角でg,y,pのどれかを入力してください")