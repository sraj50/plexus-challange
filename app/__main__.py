from .Glass import Glass
from .Overflow import visualise, find_glass
import argparse



def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--row", default=0, type=int,
                        help="Number of rows")
    parser.add_argument("-j", "--col", default=0, type=int,
                        help="Number of columns")
    parser.add_argument("-k", "--water", default=0, type=float,
                        help="Amount of liquid in litres to pour into to glass")
    parser.add_argument("-v", "--visualise", action="store_true",
                        help="Show visualisation of tree")
    return parser.parse_args()


args = get_args()
i = args.row
j = args.col
k = args.water
is_visualise = args.visualise

if __name__ == '__main__':
    if is_visualise:
        g = Glass()
        g.fill(k)
        visualise(g)

    y = find_glass(i, j, k)
