def main():
    
    direction = input()
    hor = 0
    ver = 0
    aim = 0

    while direction:
        how, dist = direction.split(' ')

        if how == 'forward':
            hor += int(dist)
            ver += aim*int(dist)
        elif how == 'down':
            aim += int(dist)
        else:
            aim -= int(dist)

        try:
            direction = input()
        except EOFError:
            break
    print(hor*ver)

if __name__ == '__main__':
    main()