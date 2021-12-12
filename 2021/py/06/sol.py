import sys

def main():
    
    # Load the data
    which = sys.argv[1]
    with open(f'{which}.in') as f:
        inp = f.readlines()[0]
    inp = [int(val.strip('\n')) for val in inp.split(',')]

    # Create a state list
    s = [inp.count(i) for i in range(9)]

    # How many days
    how_many = int(sys.argv[2])

    # Update the states
    for _ in range(how_many):

        # Part 1: Shift each fish (except from those in state 0) to new state
        # Part 2: Create new fish (state 8)
        s = s[1:] + s[:1]

        # Do not forget to also update those who transfered from 0 --> 6
        s[6] += s[-1]

    # Sum the number of fish in each state and show their total
    print(sum(s))


if __name__ == '__main__':
    main()
