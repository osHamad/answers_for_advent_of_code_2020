def format(input):
    new_input = []
    for i in input:
        line = []
        for j in i:
            line.append(j)
        new_input.append(line)

    return new_input

def count_trees(input):
    trees = 0
    pos = 0
    for i in input:
        if pos >= len(i):
            pos = pos % len(i)

        if i[pos] == '#':
            trees += 1

        pos += 3

    return trees


def main():
    input = open('input.txt', 'r')
    input = input.read().splitlines()
    input = format(input)
    answer = count_trees(input)
    print(answer)

main()
