class Kakuro:
    def __init__(self):
        self.board = [
            ['#', 'c1', 'c3'],
            ['c2', 0, 0],
            ['c4', 0, 0]
        ]

        self.constraints = {
            'c1': {'down': 11},
            'c2': {'right': 8},
            'c3': {'down': 3},
            'c4': {'right': 6}
        }

        self.column = 3
        self.row = 3

    def check_valid(self):

        check_c1 = 0
        for i in range(1, 3):
            check_c1 += self.board[i][1]

        check_c2 = 0
        for j in range(1, 3):
            check_c2 += self.board[1][j]

        check_c3 = 0
        for i in range(1, 3):
            check_c3 += self.board[i][2]

        check_c4 = 0
        for j in range(1, 3):
            check_c4 += self.board[2][j]

        if ((check_c1 == self.constraints.get('c1').get('down')) and
                (check_c2 == self.constraints.get('c2').get('right')) and
                (check_c3 == self.constraints.get('c3').get('down')) and
                (check_c4 == self.constraints.get('c4').get('right'))):
            return True
        else:
            return False

    def print_board(self):
        for i in range(0, 3):
            for j in range(0, 3):
                print(self.board[i][j], end=" ")
            print()
        print()

    def is_valid(self, row, col, num):
        for i in range(0, 3):
            if self.board[i][col] == num:
                return False
        for j in range(0, 3):
            if self.board[row][j] == num:
                return False

        return True

    def is_row_valid(self, row):
        if (row == 1 and self.board[row][1]+self.board[row][2] == 8) or (row == 2 and self.board[row][1]+self.board[row][2] == 6):
            return True
        else:
            return False

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
