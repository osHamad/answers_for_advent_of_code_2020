class Boat:
    def __init__(self, current_dir):
        self.current_dir = current_dir
        self.north = 0
        self.east = 0
        self.south = 0
        self.west = 0

    def add_to_direction(self, direction, distance):
        if direction == 'N':
            self.north += distance

        elif direction == 'E':
            self.east += distance

        elif direction == 'S':
            self.south += distance

        elif direction == 'W':
            self.west += distance


    def forward(self, distance):
        direction = {0:'N', 90:'E', 180:'S', 270:'W'}
        self.add_to_direction(direction[self.current_dir], distance)


    def change_direction(self, side, digree):
        if side == 'R':
            self.current_dir = abs(self.current_dir + digree)
        elif side == 'L':
            self.current_dir = abs(self.current_dir + abs(digree-360))

        if self.current_dir >= 360:
            self.current_dir -= 360


    def manhattan_distance(self):
        print(abs(self.north - self.south) + abs(self.east - self.west))
