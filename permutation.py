import time
from itertools import permutations


class NQueensPermutation:

    def __init__(self, n: int):
        self.n = n
        self.columns = range(self.n)

    def n_queen_permutation(self):
        # Permutations are like (1,2,3,4) where value means column and index means row
        permutation_values = permutations(self.columns)

        for combination in permutation_values:
            nw_se_diagonal = set()
            ne_sw_diagonal = set()
            for i in self.columns:
                # This can check every possible diagonals
                nw_se_diagonal.add(combination[i] - i)
                ne_sw_diagonal.add(combination[i] + i)

            # Diagonals have only one queen
            if self.n == len(nw_se_diagonal) == len(ne_sw_diagonal):
                self.print_combination(combination)
                break

    def print_combination(self, combination: tuple):
        """ Creates solution table """
        print(" " + "---" * self.n + " ")
        for el in combination:
            print("|" + " * " * el + " Q " + " * " * (self.n - el - 1) + "|")
        print(" " + "---" * self.n + " ")


if __name__ == '__main__':
    n = 4
    solution = NQueensPermutation(n)
    start_time = time.time()
    solution.n_queen_permutation()
    print("--- %s seconds ---" % (time.time() - start_time))
