def main():
    
    direction = input()
    hor = 0
    ver = 0

    while direction:
        how, dist = direction.split(' ')

        if how == 'forward':
            hor += int(dist)
        elif how == 'down':
            ver += int(dist)
        else:
            ver -= int(dist)

        try:
            direction = input()
        except EOFError:
            break
    print(hor*ver)

if __name__ == '__main__':
    main()