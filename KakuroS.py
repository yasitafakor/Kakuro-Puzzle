class Kakuro:
    def __init__(self):
        self.board = [
            ['#', '#', '#', 'c1', 'c2', '#', '#'],
            ['#', '#', 'c3', 0, 0, 'c4', 'c5'],
            ['#', 'c6', 0, 0, 0, 0, 0],
            ['c7', 0, 0, 'c8', 0, 0, 0],
            ['c9', 0, 0, 0, 0, 0, 'c10'],
            ['#', 'c11', 0, 0, 0, 0, 0],
            ['#', 'c12', 0, 0, 'c13', 0, 0]
        ]

        self.constraints = {
            'c1': {'down': 17},
            'c2': {'down': 28},
            'c3': {'down': 27, 'right': 16},
            'c4': {'down': 17},
            'c5': {'down': 17},
            'c6': {'down': 11, 'right': 27},
            'c7': {'right': 3},
            'c8': {'right': 19, 'down': 14},
            'c9': {'right': 34},
            'c10': {'down': 17},
            'c11': {'right': 30},
            'c12': {'right': 3},
            'c13': {'right': 16}
        }

        self.row = 5
        self.column = 5

    def check_valid(self):

        check_c1 = 0
        for i in range(1, 3):
            check_c1 += self.board[i][3]

        check_c2 = 0
        for i in range(1, 6):
            check_c2 += self.board[i][4]

        check_c3_right = 0
        for j in range(3, 5):
            check_c3_right += self.board[1][j]

        check_c3_down = 0
        for i in range(2, 7):
            check_c3_down += self.board[i][2]

        check_c4 = 0
        for i in range(2, 7):
            check_c4 += self.board[i][5]

        check_c5 = 0
        for i in range(2, 4):
            check_c5 += self.board[i][6]

        check_c6_right = 0
        for j in range(2, 7):
            check_c6_right += self.board[2][j]

        check_c6_down = 0
        for i in range(3, 5):
            check_c6_down += self.board[i][1]

        check_c7 = 0
        for j in range(1, 3):
            check_c7 += self.board[3][j]

        check_c8_right = 0
        for j in range(4, 7):
            check_c8_right += self.board[3][j]

        check_c8_down = 0
        for i in range(4, 7):
            check_c8_down += self.board[i][3]

        check_c9 = 0
        for j in range(1, 6):
            check_c9 += self.board[4][j]

        check_c10 = 0
        for i in range(5, 7):
            check_c10 += self.board[i][6]

        check_c11 = 0
        for j in range(2, 7):
            check_c11 += self.board[5][j]

        check_c12 = 0
        for j in range(2, 4):
            check_c12 += self.board[6][j]

        check_c13 = 0
        for j in range(5, 7):
            check_c13 += self.board[6][j]

        if ((check_c1 == self.constraints.get('c1').get('down')) and
                (check_c2 == self.constraints.get('c2').get('down')) and
                (check_c3_right == self.constraints.get('c3').get('right')) and
                (check_c3_down == self.constraints.get('c3').get('down')) and
                (check_c4 == self.constraints.get('c4').get('down')) and
                (check_c5 == self.constraints.get('c5').get('down')) and
                (check_c6_right == self.constraints.get('c6').get('right')) and
                (check_c6_down == self.constraints.get('c6').get('down')) and
                (check_c7 == self.constraints.get('c7').get('right')) and
                (check_c8_right == self.constraints.get('c8').get('right')) and
                (check_c8_down == self.constraints.get('c8').get('down')) and
                (check_c9 == self.constraints.get('c9').get('right')) and
                (check_c10 == self.constraints.get('c10').get('down')) and
                (check_c11 == self.constraints.get('c11').get('right')) and
                (check_c12 == self.constraints.get('c12').get('right')) and
                (check_c13 == self.constraints.get('c13').get('right'))):
            return True
        else:
            return False

    def print_board(self):
        for i in range(0, 7):
            for j in range(0, 7):
                print(self.board[i][j], end=" ")
            print()
        print()

    def is_valid(self, row, col, num):
        for i in range(0, 7):
            if self.board[i][col] == num:
                return False
        for j in range(0, 7):
            if self.board[row][j] == num:
                return False

        return True

    def solve_kakuro_backtrack(self, row, col):

        if col == self.column:
            col = 0
            row += 1
            if row == self.row:
                return True

        if self.board[row][col] != 0:
            return self.solve_kakuro_backtrack(row, col + 1)

        for num in range(1, 10):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.solve_kakuro_backtrack(row, col + 1) and self.check_valid():
                    return True
                self.board[row][col] = 0
        return False


k = Kakuro()
k.print_board()
k.solve_kakuro_backtrack(1, 3)
k.print_board()
