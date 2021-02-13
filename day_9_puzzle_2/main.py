def main():
    with open('input.txt', 'r') as input:
        input = input.read().splitlines()

    start = 0
    while True:
        nums = [input[x] for x in range(start, start + 25)]
        for num in nums:
            if str(int(input[start+25]) - int(num)) in nums and int(input[start+25]) - int(num) != num:
                break
        else:
            index = 0
            sum_nums = []
            while True:
                for i in range(index, len(input)):
                    if sum(sum_nums) == int(input[start+25]):
                        print(min(sum_nums)+max(sum_nums))
                        return
                    elif sum(sum_nums) > int(input[start+25]):
                        index += 1
                        sum_nums = []
                        break
                    sum_nums.append(int(input[i]))
            break
        start += 1
main()
