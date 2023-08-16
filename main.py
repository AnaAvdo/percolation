import argparse
from percolation import Percolation
from show import Show
from stats import Stats

def main():
    parser = argparse.ArgumentParser(description='Percolation model')

    parser.add_argument('-a', '--animate', action='store_true', help='Show process of opening sites until percolates (Monte Carlo)')
    parser.add_argument('-e', '--experiment', action='store_true', help='Conduct an experiment to determine statistics about number of open sites when system percolates. Default number of trials is 30')
    parser.add_argument('-g', '--grid_size', type=int, help='How many rows and columns should be in the system')
    parser.add_argument('-t', '--trials', type=int, help='Number of trials', default=30)

    args = parser.parse_args()

    if args.grid_size <=0:
        raise argparse.ArgumentError("Argument for the grid size should be greater than 0. Entered argument: " + str(args.grid_size))

    if args.animate:
        perc = Show(args.grid_size)
        perc.show()
    
    if args.experiment:
        stats = Stats(args.grid_size, args.trials)
        print(stats)

if __name__ == '__main__':
    main()