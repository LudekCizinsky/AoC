import sys


def load_data():

    which = sys.argv[1]

    with open(f"{which}.in") as f:
        o = f.readlines()

    x_max = 0
    y_max = 0

    ls = []
    ps = []
    
    for line in o:
        c = line.strip('\n').split(' -> ')
        x1, y1 = [int(val) for val in c[0].split(',')]
        x2, y2 = [int(val) for val in c[1].split(',')]

        if max(x1, x2) > x_max:
            x_max = max(x1, x2)

        if max(y1, y2) > y_max:
            y_max = max(y1, y2)

        if (x1 == x2 and y1 > y2) or (y1 == y2 and x1 > x2):
            ls.append([(x2, y2), (x1, y1)])
        elif (x1 == x2) or (y1 == y2):
            ls.append([(x1, y1), (x2, y2)])
        else:
            if x1 > x2:
                x1, x2 = x2, x1
                y1, y2 = y2, y1

            d1 = x2 - x1
            d2 = y2 - y1
            if d2 < 0:
                dr = -1
                d2 = abs(d2)
            else:
                dr = 1
            
            for i, j in zip(range(d1 + 1), range(d2 + 1)):
                ps.append((x1 + i, y1 + dr*j))

    return ls, ps, x_max, y_max