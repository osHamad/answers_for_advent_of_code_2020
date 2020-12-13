def main():
    with open('input.txt', 'r') as input:
        input = input.read().splitlines()
    start = 0
    while True:
        sums = [input[x] for x in range(start, start + 25)]
        for sum in sums:
            if str(int(input[start+25]) - int(sum)) in sums and int(input[start+25]) - int(sum) != sum:
                break
        else:
            print(input[start+25])
            break
        start += 1
main()
