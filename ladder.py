import components as cmp
from termcolor import colored

tops = (14, 31, 38, 84, 59, 67, 81, 91)
bottoms = (4, 9, 20, 28, 40, 51, 63, 71)
ladders = []

for i in range(len(tops)):
    ladder = cmp.Ladder(tops[i],bottoms[i])
    ladders.append(ladder)


def ladder_check(position):
    for ladder in ladders:
        if ladder.bottom == position:
            position = ladder.top
            print(colored("Congrats, Got up a rope.", 'blue'))
            return position
        else:
            print("No Rope")
            return position


def ladder_list():
    print("Ropes : ")
    for ladder in ladders:
        print(f'\t(Foot : {ladder.bottom}, Top : {ladder.top})')