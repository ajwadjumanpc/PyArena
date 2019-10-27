import components as cmp
from termcolor import colored

heads = (17, 54, 62, 64, 87, 93, 95, 99)
tails = (7, 34, 19, 60, 24, 73, 75, 78)
snakes = []

for i in range(len(heads)):
    snake = cmp.Snake(heads[i], tails[i])
    snakes.append(snake)


def snake_check(position):
    for snake in snakes:
        if snake.head == position:
            position = snake.tail
            print(colored("""Busted! Python bite
                 Don't Worry! Alice saved you. But your position changed.""", 'red'))
            return position
        else:
            print("No Python")
            return position


def snake_list():
    print("Pythons : ")
    for snake in snakes:
        print(f'\t(Head : {snake.head}, Tail : {snake.tail})')