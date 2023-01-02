# TODO здесь писать код
class Cells:
    board = {
        7: ' ', 8: ' ', 9: ' ',
        4: ' ', 5: ' ', 6: ' ',
        1: ' ', 2: ' ', 3: ' '
    }

    def print(self=None):
        print("\n")
        print("\t     |     |")
        print("\t  {}  |  {}  |  {}".format(Cells.board[7], Cells.board[8], Cells.board[9]))
        print('\t_____|_____|_____')

        print("\t     |     |")
        print("\t  {}  |  {}  |  {}".format(Cells.board[4], Cells.board[5], Cells.board[6]))
        print('\t_____|_____|_____')

        print("\t     |     |")
        print("\t  {}  |  {}  |  {}".format(Cells.board[1], Cells.board[2], Cells.board[3]))
        print("\t     |     |")
        print("\n")


def game(i):
    Cells.print()
    try:
        a = int(input(f'Ход {i} куда ставить: '))

        if Cells.board[a] != ' ':
            print('Клетка занята. Выберите другую клетку.')
            return game(i)

        Cells.board[a] = i
    except KeyError:
        print('Не правильный номер клетки. Попробуйте еще раз.')
        return game(i)

while True:
    for i in ('X', '0'):
        game(i)
