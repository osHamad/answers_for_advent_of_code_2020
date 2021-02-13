def occupied(input):
    leave = []
    sit = []
    for i in range(len(input)):
        for j in range(len(input[i])):
            right = (i, j + 1)
            left = (i, j - 1)
            top = (i - 1, j)
            bottom = (i + 1, j)
            top_left = (i - 1, j - 1)
            top_right = (i - 1, j + 2)
            bottom_left = (i + 1, j - 1)
            bottom_right = (i + 1, j + 1)
            dirs = [right, left, top, bottom, top_left, top_right, bottom_left, bottom_right]
            if input[i][j] != '.':
                occupied = 0
                for dir in dirs:
                    if occupied >= 4:
                        leave.append((i, j))
                        occupied = 0
                        break
                    try:
                        if input[dir[0]][dir[1]] == '#':
                            occupied += 1
                    except IndexError:
                        pass
                else:
                    sit.append((i, j))
                    occupied = 0


    return leave, sit


def main():
    with open('input.txt','r') as input:
        input = [[j for j in x] for x in input.read().splitlines()]

    leave, sit = occupied(input)

    for x in sit:
        input[x[0]][x[1]] = '#'

    for i in leave:
        input[i[0]][i[1]] = 'L'

    print(input)
    leave, sit = occupied(input)
    print(len(sit), len(leave))

main()
