def binary(seat, start=7, end=0, condition='B'):
    index = start
    amount = 0
    while index > end:
        if seat[index-1] == condition:
            amount += 2**(start-index)
        index -= 1
    return amount

def main():
    input = open('input.txt', 'r')
    input = input.read().splitlines()
    id = []
    for seat in input:
        row = binary([char for char in seat], 7, 0, 'B')
        col = binary([char for char in seat], 10, 7, 'R')
        id.append(int(row) * 8 + int(col))
        
    for seat in range(min(id), max(id)):
        if seat not in id:
            print(seat)
main()
