import sys
import numpy as np

def load_tracking(n , m):
    
    return [np.zeros((m ,m)) for _ in range(n)]

def load_input():
    
    which = sys.argv[1]

    with open(f"{which}.in") as f:
        o = f.readlines()
    
    nums = o.pop(0)
    o.pop(0)
    nums = [int(val) for val in nums.strip('\n').split(',')]

    ts = list()
    curr = -1

    while o:

        r = o.pop(0).strip(' \n')
        t = []

        while r:
            r = [int(val) for val in r.split(' ') if val]
            t.append(r)
            if o:
                r = o.pop(0).strip(' \n')
            else:
                break
        
        ts.append(np.array(t))
    
    n, m = len(ts), ts[0].shape[0]
    ts2 = load_tracking(n, m)

    return nums, ts, ts2, m
