import numpy as np
from util import load_input, load_tracking

def next_round_sw(nums, ts, ts2, m):

    num = nums.pop(0)

    for t1, t2 in zip(ts, ts2):

        i = np.where(t1 == num)
        t2[i] = 1

        c = m in np.sum(t2, axis=0)
        r = m in np.sum(t2, axis=1)

        if c or r:
            return num, t1, t2
    
    return next_round_sw(nums, ts, ts2, m)


def next_round_sl(nums, ts, ts2, m, ws):

    if not ts or not nums:
        return ws

    num = nums.pop(0)
    new_ts = []
    new_ts2 = []

    for t1, t2 in zip(ts, ts2):

        i = np.where(t1 == num)
        t2[i] = 1

        c = m in np.sum(t2, axis=0)
        r = m in np.sum(t2, axis=1)

        if not c and not r:
            new_ts.append(t1)
            new_ts2.append(t2)
        else:
            ws.append([num, t1, t2])

    return next_round_sl(nums, new_ts, new_ts2, m, ws)

def main():
    
    nums, ts, ts2, m = load_input()
    num, t1, t2 = next_round_sw(nums, ts, ts2, m)
    res = num*np.sum(t1[np.where(t2 == 0)])
    print(res)

    num, t1, t2 = next_round_sl(nums, ts, ts2, m, ws=[])[-1]
    res = num*np.sum(t1[np.where(t2 == 0)])
    print(res)
    

if __name__ == '__main__':
    main()