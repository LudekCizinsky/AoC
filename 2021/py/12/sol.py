from sys import stdin

def read_input():

    ls = [l.strip().split('-') for l in stdin.readlines()]
    G = dict()
    for l in ls:
        n1, n2 = l

        for e in [[n1, n2], [n2, n1]]:
            f, t = e
            if f in G:
                G[f].append(t)
            else:
                G[f] = [t]
    return G


def explore(G, paths, result, s=dict()):

    new_paths = []
    for path in paths:

        curr = path[-1]

        if curr == 'end':
            result.add(",".join(path))
            continue
        
        for nb in G[curr]:
            if nb.isupper() and  nb != 'start':
                new_paths.append(path + [nb])
            elif nb not in path and nb != 'start':
                new_paths.append(path + [nb])
            elif nb in s:
                cn = path.count(nb)
                if cn < s[nb]:
                    new_paths.append(path + [nb])
    
    if new_paths:
        explore(G, new_paths, result, s)


def main():
    
    # Read the input
    G = read_input()

    # PART 1
    res = set()
    explore(G, paths=[['start', p] for p in G['start']], result=res)
    print(len(res))

    # PART 2
    res = set()
    sm = [k for k in G.keys() if k != 'start' and k != 'end' and not k.isupper()]
    for sc in sm:
        explore(G, paths=[['start', p] for p in G['start']], result=res, s={sc: 2})
    print(len(res))

if __name__ == '__main__':
    main()