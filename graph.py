import numpy as np


class Graph:
    def __init__(self):
        self.matrix = np.matrix([[]])
        self.keys = {}
        self.curr_index = 0

    def add(self, key):
        self.keys[key] = self.curr_index
        self.curr_index += 1

        # np.vstack self.matrix

    # def add_weight():
