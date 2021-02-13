def format(input):
    new_input = []
    for i in input:
        line = []
        for j in i:
            line.append(j)
        new_input.append(line)

    return new_input


def count_trees(input, right, down):
    trees = 0
    col = 0
    row = 0
    while row < len(input):

        if col >= len(input[0]):
            col = col % len(input[0])

        if input[row][col] == '#':
            trees += 1

        row += down
        col += right

    return trees


def main():
    input = open('input.txt', 'r')
    input = input.read().splitlines()
    input = format(input)
    a = count_trees(input, 1, 1)
    b = count_trees(input, 3, 1)
    c = count_trees(input, 5, 1)
    d = count_trees(input, 7, 1)
    e = count_trees(input, 1, 2)
    print(a*b*c*d*e)

main()
