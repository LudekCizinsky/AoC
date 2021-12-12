from util import load_data
import numpy as np


def main():

    ls, ps, x_max, y_max = load_data()
    t = np.zeros((x_max + 1, y_max + 1))

    for l in ls:
        p1, p2 = l
        x1, y1 = p1
        x2, y2 = p2
        t[x1:x2 + 1, y1:y2 + 1] += 1
    r = len(np.where(t > 1)[0])
    print(r)
    
    for p in ps:
        x, y = p
        t[x, y] += 1

    r = len(np.where(t > 1)[0])
    print(r)


if __name__ == '__main__':
    main()