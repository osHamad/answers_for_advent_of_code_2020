def acc(index, accumulator, arg):
    return index + 1, eval(str(accumulator) + arg)

def jmp(index, arg):
    return eval(str(index) + arg)

def nop(index):
    return index + 1

def main():
    accumulator = 0
    index = 0
    lines_run = []
    with open('input.txt', 'r') as input:
        input = input.read().splitlines()

    while index not in lines_run:
        lines_run.append(index)
        if input[index].split()[0] == 'acc':
            index, accumulator = acc(index, accumulator, input[index].split()[1])
        elif input[index].split()[0] == 'jmp':
            index = jmp(index, input[index].split()[1])
        elif input[index].split()[0] == 'nop':
            index = nop(index)

    print(accumulator)
main()
