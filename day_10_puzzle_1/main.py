def jolts(adapters, current):
    for i in range(len(adapters)):
        jolt_1, jolt_3 = 0, 0
        numbers = []
        if adapters[i] - current in range(1, 4):
            numbers.append(adapters[i])
            if adapters[i] - current == 1:
                jolt_1 += 1
            if adapters[i] - current == 3:
                jolt_3 += 1

    print(jolt_1, jolt_3)
    return numbers, jolt_1, jolt_3


def main():
    with open('input.txt', 'r') as input:
        input = sorted([int(x) for x in input.read().splitlines()])


    adapters = input
    jolt_1 = 0
    jolt_2 = 0

    for current in input:
        x = jolts(adapters, current)
        adapters.extend(x[0])
        sorted(adapters)
        jolt_1, jolt_3 = x[1], x[2]

    print(jolt_1, jolt_3)


main()
# make two lists
# one list is going to be the input
# the second list will be the results of subtracting elements of the first list by current
#current is the first element of the first list and moves forward after each call of the function
