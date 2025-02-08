import time


class BitwiseSolver:

    def __init__(self, n: int):
        self.n = n
        self.cols = 0
        self.diagonals1 = 0
        self.diagonals2 = 0
        self.state = []

    def solve_n_queens(self):
        self.state = self.backtrack(0, 0, 0, 0, [])
        return self.state

    def print_solution(self):
        """ Creates solution table """
        print(" " + "---" * self.n + " ")
        for el in self.state:
            print("|" + " * " * el + " Q " + " * " * (self.n - el - 1) + "|")
        print(" " + "---" * self.n + " ")

    def backtrack(self, row, cols, diagonals1, diagonals2, board):
        if row == self.n:
            return board

        available_positions = ((1 << self.n) - 1) & ~(cols | diagonals1 | diagonals2)
        while available_positions:
            position = available_positions & -available_positions
            available_positions &= available_positions - 1
            col = bin(position - 1).count("1")

            board.append(col)
            result = self.backtrack(row + 1, cols | position,
                                    (diagonals1 | position) << 1,
                                    (diagonals2 | position) >> 1,
                                    board)
            if result:
                return result
            board.pop()

        return None


if __name__ == '__main__':
    n = 30
    bitwise_solver = BitwiseSolver(n)
    start_time = time.time()
    solution = bitwise_solver.solve_n_queens()
    print("--- %s seconds ---" % (time.time() - start_time))
    # bitwise_solver.print_solution()
