from utils.aoc_utils import AOCDay, day

@day(12)
class Day12(AOCDay):
    def common(self):
        self.compass = ['N', 'E', 'S', 'W']

        return 0

    def part1(self):
        self.face = 'E'
        self.x = 0
        self.y = 0
        for line in self.inputData :
            self.navigateShip(line)

        return abs(self.x) + abs(self.y)

    def navigateShip(self, line):
        # Parse line
        direction = line[:1]
        value = int(line[1:])

        # Handle rotations
        if direction == 'R' or direction == 'L':
            current = self.compass.index(self.face)

            if direction == 'L' :
                iteration = -1
            else : iteration = 1


            #Find new direction
            for i in range(int(value/90)):
                current += iteration
                if current == len(self.compass):
                    current = 0
                
                if current == -1:
                    current = len(self.compass) - 1
            
            # Set new face
            self.face = self.compass[current]
        else :
            if direction == 'F':
                direction = self.face
            
            if direction == 'N':
                self.y += value
            elif direction == 'S':
                self.y -= value
            elif direction == 'W':
                self.x -= value
            else:
                self.x += value

    
    def part2(self):
        self.x = 0
        self.y = 0
        self.waypointx = 10
        self.waypointy = 1

        for line in self.inputData :
            self.navigateWaypoint(line)

        return abs(self.x) + abs(self.y)

    def navigateWaypoint(self, line):
        # Parse line
        direction = line[:1]
        value = int(line[1:])

        # Handle rotations
        if direction == 'R':
            # // is an integer division
            for i in range(value//90) :
                buffr = self.waypointx
                self.waypointx = self.waypointy
                self.waypointy = -1*buffr
        
        elif direction == 'L':
            for i in range(value//90) :
                buffr = self.waypointy
                self.waypointy = self.waypointx
                self.waypointx = -1*buffr
        
        elif direction == 'N':
            self.waypointy += value
        elif direction == 'S':
            self.waypointy -= value
        elif direction == 'W':
            self.waypointx -= value
        elif direction == 'E':
            self.waypointx += value
        else : #F
            self.x += self.waypointx * value
            self.y += self.waypointy * value

