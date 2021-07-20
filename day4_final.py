import random

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map1 = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
aa = list(map(int, str(position)))
# map[position] = "x"-------------------------
print(f"{row1}\n{row2}\n{row3}")