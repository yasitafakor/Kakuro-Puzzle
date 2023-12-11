class Kakuro:
    def __init__(self):
        self.board = [
            ['#', 'c1', 'c3'],
            ['c2', 0, 0],
            ['c4', 0, 0]
        ]

        self.constraints = {
            1: {'down': 11},
            2: {'right': 8},
            3: {'down': 3},
            4: {'right': 6}
        }

        self.constraints_directions = {
            1: {'down'},
            2: {'right'},
            3: {'down'},
            4: {'right'}
        }

        self.constraints_target = {
            1: {11},
            2: {8},
            3: {3},
            4: {6}
        }

        self.constraints_location = {
            1: [0, 1],
            2: [1, 0],
            3: [0, 2],
            4: [2, 0]
        }

        self.constraints_list = [1, 2, 3, 4]

        self.domains = {
            'a11': [1, 2, 3, 4, 5, 6, 7, 8, 9],
            'a12': [1, 2, 3, 4, 5, 6, 7, 8, 9],
            'a21': [1, 2, 3, 4, 5, 6, 7, 8, 9],
            'a22': [1, 2, 3, 4, 5, 6, 7, 8, 9]
        }

        self.column = 3
        self.row = 3

    def print_board(self):
        for i in range(0, 3):
            for j in range(0, 3):
                print(self.board[i][j], end=" ")
            print()
        print()

    def test(self):
        t = self.constraints_list.pop(0)
        print(self.domains.get('a11'))
        n = 4
        print(self.domains.get('a11').remove(n))
        print(self.domains.get('a11'))
        print(a+1)

    def get_domain(self, i, j):
        if i == 1 and j == 1:
            return self.domains.get('a11')
        elif i == 1 and j == 2:
            return self.domains.get('a12')
        elif i == 2 and j == 1:
            return self.domains.get('a21')
        elif i == 2 and j == 2:
            return self.domains.get('a22')

    def get_constraint(self, row, col):
        if row == 0 and col == 1:
            return 1
        if row == 1 and col == 0:
            return 2
        if row == 0 and col == 2:
            return 3
        if row == 2 and col == 0:
            return 4

    def update_domain(self, domain, num, i, j):

    def solve_kakuro(self, row, col, temp_domain, temp_list):

        temp_constraint = self.get_constraint(row, col)

        copy_list = self.constraints_list.copy()

        if self.constraints_directions.get(temp_constraint).pop() == 'down':
            j = self.constraints_location.get(temp_constraint).pop()
            i = self.constraints_location.get(temp_constraint).pop(0) + 1

            for num in self.get_domain(i, j):
                if self.board[i][j] != 0:
                    self.board[i][j] = num
                    copy_domain = self.domains.copy()
                    self.update_domain(copy_domain, num, i, j)
                    if solve_kakuro(row+1, col, copy_domain, copy_list):
                        return True

        elif self.constraints_directions.get(temp_constraint).pop() == 'right':
            j = self.constraints_location.get(temp_constraint).pop()
            i = self.constraints_location.get(temp_constraint).pop(0) + 1

            for num in self.get_domain(i, j):
                if self.board[i][j] != 0:
                    self.board[i][j] = num
                    copy_domain = self.domains.copy()
                    self.update_domain(copy_domain, num, i, j)
                    if solve_kakuro(row+1, col, copy_domain, copy_list):
                        return True




k = Kakuro()
k.print_board()
