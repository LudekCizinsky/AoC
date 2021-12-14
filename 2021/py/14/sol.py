from sys import stdin
from collections import Counter

def load_input():

    # Get the raw input
    raw = [l.strip('\n') for l in stdin.readlines() if l.strip()]

    # Count the unique letters
    t = raw.pop(0)
    c = Counter(t)

    # Count the pairs
    pairs = dict()
    for i in range(1, len(t)):
        p = t[i - 1: i + 1]
        if p in pairs:
            pairs[p] += 1
        else:
            pairs[p] = 1

    # Get the mapping for insertions
    m = {v.split('->')[0].strip(): v.split('->')[1].strip() for v in raw}
    
    return pairs, m, c

def main():
    
    # Load data
    t, m, C = load_input()

    for s in range(40):

        # Update polymer
        pairs, counts = list(t.keys()), list(t.values())
        newt = dict()
        for p, c in zip(pairs, counts):
            if m.get(p):

                # Create new pairs
                p1, p2 = p[0] + m[p], m[p] + p[1]
                for i in [p1, p2]:
                    if i in newt:
                        newt[i] += c
                    else:
                        newt[i] = c
                
                # Add inserted value to counter
                if m[p] in C:
                    C[m[p]] += c
                else:
                    C[m[p]] = c
        
        # Update the template
        t = newt

        # PART 1
        if s == 9:
            print(C.most_common()[0][1] - C.most_common()[-1][1])

    # PART 2
    print(C.most_common()[0][1] - C.most_common()[-1][1])

if __name__ == '__main__':
    main()