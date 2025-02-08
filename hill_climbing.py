import random as rand
import time

import numpy as np
import scipy

from move import Move


class NQPosition:

    def __init__(self, n: int):
        self.n = n
        self.state = rand.sample(range(self.n), self.n)

    def hill_climbing(self):
        current_value = self.get_conflicts()
        while True:
            move, new_value = self.algorithm()
            if current_value == 0.0:
                print(self.state)
                return current_value
            if new_value >= current_value:
                # no improvement, give up
                self.state = rand.sample(range(self.n), self.n)
                current_value = self.get_conflicts()
                continue
            else:
                # position improves, keep searching
                current_value = new_value
                self.make_move(move)

    def get_conflicts(self):
        """ Calculate the number of conflicts (queens that can capture each other) """

        # Rows conflicts
        same_rows = np.zeros(self.n)
        for row in self.state:
            same_rows[row] += 1

        # Diagonal conflicts
        dia1_conf = scipy.special.binom((self.n - len(set(self.state + np.arange(self.n))) + 1), 2)
        dia2_conf = scipy.special.binom((self.n - len(set(self.state - np.arange(self.n))) + 1), 2)

        # Total conflicts
        conflicts = dia1_conf + dia2_conf + sum(scipy.special.binom(same_rows, 2))
        return conflicts

    def make_move(self, move: Move):
        self.state[move.get_col()] = move.get_new_row()

    def print_solution(self):
        """ Creates solution table """
        print(" " + "---" * self.n + " ")
        for el in self.state:
            print("|" + " * " * el + " Q " + " * " * (self.n - el - 1) + "|")
        print(" " + "---" * self.n + " ")

    def algorithm(self):
        raise NotImplementedError


class NQPositionUpAndDown(NQPosition):

    def algorithm(self):
        value = self.get_conflicts()
        move = None
        for i in self.state:
            if self.state[i] + 1 < self.n:
                self.state[i] += 1
                new_row = self.state[i]
                value2 = self.get_conflicts()
                if value2 < value:
                    value = value2
                    move = Move(i, new_row)
                self.state[i] -= 1
            if self.state[i] - 1 >= 0:
                self.state[i] -= 1
                new_row = self.state[i]
                value2 = self.get_conflicts()
                if value2 < value:
                    value = value2
                    move = Move(i, new_row)
                self.state[i] += 1
        return move, value


class NQPositionAllTable(NQPosition):

    def algorithm(self):
        value = self.get_conflicts()
        move = None
        for x in range(self.n):
            initial = self.state[x]
            for y in range(self.n):
                self.state[x] = y
                if self.get_conflicts() < value:
                    value = self.get_conflicts()
                    move = Move(x, y)
            self.state[x] = initial
        return move, value


if __name__ == '__main__':
    # NQPositionUpAndDown
    start_time = time.time()
    pos_up_and_down = NQPositionUpAndDown(12)
    pos_up_and_down.hill_climbing()
    pos_up_and_down.print_solution()
    print("--- %s seconds ---" % (time.time() - start_time))

    # NQPositionAllTable
    start_time = time.time()
    pos_all_table = NQPositionAllTable(10)
    pos_all_table.hill_climbing()
    pos_all_table.print_solution()
    print("--- %s seconds ---" % (time.time() - start_time))
