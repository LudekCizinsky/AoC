import sys

def main():
    
    which = sys.argv[1]
    with open(f'{which}.in') as f:
        lines = [int(val.strip('\n')) for val in f.readlines()]
    n = len(lines)

    res = 0
    prev = None
    for i in range(n - 2):
        if prev is not None:
            new = sum(lines[i:i + 3])
            incr = new > prev
            if incr:
                res += 1
            prev = new
        else:
            prev = sum(lines[i:i + 3])
    print(res)

if __name__ == '__main__':
    main()