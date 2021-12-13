from sys import stdin

def load_input():

    raw = stdin.readlines()
    cord = set([tuple([int(v) for v in l.strip().split(',')]) for l in filter(lambda x: 'fold' not in x and x.strip(), raw)])
    fold = [l.strip().split(' ')[-1] for l in filter(lambda x: 'fold' in x and x.strip(), raw)]
    
    return cord, fold

def fold(ax, val, crds):

    new_crds = set()
    for cr in crds:

        # Only relevant half
        if cr[ax] > val:

            # Compute the new cordinates
            d = cr[ax] - val
            new_cr = [None, None]
            new_cr[ax - 1] = cr[ax - 1]
            if not (val - d) < 0:
                new_cr[ax] = val - d
                new_crds.add(tuple(new_cr))
        
        else:
            new_crds.add(cr)
    
    return new_crds

def visualize(crds):
    
    # Find max x and y cords
    x_max = max(crds, key=lambda x: x[0])[0]
    y_max = max(crds, key=lambda x: x[1])[1]

    # Create the corresponding grid
    for i in range(x_max + 1):
        row = [1 if tuple([i, j]) in crds else 0 for j in range(y_max + 1)]
        if sum(row) == 0:
            print()
            print('='*50)
            print()
        else:
            row = ['#' if tuple([i, j]) in crds else '.' for j in range(y_max + 1)]
            print(" ".join(row))

def main():
    
    # Load input
    crds, fd = load_input()

    # Cordinate mapping
    crm = lambda ax: 0 if ax == 'x' else 1

    # PART 1
    ax, val = fd[0].split('=')
    p1_crds = fold(crm(ax), int(val), crds)
    print(f'PART 1 clearanswer: {len(p1_crds)}')

    # PART 2
    for f in fd:
        ax, val = f.split('=')
        crds = fold(crm(ax), int(val), crds)
    visualize(crds)


if __name__ == '__main__':
    main()