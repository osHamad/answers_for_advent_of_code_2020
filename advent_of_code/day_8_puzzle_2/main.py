import copy

def acc(index, accumulator, arg):
    return index + 1, eval(str(accumulator) + arg)

def jmp(index, arg):
    return eval(str(index) + arg)

def nop(index):
    return index + 1

def is_solution(local_input, accumulator, index):
    lines_run = []
    while index not in lines_run:
        lines_run.append(index)
        if index == len(local_input)-1:
            print(accumulator)
            return
        elif local_input[index].split()[0] == 'acc':
            index, accumulator = acc(index, accumulator, local_input[index].split()[1])
        elif local_input[index].split()[0] == 'jmp':
            index = jmp(index, local_input[index].split()[1])
        elif local_input[index].split()[0] == 'nop':
            index = nop(index)

def main():
    with open('input.txt', 'r') as input:
        input = input.read().splitlines()

    for line in range(len(input)):
        local_input = copy.deepcopy(input)
        accumulator = 0
        index = 0
        if local_input[line].split()[0] != 'acc':

            if local_input[line].split()[0] == 'jmp':
                local_input[line] = f'nop {local_input[line].split()[1]}'

            elif local_input[line].split()[0] == 'nop':
                local_input[line] = f'jmp {local_input[line].split()[1]}'

            is_solution(local_input, accumulator, index)
main()
