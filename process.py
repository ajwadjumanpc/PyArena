import components as cmp
import ladder as ld
import snakes as sk
import story
from termcolor import colored, cprint

players = []


def helper():
    print('''
                        Command List :
                            alice - Alice will tell you the story 
                            start - to set a game
                            play - start playing
                            roll - to roll the dice
                            stop - stop game and back to setup
                            help - to discover the PyArena
                            quit - to quit the game
                            reset - to reset the game 
                        ''')
    sk.snake_list()
    ld.ladder_list()


def game_init():
    number_of_players = int(input(">>> Number of players : "))
    for i in range(number_of_players):
        player = cmp.Player(i,input(f">>> Enter the name of player {i+1} : "),0,'joined game')
        players.append(player)
        print(f' Player {player.name} {player.status} in id {player.id}')


def enter_field(playerid,value):
    if value == 1:
        players[playerid].position = 1
        players[playerid].status = 'started game'
        print(f'Congrats! {players[playerid].name} {players[playerid].status}.')
        print(colored(f'Welcome to Python Arena. Here Pythons rule. Beware of hazardous pythons. Move on...', 'green'))
        print(f'{players[playerid].name}: {players[playerid].position}')
        pass
    else:
        print(colored(f'{players[playerid].name}>Better luck next time. Get ready to get into python arena.', 'red'))
        print(f'{players[playerid].name} : {players[playerid].position}')


def win_check():
    for player in players:
        pos = player.position
        if pos == 100:
            winner = player.name
            print(colored(f"Congrats, {winner} won the game!\n\t!PYTHON MASTER!", 'green'))
            exit()
        else:
            pass


def play(playerid):
    win_check()
    dice = cmp.Dice()
    value = dice.roll()
    nam = players[playerid].name
    print(f" DICE : {value}")
    if players[playerid].position != 0 and (players[playerid].position+value)<=100:
        players[playerid].position += value
        snake_test = sk.snake_check(players[playerid].position)
        players[playerid].position = snake_test
        ladder_test = ld.ladder_check(players[playerid].position)
        players[playerid].position = ladder_test
        print(f"> {nam} : {players[playerid].position}")
        while value == 6:
            return 6
        return 0
    elif (players[playerid].position+value)>100:
        pass
    else:
        enter_field(playerid, value)

try:
    def commander():
        command = ""
        pyarena = cmp.Game('not started',players)
        while command != 'quit':
            command = input(">>>").lower()
            if command == 'help':
                helper()
            elif command == 'start' and pyarena.status != 'started':
                pyarena.status = 'started'
                pyarena.init_game()
            elif command == 'start' and pyarena.status == 'started':
                print(colored("PyArena is already started!", 'red'))
                continue
            elif command == 'play':
                pyarena.play_game()
            elif command == 'alice':
                story.tell()
            elif command == 'quit':
                print(colored("Bye Boss, I will be missing you. Back you soon...", 'green'))
                exit()
            elif command == 'reset':
                cprint("Game settings reset!", 'cyan')
                game_reset()
            else:
                print(colored("Sorry Boss, Alice can't understand!", 'yellow'))
except ValueError:
    cprint("Sorry, Alice can't understand!", 'yellow')
    commander()



def game_starter():
    cprint('''
                        WELCOME TO PyArena
    
    BEWARE OF HAZARDOUS PYTHONS. SEARCH FOR ROPES AND BE THE PYTHON MASTER! 
    
    command 'help' - to help
    ''', 'green', attrs=['bold'])
    commander()


def game_reset():
    cmp.Game.status = 'not started'
    players.clear()
    commander()
