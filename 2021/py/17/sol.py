from sys import stdin

def simulate(xv, yv, xrg, yrg):

    # Setup
    xmin, xmax = xrg
    ymin, ymax = yrg
    withinx = lambda x: xmin <= x and x <= xmax
    withiny = lambda y: ymin <= y and y <= ymax
    xdr = -1 if xv > 0 else 1
    if xdr == 1:
        xmin, xmax = xmax, xmin


    x = 0
    y = 0
    ys = []
    while (xv != 0 and x < xmax) or y > ymin:
        
        x += xv
        y += yv
        ys.append(y)

        if withinx(x) and withiny(y):
            return True, max(ys)

        if xv != 0:
            xv += xdr
        yv -= 1
    
    return False, max(ys)
    

def main():

    # Read input
    raw = [i.strip(',x=y') for i in stdin.read().split(' ')]
    xrg, yrg = [int(v) for v in raw[-2].split('..')], [int(v) for v in raw[-1].split('..')]


    # Brute force :(
    xv = [i for i in range(-300, 400)]
    yv = [i for i in range(-300, 400)]
    ys = []
    hc = 0
    for i in xv:
        for j in yv:
            hit, ymx = simulate(i, j, xrg, yrg)
            if hit:
                hc += 1
                ys.append(ymx)
    print('Part 1: ', max(ys))
    print('Part 2: ', hc)

if __name__ == '__main__':
    main()