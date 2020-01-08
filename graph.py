import numpy as np
import math


class Graph:
    def __init__(self, n):
        # Create matrix of nxn dimensions (where n is the number of currencies)
        self.matrix = np.zeros((n, n))
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

        # Calculate -log(rate)
        val = -math.log(rate)

        # Add value to matrix
        self.matrix[self.keys[base], self.keys[target]] = val

    def find_negative_weight_cycle(self):
        pass

    def show(self):
        print(self.matrix)
