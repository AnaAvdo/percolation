import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import animation
from percolation import Percolation

class Show:
    def __init__(self, n, figsize = 5.5):
        self.perc = Percolation(n)
        self.n = n
        self.figsize = figsize
        self.col = 'mako'

    def show(self):
        # Show an animation of sites opens until system percolates
        plt.rcParams["figure.figsize"] = [self.figsize, self.figsize]
        plt.rcParams["figure.autolayout"] = True
        fig = plt.figure()
        def animate(i):
            if not self.perc.percolates():
                rand_row = np.random.randint(self.n)
                rand_col = np.random.randint(self.n)
                self.perc.open(rand_row, rand_col)
            else: 
                self.col = 'rocket'
            sns.heatmap(self.perc.system, vmax=1, cbar=False, cmap=self.col)
        anim = animation.FuncAnimation(fig, animate, frames = self.n**3, repeat=False)
        plt.show()