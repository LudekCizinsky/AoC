from sys import stdin
from collections import deque
from functools import reduce

def parse_lit(p):

    run = True
    parsed = ''
    t = 0
    while run:
        v = "".join([p.popleft() for _ in range(5)])
        t += 5
        parsed += v[1:]
        if v[0] == '0':
            run = False
    
    return int(parsed, 2), t

def operate(opid, l):

    if opid == 0:
        return sum(l)
    elif opid == 1:
        return reduce((lambda x, y: x * y), l)
    elif opid == 2:
        return min(l)
    elif opid == 3:
        return max(l)
    elif opid == 5:
        return int(l[0] > l[1])
    elif opid == 6:
        return int(l[0] < l[1])
    elif opid == 7:
        return int(l[0] == l[1])


def parse(p):

    # Base case
    if len(p) < 6:
        return 0, 0, []

    # Count parsed total
    total = 0

    # Get version and typeid of the packet
    vid = int("".join([p.popleft() for _ in range(3)]), 2)
    typeid = int("".join([p.popleft() for _ in range(3)]), 2)
    total += 6


    # Is literal?
    if typeid == 4:
        l, t = parse_lit(p)
        return vid, total + t, [l]
    
    # Operator
    else:

        # * Parse length typeid
        ltid = p.popleft()
        total += 1

        # * Parse subpackets
        if ltid == '0':
            ln = int("".join([p.popleft() for _ in range(15)]), 2)
            total += 15

            curr = 0
            lits = []
            while curr != ln:
                vid2, t2, l = parse(p)
                lits += l
                vid += vid2
                curr += t2
            
            return vid, ln + total, [operate(typeid, lits)]

        else:
            n = int("".join([p.popleft() for _ in range(11)]), 2)
            total += 11
            curr = 0
            lits = []
            while curr < n:
                vid2, t2, l = parse(p)
                lits += l
                vid += vid2
                curr += 1
                total += t2

            return vid, total, [operate(typeid, lits)]


def main():

    # Parse the input and the header
    p = ''
    for s in stdin.read():
        p += format(int(s, 16), "04b")
    p = deque(p)
    
    p1, t, p2 = parse(p)
    
    print(p1)
    print(p2[0])

if __name__ == '__main__':
    main()