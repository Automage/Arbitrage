import numpy as np


class Graph:
    def __init__(self, n):
        # Create matrix of nxn dimensions (where n is the number of currencies)
        self.matrix = np.empty((n, n))
        self.keys = {}
        self.index = 0

    def add_edge(self, base, target, rate):
        # Add index of tickers to dict, if not already
        if not (base in self.keys):
            self.keys[base] = self.index
            self.index += 1

        if not (target in self.keys):
            self.keys[target] = self.index
            self.index += 1

        # Add rate to matrix
        self.matrix[self.keys[base], self.keys[target]] = rate

    def find_negative_weight_cycle(self):
        pass

    def show(self):
        print(self.matrix)
