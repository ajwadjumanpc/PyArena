import random as rd
import process as pro
from termcolor import colored, cprint


class Player:
    def __init__(self, id, name, position, status):
        self.id = id
        self.name = name
        self.position = position
        self.status = status


class Dice:
    def __init__(self):
        pass

    def roll(self):
        value = rd.randint(1, 6)
        return value


class Game:
    def __init__(self, status, players):
        self.status = status
        self.players = players

    def init_game(self):
        pro.game_init()

    def play_game(self):
        command = ""
        while command != "stop":
            for i in range(len(self.players)):
                self.play_terminal(i)

    def extra_chance(self, id):
        self.play_terminal(id)

    def play_terminal(self, id):
        command = input(f'{self.players[id].name}>').lower()
        if command == 'roll':
            indicator = pro.play(id)
            if indicator == 6:
                cprint("Hurray! One more chance", 'green')
                self.extra_chance(id)
        elif command == 'stop':
            confirm = input(colored('Are you sure to stop the game? This will terminate this game. [y/n] : ', 'red')).lower()
            if confirm == 'y':
                pro.commander()
            elif confirm == 'n':
                print(colored("WARNING : Entering 'stop' once more now will terminate game without confirmation!", 'yellow'))
                self.play_terminal(id)
            else:
                print(colored("Sorry Boss,Alice can't understand! ", 'yellow'))
        elif command == 'quit':
            confirm = input(colored('Are you sure to quit the game? [y/n] : ', 'red')).lower()
            if confirm == 'y':
                print(colored("Bye Boss, I will be missing you. Back you soon...", 'green'))
                exit()
            elif confirm == 'n':
                print(colored("WARNING : Entering 'quit' or 'stop' once more now will terminate game without confirmation!", 'yellow'))
                self.play_terminal(id)
        elif command == 'help':
            pro.helper()
        else:
            print(colored("Sorry Boss, Alice can't understand!", 'yellow'))

