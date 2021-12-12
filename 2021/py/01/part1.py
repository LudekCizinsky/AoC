def main():

    prev = None
    m = int(input())
    res = 0
    while m:
        if prev:
            incr = m > prev
            if incr:
                res += 1
        prev = m
        try:
            m = int(input())
        except EOFError:
            break
    print(res)

if __name__ == '__main__':
    main()