class TicTacToe:
    list_game = []
    win = ''
    impossible_game = False
    x = 0
    o = 0

    def __init__(self, element='         '):
        self.element = element.replace('_', ' ')
        self.list_game = [self.element[i:i + 3] for i in range(0, len(self.element), 3)]
        self.impossible_game = False
        self.win = ''


    def run(self):
        x1, x2 = '', ''
        for i in range(3):
            col, row, = '', ''

            for j in range(3):
                col += self.list_game[j][i]
                row += self.list_game[i][j]

                if j == i:  # This is position 0,0 1,1 2,2
                    x1 += self.list_game[j][i]

                if (i == 0 and j == 2) or (i == j and i == 1) or (i == 2 and j == 0):
                    x2 += self.list_game[j][i]

            if col == 'XXX' or col == 'OOO':
                if not self.set_win(col):
                    break

            if row == 'XXX' or row == 'OOO':
                if not self.set_win(row):
                    break

        if x1 == 'XXX' or x1 == 'OOO':
            self.set_win(x1)

        if x2 == 'XXX' or x2 == 'OOO':
            self.set_win(x2)

        if self.impossible_game:
            print("Impossible")
        elif self.win != '':
            print(f"{self.win} wins")
            return False

        return True
    def to_play(self):
        self.display()
        turn_x = True

        while True:
            if self.is_draw():
                print("Draw")
                break

            coordinate = input()

            if len(coordinate) != 3 or coordinate[1] != ' ':
                print("You should enter numbers!")
                continue

            n1, n2 = int(coordinate[0]) - 1, int(coordinate[-1]) - 1

            try:
                cell = self.list_game[n1][n2]

                if cell not in ['X', 'O']:
                    nl = list(self.list_game[n1])
                    nl[n2] = 'X' if turn_x else 'O'

                    turn_x = False if turn_x else True
                    self.list_game[n1] = ''.join(nl)
                    self.display()

                    if not self.run():
                        break
                else:
                    print("This cell is occupied! Choose another one!")
                    continue
            except ValueError:
                print("You should enter numbers!")
                continue
            except IndexError:
                print("Coordinates should be from 1 to 3!")
                continue

    def is_draw(self):
        x = [x for l in self.list_game for x in l if x == 'X']
        o = [x for l in self.list_game for x in l if x == 'O']
        if len(x) + len(o) == 9:
            return True

        return False

    def display(self):
        print("--------")
        print('|', *self.list_game[0], '|', sep=' ')
        print('|', *self.list_game[1], '|', sep=' ')
        print('|', *self.list_game[2], '|', sep=' ')
        print("--------")

    def set_win(self, pattern):
        if self.win != '' and self.win != pattern[0]:
            self.impossible_game = True
            return False
        else:
            self.win = pattern[0]
            return True

game = TicTacToe()
game.to_play()
