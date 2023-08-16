import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import animation
from weightedqu import WeightedQU

class Percolation():
    def __init__(self, n):
        # creates n-by-n grid, with all sites initially blocked
        self.n = n
        self.system = [[0 for i in range(n)] for i in range(n)]
   
        self.qu_object = WeightedQU(self.n**2+2)
        # connect all bottom /all top elements to additional sites
        for i in range(n):
            # top additional site value = n*n
            self.qu_object.union(i, self.n**2)
            # bottom additional site value = n*n+1
            self.qu_object.union(i+n*(n-1), self.n**2+1)
        
        self.open_sites = 0
    
    def grid_to_array(self, row, col):
        # For given row and column in the system returns the index of this site in connections array for qu_object
        return row*self.n + col

    def open(self, row, col):
        # opens the site (row, col) if it is not open already (given row and col is in [0,n))
        elem = self.grid_to_array(row, col)
        if self.system[row][col] == 0:
            self.system[row][col] = 1
            self.open_sites += 1

            # If there are open neighbours (4 elements), connect to them
            if row-1 >= 0 and self.is_open(row-1, col):
                self.qu_object.union(elem-self.n, elem)
            if row+1 < self.n and self.is_open(row+1, col):
                self.qu_object.union(elem+self.n, elem)
            if col-1 >= 0 and self.is_open(row, col-1):
                self.qu_object.union(elem-1, elem)
            if col+1 < self.n and self.is_open(row, col+1):
                self.qu_object.union(elem+1, elem)

    def is_open(self, row, col):
        # is the site of given coordinates open
        return self.system[row][col] == 1

    def is_full(self, row, col):
        # checks if site is full ~is  an open site that can be connected to an open site in the top row via a chain of neighboring (left, right, up, down) open sites)
        if self.is_open(row, col):
            id = self.grid_to_array(row, col)
            return self.qu_object.is_connected(self.n**2, id)
        return False

    def num_open_sites(self):
        # returns the number of open sites
        return self.open_sites
    
    def percolates(self):
        # does the system percolate ~ are top and bottom additional sites connected
        return self.qu_object.is_connected(self.n**2, self.n**2+1)
    