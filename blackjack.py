
import random

crover = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
haert = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
dia = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
spead = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]

trump = crover + haert + dia + spead
random.shuffle(trump)

cpu = trump[0:2]
for i in cpu:
    trump.remove(i)

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

player =trump[0:2]
for i in player:
    trump.remove(i)
print(f"あなたのカードは{player}です")
print(f"ディーラーのアップカードは{cpu[0]}です")
n = input("カードを引きますか？>>>y/n")

if n == "y":
    player.append(trump[0])
    trump.remove(player[2])
elif n == "n":
    if len(cpu) < 15:
        cpu.append(trump[0])
        trump.remove(cpu[2])

print(player)
print(cpu)