
import random

i = True

# トランプと山札の作成
crover = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
haert = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
dia = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
spead = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]

trump = crover + haert + dia + spead
random.shuffle(trump)

# 山札から最初の手札を配る関数
def hand_card():
    global trump
    hand = []
    hand = trump[0:2]
    for i in hand:
        trump.remove(i)
        return hand

# 山札からカードを引く関数
def cpu_draw():
    global trump
    draw = 0
    draw.append(trump[0])
    trump.remove(cpu[-1])
    return draw

# J,Q,K,Aを数字として扱うための辞書
num_change = {"J":10,"Q":10,"K":10,"A":1}

cpu = hand_card()
player = hand_card()

for x in cpu:
    if x == "J":
        cpu.insert(1,10)
        cpu.remove("J")
    elif x == "Q":
        cpu.insert(1,10)
        cpu.remove("Q")
    elif x =="K":
        cpu.insert(1,10)
        cpu.remove("K")
    elif x =="A":
        cpu.insert(1,1)
        cpu.remove("A")


print(f"あなたのカードは{player}です。\nディーラーのアップカードは{cpu[0]}です。")

while i == True:
    n = input("カードを引きますか？>>>y/n")
    if n == "y" or n == "n":
        i = False
    else: print("入力が正しくありません\n半角小文字でyかnを入力してください")

if n == "y":
    player.append(trump[0])
    trump.remove(player[2])
elif n == "n":
    if len(cpu) < 15:
        cpu.append(trump[0])
        trump.remove(cpu[2])

print(player)
print(cpu)