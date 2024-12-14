import sys

import numpy as np

def circle_area(radius):
    return radius*radius*np.pi

if __name__ == '__main__':
    print(circle_area(float(sys.argv[1])))