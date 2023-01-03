# TODO здесь писать код
class Cells:
    """Пустые клетки"""
    cells = {
        7: ' ', 8: ' ', 9: ' ',
        4: ' ', 5: ' ', 6: ' ',
        1: ' ', 2: ' ', 3: ' '
    }

    """Выигрышные комбинации"""
    movies = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9],
        [1, 5, 9],
        [3, 5, 7]
    ]


class Board:
    def board(self=None):
        print("\n")
        print("\t     |     |")
        print("\t  {}  |  {}  |  {}".format(Cells.cells[7], Cells.cells[8], Cells.cells[9]))
        print('\t_____|_____|_____')

        print("\t     |     |")
        print("\t  {}  |  {}  |  {}".format(Cells.cells[4], Cells.cells[5], Cells.cells[6]))
        print('\t_____|_____|_____')

        print("\t     |     |")
        print("\t  {}  |  {}  |  {}".format(Cells.cells[1], Cells.cells[2], Cells.cells[3]))
        print("\t     |     |")
        print("\n")


class Player:
    name = ''
    dice = ''

    def print(self):
        print('Имя: {}\n'
              'Фишка: {}\n'.format(self.name, self.dice))

    def __str__(self):
        return f'{self.name}'


class Game:
    def game(self, name, dice):
        Board.board()
        try:
            position = int(input(f'Ход {name} куда ставить фишку "{dice}": '))

            if Cells.cells[position] != ' ':
                print('Клетка занята. Выберите другую клетку.')
                return Game.game(self, name, dice)

            Cells.cells[position] = dice

        except KeyError:
            print('Не правильный номер клетки. Попробуйте еще раз.')
            return Game.game(self, name, dice)

    """Проверка на выигрыш"""

    def winner(self=None):
        win = ''
        for i in Cells.movies:
            if Cells.cells[i[0]] == 'X' and Cells.cells[i[1]] == 'X' and Cells.cells[i[2]] == 'X':
                win = 'X'
            if Cells.cells[i[0]] == '0' and Cells.cells[i[1]] == '0' and Cells.cells[i[2]] == '0':
                win = '0'

        return win

    """Проверка на ничью"""

    def free_cells(self=None):
        count = 0
        for key in Cells.cells:
            if Cells.cells[key] == ' ':
                count += 1
        if count == 0:
            Board.board()
            print('Игра закончилась ничьей.')
            raise SystemExit


player_1 = Player()
player_1.name = 'Игрок-1'
player_1.dice = 'X'
player_2 = Player()
player_2.name = 'Игрок-2'
player_2.dice = '0'

player_1.print()
player_2.print()
players = player_1, player_2

while True:
    for player in players:
        Game.game('', player.name, player.dice)
        Game.winner()
        if Game.winner():
            Board.board()
            print(f'Победитель {player}')
            raise SystemExit
        Game.free_cells()
