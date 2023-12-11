class Kakuro:
    def __init__(self):
        self.board = [
            ['#', 'c1', 'c3', '#', '#'],
            ['c2', 0, 0, 'c5', '#'],
            ['c4', 0, 0, 0, 'c7'],
            ['#', 'c6', 0, 0, 0],
            ['#', '#', 'c8', 0, 0]
        ]

        self.constraints = {
            'c1': {'down': 3},
            'c2': {'right': 6},
            'c3': {'down': 18},
            'c4': {'right': 7},
            'c5': {'down': 9},
            'c6': {'right': 17},
            'c7': {'down': 3},
            'c8': {'right': 3}
        }

        self.row = 5
        self.column = 5

    def check_valid(self):

        check_c1 = 0
        for i in range(1, 3):
            check_c1 += self.board[i][1]

        check_c2 = 0
        for j in range(1, 3):
            check_c2 += self.board[1][j]

        check_c3 = 0
        for i in range(1, 4):
            check_c3 += self.board[i][2]

        check_c4 = 0
        for j in range(1, 4):
            check_c4 += self.board[2][j]

        check_c5 = 0
        for i in range(2, 5):
            check_c5 += self.board[i][3]

        check_c6 = 0
        for j in range(2, 5):
            check_c6 += self.board[3][j]

        check_c7 = 0
        for i in range(3, 5):
            check_c7 += self.board[i][4]

        check_c8 = 0
        for j in range(3, 5):
            check_c8 += self.board[4][j]

        if ((check_c1 == self.constraints.get('c1').get('down')) and
                (check_c2 == self.constraints.get('c2').get('right')) and
                (check_c3 == self.constraints.get('c3').get('down')) and
                (check_c4 == self.constraints.get('c4').get('right')) and
                (check_c5 == self.constraints.get('c5').get('down')) and
                (check_c6 == self.constraints.get('c6').get('right')) and
                (check_c7 == self.constraints.get('c7').get('down')) and
                (check_c8 == self.constraints.get('c8').get('right'))):
            return True
        else:
            return False

    def print_board(self):
        for i in range(0, 5):
            for j in range(0, 5):
                print(self.board[i][j], end=" ")
            print()
        print()

    def is_valid(self, row, col, num):
        for i in range(0, 5):
            if self.board[i][col] == num:
                return False
        for j in range(0, 5):
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
k.solve_kakuro_backtrack(1, 1)
k.print_board()
