from boat import Boat

def main():
    with open('input.txt', newline='') as raw_input:
        puzzle_input = raw_input.read().splitlines()

    puzzle_boat = Boat(90)

    for dir in puzzle_input:
        if dir[0] in 'NESW':
            puzzle_boat.add_to_direction(dir[0], int(dir[1:]))

        elif dir[0] in 'LR':
            puzzle_boat.change_direction(dir[0], int(dir[1:]))

        elif dir[0] == 'F':
            puzzle_boat.forward(int(dir[1:]))

    # prints answer
    puzzle_boat.manhattan_distance()

if __name__ == '__main__':
    main()
