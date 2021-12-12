from sys import stdin


class Grid:

    def __init__(self, G, n, m):
        self.G = G
        self.n = n
        self.m = m
        self.tf = 0 # total flashes
    
    def step(self):

        # Add 1 to each octopus
        for i in range(self.n):
            for j in range(self.m):
                o = self.G[i][j]
                o.e += 1

        # Flash if neccessary
        cf = 0
        for i in range(self.n):
            for j in range(self.m):
                o = self.G[i][j]
                if o.e > 9:
                    o.e = 0
                    inc = 1 + o.flash()
                    self.tf += inc
                    cf += inc
        return cf
    
    def visualize(self):
        for i in range(self.n):
            print([self.G[i][j].e for j in range(self.m)])



class Octopus:

    def __init__(self, e, p):
        self.e = e
        self.p = p
        self.dr = [-1, 0, 1, 0, -1, -1, 1, 1]
        self.dc = [0, 1, 0, -1, -1, 1, -1, 1]
        self.is_within_range = lambda p: 0 <= p[0] < p[2] and 0 <= p[1] < p[3]
        self.nbs = []
    
    def add_nb(self, n, m, M):
        
        for d in range(8):
            rr = self.p[0] + self.dr[d]
            cc = self.p[1] + self.dc[d]
            p2 = (rr, cc, n, m)
            if self.is_within_range(p2):
                self.nbs.append(M[rr][cc])
    
    def flash(self):
        t = 0
        for nb in self.nbs:

            if nb.e != 0:
                nb.e += 1
            
            if nb.e > 9:
                nb.e = 0
                t += 1 + nb.flash()
        return t
    
    def __repr__(self):
        return f'Row: {self.p[0]} | Col: {self.p[1]} | EL: {self.e}'

def main():

    # Load the data
    M = [[Octopus(int(v), (i, j)) for j, v in enumerate(list(l))] for i, l in enumerate(stdin.read().split("\n"))]
    n = len(M)
    m = len(M[0])

    # Add neighbors for each octopus
    for i in range(n):
        for j in range(m):
            M[i][j].add_nb(n, m, M)
    G = Grid(M, n, m)

    # PART 1
    for s in range(100):
        G.step()
    print(G.tf)

    # PART 2
    t = 101
    while G.step() != n*m:
        t += 1
    print(t)



if __name__ == '__main__':
    main()