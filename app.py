import process as pro
from termcolor import cprint

try:
    pro.game_starter()
except ValueError:
    cprint("Sorry, Alice can't understand!", 'yellow')
    pro.commander()
except OverflowError:
    cprint("Sorry Error Occured. Alice will restart PyArena Now!", 'yellow')
    pro.game_starter()
