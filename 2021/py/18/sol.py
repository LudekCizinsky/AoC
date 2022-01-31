from sys import stdin
from collections import deque
import math

class Pair:

    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.parent = None

    def explode(self, left, right):

        # Base case
        if not self.parent or (not left and not right):
            return None

        if left and type(self.parent.left) == int:
            self.parent.left += left
            left = None

        if right and type(self.parent.right) == int:
            self.parent.right += right
            right = None

        return self.parent.explode(left, right)

    def show(self):

        q = deque([self.left, self.right])
        lvl = 1
        while q:

            tmp = '|  '
            newq = deque()
                
            for ch in q:
                if type(ch) != int:
                    tmp += 'Pair  |  '
                    newq.extend([ch.left, ch.right])
                else:
                    tmp += f'{ch}  |  '

            print(f'LVL: {lvl}')
            print(tmp)
            lvl += 1
            q = newq

    def reduce(self, lvl=0, how='explode'):
        
        if how == 'explode':
            # Base case
            stop = type(self.left) == int and type(self.right) == int and lvl == 4
            if stop:

                # Distribute values of the pair
                self.explode(self.left, self.right)

                # Turn the pair into zero
                if self.parent.left == self:
                    self.parent.left = 0
                else:
                    self.parent.right = 0
                
                return True
        
            stop = False
            for ch in [self.left, self.right]:
                if type(ch) != int and not stop:
                    ch.parent = self
                    stop = ch.reduce(lvl + 1)
            
            return stop
        
        else:

            stop = False
            for ch in [self.left, self.right]:
                if type(ch) != int and not stop:
                    ch.parent = self
                    stop = ch.reduce(lvl + 1, how='split')
                elif type(ch) ==  int and not stop and ch >= 10:
                    
                    p = Pair(ch//2, math.ceil(ch/2))
                    if self.left == ch:
                        self.left = p
                    else:
                        self.right = p

                    return True

            return stop 
    
    def magnitude(self):
        
        if type(self.left) == int:
            left = 3*self.left
        else:
            left = 3*self.left.magnitude()
        
        if type(self.right) == int:
            right = 2*self.right
        else:
            right = 2*self.right.magnitude()
        
        return left + right

def load():

    raw = [deque(l.strip()) for l in stdin.readlines()]
    numbers = deque()
    
    # Parse
    for row in raw:
        
        commas = deque()
        vals = deque()
        v = row.popleft()

        while len(row) > 0:
            if v == ']':
                right = vals.pop()
                left = vals.pop()
                v = Pair(left, right)
                vals.append(v)
            elif v.isdigit():
                vals.append(int(v))
            v = row.popleft()

        numbers.append(Pair(vals[0], vals[1]))

    return numbers


def main():
    
    nums = load()
    tmp = nums.popleft()

    while nums:
        new_num = Pair(tmp, nums.popleft())
        ops = ['explode', 'split']

        while ops:
            op = ops.pop(0)
            changed = new_num.reduce(how=op) 
            if changed:
                ops = ['explode', 'split']

        tmp = new_num

    result = tmp.magnitude()
    tmp.show()
    print()
    print(result)


if __name__ == '__main__':
    main()
