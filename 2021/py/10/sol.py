from sys import stdin

def main():

    ls = stdin.read().split("\n")

    opn = {'(': ')', '[': ']', '{':'}', '<':'>'}
    s1 = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    s2 = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }
    t1 = 0
    complsc = []
    for l in ls:
        broken = False
        s = []
        for c in l:
            if c in opn:
                s.append(c)
            else:
                o = s.pop()
                if c != opn[o]:
                    t1 += s1[c]
                    broken = True
                    break

        t2 = 0
        compl = ''
        if len(s) != 0 and not broken:
            for i in s[::-1]:
                t2 = t2*5 + s2[opn[i]]
            complsc.append(t2)
    
    print(f'Total score for corrupted: {t1}')
    print(f'Total score for completion: {sorted(complsc)[int(len(complsc)/2)]}')


if __name__ == '__main__':
    main()