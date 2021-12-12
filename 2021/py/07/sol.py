from collections import Counter, defaultdict

def median(l):
    sl = sorted(l)
    n = len(l)
    index = (n - 1) // 2
   
    if (n % 2):
        return sl[index]
    else:
        return (sl[index] + sl[index + 1])/2.0

def cost(l, c):
    return sum([sum([j for j in range(1, abs(val - c) + 1)]) for val in l])

def find_opt(i, c, dr, prev):

    curr = cost(i, c)
    if curr > prev:
        return c - dr, prev
    else:
        return find_opt(i, c + dr, dr, curr)


def main():
    
    # Read the input
    i = [int(val) for val in input().split(',')]

    # Part 1 - just find median
    med = int(median(i))
    r = sum([abs(val - med) for val in i])
    print(r)

    # Part 2
    j1, c1 = find_opt(i, med + 1, 1, cost(i, med))
    j2, c2 = find_opt(i, med - 1, -1, cost(i, med))
    if c1 < c2:
        print(c1)
    else:
        print(c2)

if __name__ == '__main__':
    main()