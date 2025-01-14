import random
janken_list = ["g","y","p"]
print("じゃんけんをします")
print("最初はグーじゃんけん・・・")

# 手の強弱
strong = {"g":"p","p":"y","y":"g"}

# 出した手をわかりやすくする
janken_te = {"g":"グー","p":"パー","y":"チョキ"}

# プレイヤーの手を決めるための関数
def player_choice():
    player = 0
    n = True
    while n == True:
        player = input("グーの場合はg、チョキの場合はy、パーの場合はpを入力してください>>>")
        if player == "g" or player == "y" or player == "p":
            n = False
        else: print("g,y,pのいずれかを半角小文字で入力してください")
    return player


# プレイヤーの手を決定
player = player_choice()

# CPUの手を決める
cpu = random.choice(janken_list)


# あいこの場合ループから抜け出せないようにする
while cpu == player:
        print(f"CPU>>>{janken_te[cpu]}")
        print("あいこです")
        print("あいこで・・・")
        player = player_choice()
        cpu = random.choice(janken_list)


# 勝敗を判定と結果の出力
if player == strong[cpu]:
    print(f"CPU>>>{janken_te[cpu]}\nあなたの勝ちです")
else: print(f"CPU>>>{janken_te[cpu]}\nあなたの負けです")