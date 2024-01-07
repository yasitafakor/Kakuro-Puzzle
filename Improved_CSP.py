class Kakuro:
    def __init__(self):
        self.board = [
            ['#', 'c1', 'c3'],
            ['c2', 0, 0],
            ['c4', 0, 0]
        ]
​
        self.constraints = {
            'c1': {'down': 11},
            'c2': {'right': 8},
            'c3': {'down': 3},
            'c4': {'right': 6}
        }
​
        self.constraints_location = {
            'c1': [0, 1],
            'c2': [1, 0],
            'c3': [0, 2],
            'c4': [2, 0]
        }
​
        self.constraints_list = ['c1', 'c2', 'c3', 'c4']
​
        self.domains = {
            'c1': [1, 2, 3, 4, 5, 6, 7, 8, 9],
            'c2': [1, 2, 3, 4, 5, 6, 7, 8, 9],
            'c3': [1, 2, 3, 4, 5, 6, 7, 8, 9],
            'c4': [1, 2, 3, 4, 5, 6, 7, 8, 9]
        }
​
        self.column = 3
        self.row = 3
​
    def print_board(self):
        for i in range(0, 3):
            for j in range(0, 3):
                print(self.board[i][j], end=" ")
            print()
        print()
​
    def update_domain(self, num, constraint_name):
        if num in self.domains.get(constraint_name):
            self.domains.get(constraint_name).remove(num)
​
    def solve(self, row, col, constraints, domain, constraint_name=None, direction=None, number=None, smm=0):
​
        if len(self.constraints_list) == 0:
            return True
​
        if row == -1 and col == -1:
            constraint_name = self.constraints_list.pop(0)
            direction = list(self.constraints.get(constraint_name).keys())[0]
            row, col = self.constraints_location.get(constraint_name)
            if direction == 'down':
                row += 1
            else:
                col += 1
            
            domain = self.domains.get(constraint_name)
            if self.solve(row, col, constraints, domain, constraint_name, direction, number):
                return True
​
            return False
​
        if direction == 'down':
            if row == len(self.board) or self.board[row][col] == '#' or self.board[row][col] in self.constraints:
                # send to next constraint
                if smm != self.constraints.get(constraint_name).get(direction):
                    return False
                return self.solve(-1, -1, constraints, domain, constraint_name, direction, number)
​
            if self.board[row][col] != 0:
                # it has been filled before
                return self.solve(row + 1, col, self.board, constraints, domain, constraint_name, direction)
​
            elif self.board[row][col] == 0:
                for i in domain:
                    self.board[row][col] = i
                    # self.print_board()
                    self.update_domain(i, constraint_name)
                    if self.solve(row + 1, col, constraints, domain, constraint_name, direction, i, smm + i):
                        return True
                return False
​
        if direction == 'right':
            if col == len(self.board) or self.board[row][col] == '#' or self.board[row][col] in self.constraints:
                if smm != self.constraints.get(constraint_name).get(direction):
                    return False
                # send to next constraint
                return self.solve(-1, -1, constraints, domain, constraint_name, direction, number)
​
            if self.board[row][col] != 0:
                # it has been filled before
                return self.solve(row, col + 1, self.board, constraints, domain, constraint_name, direction)
​
            elif self.board[row][col] == 0:
                for i in domain:
                    self.board[row][col] = i
                    # self.print_board()
                    self.update_domain(i, constraint_name)
                    if self.solve(row, col + 1, constraints, domain, constraint_name, direction, i, smm + i):
                        return True
                return False
​
​
k = Kakuro()
k.solve(-1, -1, k.constraints, k.domains)
k.print_board()
