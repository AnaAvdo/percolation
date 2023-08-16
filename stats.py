from percolation import Percolation
import numpy as np

class Stats:
    # perform independent trials on an n-by-n grid
    def __init__(self, n, trials):
        self.trials = trials
        self.fractions = []
        for i in range(trials):
            perc = Percolation(n)
            while not perc.percolates():
                rand_row = np.random.randint(n)
                rand_col = np.random.randint(n)
                perc.open(rand_row, rand_col)
            opened = perc.num_open_sites()
            self.fractions.append(opened/(n*n))

        self.mean = np.mean(self.fractions)
        self.std = np.std(self.fractions)
        self.conf_l = self.mean - (1.96*self.std)/np.sqrt(self.trials)
        self.conf_h = self.mean + (1.96*self.std)/np.sqrt(self.trials)

    def __str__(self):
        return f"mean                    = {self.mean} \nstddev                  = {self.std}\n95% confidence interval = [{self.conf_l}, {self.conf_h}]"
    

    