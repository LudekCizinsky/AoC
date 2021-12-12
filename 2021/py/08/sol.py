import sys
from collections import Counter

def main():
    
    # Load the data
    with open(f'{sys.argv[1]}.in') as f:
        inp = f.readlines()
    inp = {i: {j: [v2 for v2 in s.strip('\n ').split(' ')] for j, s in zip(['in', 'out'], v.split('|'))} for i, v in enumerate(inp)}
    
    ## PART 1
    # Create a lookup for segments of digits
    l = {
        0: 'abcefg',
        1: 'cf',
        2: 'acdeg',
        3: 'acdfg',
        4: 'bcdf',
        5: 'abdfg',
        6: 'abdefg',
        7: 'acf',
        8: 'abcdefg',
        9: 'abcdfg' 
    }

    # Find the digits which have a unique len
    uc = [k for k, c in Counter([len(l[i]) for i in range(10)]).items() if c == 1]
    ud = [i for i in range(10) if len(l[i]) in uc]
    
    # Count the digits in the output
    c = 0
    for v in inp.values():

        o = v['out']
        for i in o:
            if len(i) in uc:
                c += 1
    #print(c)

    ## PART 2
    res = []
    for v in inp.values():

        # PART 2A --> Define the mapping
        m = {}
        i = sorted(v['in'], key=len)

        # First determine possibilities for each of the 7 segments
        used_old = set()
        used_org = set()
        for old in i:
            if len(old) in uc:
                num = ud[uc.index(len(old))]
                orgs = set(l[num]) - used_org
                for org in orgs:
                    m[org] = set(old) - used_old
                used_old.update(set(old))
                used_org.update(orgs)
        
        # Get inputs with len 5 only
        ifl = set([val for val in i if len(val) == 5])
        
        # Get the encoding for 3
        enc3_str = [val for val in ifl if len(set(val) -  m['c']) == 3][0]
        enc3 = set(enc3_str)
        
        # Update the mapping
        m['d'] = enc3 & m['d']
        m['b'] = m['b'] - enc3
        m['g'] = enc3 & m['g']
        m['e'] = m['e'] - enc3

        # Get the encoding for 2
        ifl = ifl - set([enc3_str])
        me = next(iter(m['e']))
        enc2 = set([val for val in ifl if me in val][0])

        # Update the mapping
        m['c'] = enc2 & m['c']
        m['f'] = m['f'] - enc2

        # Adjust the mapping so the values are just strings and reverse the order
        m = {key: next(iter(val)) for key, val in m.items()}
        m = {key: val for val, key in m.items()}

        # Create a new mapping encoding --> number
        l2 = {key: val for val, key in l.items()}

        # PART 2B --> use the mapping to determine output
        o = v['out']
        nums = []
        for val in o:
            key = "".join(sorted([m[s] for s in val]))
            num = l2[key]
            nums.append(str(num))
        res.append(int("".join(nums)))
    
    # Show the result
    print(sum(res))


if __name__ == '__main__':
    main()