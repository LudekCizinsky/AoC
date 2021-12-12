import sys

def is_lower(m, v, ii, jj):

    try:
        if ii < 0 or jj < 0:
            return True
        return v < m[ii][jj]
    except IndexError:
        return True

def goes_up(m, v, ii, jj):

    try:
        if ii < 0 or jj < 0:
            return None
        return v < m[ii][jj] and m[ii][jj] != 9
    except IndexError:
        return None


def get_basin_size(m, i, j, s, v):

    v.add((i, j))
    for d in [-1, 1]:
        
        # Figure out if it makes sense to go to the given direction
        if (i + d, j) not in v:
            dir1 = goes_up(m, m[i][j], i + d, j) # up or down
            if dir1:
                s = 1 + get_basin_size(m, i + d, j, s, v)

        if (i, j + d) not in v:
            dir2 = goes_up(m, m[i][j], i, j + d) # left or right
            if dir2:
                s = 1 + get_basin_size(m, i, j + d, s, v)
    
    return s


def main():
    
    with open(f'{sys.argv[1]}.in') as f:
        inp = f.readlines()
        inp = [[int(h) for h in line.strip()] for line in inp]
        n = len(inp)
        m = len(inp[0])
    
    answ1 = 0
    lp = []
    for i in range(n):
        for j in range(m):
            p = inp[i][j]
            left, right = is_lower(inp, p, i, j - 1), is_lower(inp, p, i, j + 1)
            up, down = is_lower(inp, p, i - 1, j), is_lower(inp, p, i + 1, j)
            cm = left and right and up and down
            if cm:
                lp.append((i, j))
                answ1 += 1 + p
    print(answ1)

    b = []
    for p in lp:
        sz = get_basin_size(inp, p[0], p[1], 1, set())
        b.append(sz)
    top3 = sorted(b, reverse=True)[:3]
    print(top3[0]*top3[1]*top3[2])

if __name__ == '__main__':
    main()