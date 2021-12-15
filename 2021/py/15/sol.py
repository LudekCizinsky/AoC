from sys import stdin
import math

class Node:

    def __init__(self, risk, pos):
        self.risk = risk
        self.pos = pos
        self.dist = math.inf
        self.DR = [0, 1, 0, -1]
        self.DC = [1, 0, -1, 0]
        self.vis = False

    def get_nbs(self, n, m, G):
        
        nbs = []
        for d in range(4):
            r, c = self.pos
            rr = r + self.DR[d]
            cc = c + self.DC[d]
            if 0 <= rr < n and 0 <= cc < m:
                nbs.append(G[rr][cc])
        return nbs

    def update_dist(self, n, m, G, Q):
        
        newQ = []
        nbs = self.get_nbs(n, m, G)
        for nb in filter(lambda node: not node.vis, nbs):
            if self.dist + nb.risk < nb.dist:
                nb.dist = self.dist + nb.risk
                newQ.append(nb)
        
        return sorted(newQ + Q, key=lambda node: node.dist, reverse=True)

def load_input():
    
    G = [[Node(int(r), (i, j,)) for j, r in enumerate(line.strip())] for i, line in enumerate(stdin.readlines())]
    return G

def create_new_map(tile, rep):
    
    n, m = len(tile), len(tile[0])
    new_map = [[0 for j in range(rep*m)] for i in range(rep*n)]

    for i in range(rep*n):
        for j in range(rep*m):
            rd = i//n
            cd = j//m
            r = tile[i - n*rd][j - m*cd].risk + rd + cd
            if r > 9:
                r = r - 9

            new_map[i][j] = Node(risk = r, pos = (i,j,))
    
    return new_map
            

def dijkstra(Q, G, n, m):

    while Q:

        # Reduce queue - O(1)
        v = Q.pop()
        v.vis = True

        # Update dist values
        Q = v.update_dist(n, m, G, Q)

def main():
    
    # PART 1 input
    G1 = load_input()

    # PART 2 input
    G2 = create_new_map(G1, 5)
    row = [node.risk for node in G2[0]]

    for G in [G1, G2]:

        # Distance to source node s
        G[0][0].dist = 0

        # Initial Queue
        Q = [G[0][0]]

        # G dimensions
        n = len(G)
        m = len(G[0])
        
        # Run dijkstra
        dijkstra(Q, G, n, m)

        # Show the distance to the most bottom right node
        print(G[-1][-1].dist)

if __name__ == '__main__':
    main()