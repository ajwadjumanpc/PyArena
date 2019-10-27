from termcolor import colored


class Snake:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail


heads = [17, 54, 62, 64, 87, 93, 95, 99]
tails = [7, 34, 19, 60, 24, 73, 75, 78]

snakes = []

for i in range(len(heads)):
    snake = Snake(heads[i], tails[i])
    snakes.append(snake)


def snake_check(position):
    ini_pos = position
    for snake in snakes:
        if snake.head == position:
            position = snake.tail
        else:
            pass
    if ini_pos != position:
        print(colored("""Busted! Python bite
                            Don't Worry! Alice saved you. But your position changed.""", 'red'))
    else:
        print("No python")
    return position


def snake_list():
    print("Pythons : ")
    for snake in snakes:
        print(f'\t(Head : {snake.head}, Tail : {snake.tail})')
