import os


class colors:
    '''Colors class:
    Reset all colors with colors.reset
    Two subclasses fg for foreground and bg for background.
    Use as colors.subclass.colorname.
    i.e. colors.fg.red or colors.bg.green
    Also, the generic bold, disable, underline, reverse, strikethrough,
    and invisible work with the main class
    i.e. colors.bold
    '''
    reset = '\033[0m'
    bold = '\033[01m'
    disable = '\033[02m'
    underline = '\033[04m'
    reverse = '\033[07m'
    strikethrough = '\033[09m'
    invisible = '\033[08m'

    class fg:
        black = '\033[30m'
        red = '\033[31m'
        green = '\033[32m'
        orange = '\033[33m'
        blue = '\033[34m'
        purple = '\033[35m'
        cyan = '\033[36m'
        lightgrey = '\033[37m'
        darkgrey = '\033[90m'
        lightred = '\033[91m'
        lightgreen = '\033[92m'
        yellow = '\033[93m'
        lightblue = '\033[94m'
        pink = '\033[95m'
        lightcyan = '\033[96m'

    class bg:
        black = '\033[40m'
        red = '\033[41m'
        green = '\033[42m'
        orange = '\033[43m'
        blue = '\033[44m'
        purple = '\033[45m'
        cyan = '\033[46m'
        lightgrey = '\033[47m'

symbol_X = colors.fg.red+'X'+colors.reset
symbol_0 = colors.fg.lightblue+'0'+colors.reset
board = list(range(1, 10))
console_height = 120

def interfaceBoard():
    os.system('cls')
    print(((colors.reverse + " " + colors.reset) * console_height))
    print((symbol_X + " " + symbol_0 + " ") * int(console_height/4))
    print((" " + symbol_0 + " " + symbol_X) * int(console_height/4))
    print((symbol_X + " " + symbol_0 + " ") * int(console_height/4))
    print(((colors.reverse + " " + colors.reset) * console_height))


def playingField(board):
    interfaceBoard()
    print(f'\n{"-" * 13}')
    for i in range(3):
        print(f'| {colors.fg.darkgrey}{board[0 + i * 3]}{colors.reset} '
              f'| {colors.fg.darkgrey}{board[1 + i * 3]}{colors.reset} '
              f'| {colors.fg.darkgrey}{board[2 + i * 3]}{colors.reset} '
              f'|')
        print("-" * 13)


def stepUser(player_token):
    valid = False
    while not valid:
        player_answer = input(f'🔢 Введите номер клетки для установки "{player_token}": ')
        try:
            player_answer = int(player_answer)
        except:
            print(f'{colors.fg.red}Ой! 🤦 Вы уверены, что ввели число?{colors.reset}')
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(board[player_answer - 1]) not in (symbol_X,symbol_0)):
                board[player_answer - 1] = player_token
                valid = True
            else:
                print(f'{colors.fg.red}Ой! 🤦 Клетка занята, выберите другую!{colors.reset}')
        else:
            print(f'{colors.fg.red}Ой! 🤦 Эта клетка недоступна. Введите число от 1 до 9.{colors.reset}')


def checkWinner(board):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

count = 0
winner = False
while not winner:
    playingField(board)
    if count % 2 == 0:
        stepUser(symbol_X)
    else:
        stepUser(symbol_0)
    count += 1
    if count > 4:
        player = checkWinner(board)
        if player:
            playingField(board)
            print(f'\nПобедили "{player*3}"! 🏆🏆🏆')
            winner = True
            break
    if count == 9:
        playingField(board)
        print("🤷 Ничья!")
        print((symbol_X + " " + symbol_0 + " ") * 3)
        break



input('\n\n\nНажмите "Enter ⏎" для выхода!')