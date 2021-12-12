from collections import Counter

def load_rows():
    row = input()
    rows = []

    while row:
        row = [int(val) for val in row]
        rows.append(row)
        try:
            row = input()
        except EOFError:
            break
    
    return rows
    

def get_count(rows):

    c = {j: [0, 0] for j  in range(len(rows[0]))}
    for row in rows:

        m = len(row)
        
        for j in range(m):
            b = row[j]
            c[j][b] += 1
    
    gri = [0 if l[0] > l[1] else 1 for l in c.values()]
    eri = [1 if l[0] > l[1] else 0 for l in c.values()]

    return c


def part1():
    
    c = get_count(load_rows())
    gr = "".join(["0" if l[0] > l[1] else "1" for l in c.values()])
    er = "".join(["1" if l[0] > l[1] else "0" for l in c.values()])
    print(int(gr, 2)*int(er, 2))

def filt(rows, cr, j = 0):

    if len(rows) == 1:
        return "".join(str(val) for val in rows[0])
    
    c = Counter([row[j] for row in rows])
    c = [c[0], c[1]]

    fr = list(filter(lambda row: row[j] == cr(c), rows))

    return filt(fr, cr, j + 1)
    

def part2():

    cr1 = lambda x: 0 if x[0] > x[1] else 1
    cr2 = lambda x: 1 if x[0] > x[1] else 0

    rows = load_rows()
    oxyg = int(filt(rows, cr1), 2)
    co2 =  int(filt(rows, cr2), 2)

    print(oxyg*co2)
    

if __name__ == '__main__':
    part2()