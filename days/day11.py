from utils.aoc_utils import AOCDay, day

@day(11)
class Day11(AOCDay):
    def common(self):
        #Convert to two dimensional array
        self.seatLayout = [[0 for x in range(len(self.inputData[0]))] for y in range(len(self.inputData))]
        self.ogBackup = [[0 for x in range(len(self.inputData[0]))] for y in range(len(self.inputData))]
        for i in range(len(self.inputData)):
            for j in range(len(self.inputData[i])) :
                self.seatLayout[i][j] = self.inputData[i][j]
                self.ogBackup[i][j] = self.inputData[i][j]

        return 0

    def part1(self):
        #Run simulation until stale
        stale = False
        while not stale:
            newLayout = self.heartbeat(False)

            if not self.seatLayout == newLayout :
                self.seatLayout = newLayout
            else : 
                stale = True

        return self.occupiedSeats()

        

    def occupiedSeats(self):
        occupiedSeats = 0
        #Get number of seats
        for i in range(len(self.seatLayout)):
            for j in range(len(self.seatLayout[i])) :
                if self.seatLayout[i][j] == '#' :
                    occupiedSeats += 1
        return occupiedSeats

    def heartbeat(self, v2):
        newLayout = [['A' for x in range(len(self.inputData[0]))] for y in range(len(self.inputData))]
        if v2 :
            bail = 5
        else :
            bail = 4

        for i in range(len(self.inputData)):
            for j in range(len(self.inputData[0])):
                if self.seatLayout[i][j] == 'L' :
                    if self.lookAround(i, j, v2) == 0:
                        newLayout[i][j] = '#'
                    else :
                        newLayout[i][j] = 'L'
                    
                elif self.seatLayout[i][j] == '#' :
                    if self.lookAround(i, j, v2) >= bail:
                        newLayout[i][j] = 'L'
                    else : 
                        newLayout[i][j] = '#'
                else : 
                    newLayout[i][j] = '.'
        return newLayout
                    
    def lookAround(self, i, j, v2):
        adjacentSeats = 0
        if not v2 :
            # Top
            if i-1 >= 0 :
                if self.checkSeat(i-1, j) :
                    adjacentSeats+=1

                # Top left
                if j-1 >= 0:
                    if self.checkSeat(i-1, j-1):
                        adjacentSeats+=1
                
                # Top right
                if j+1 < len(self.seatLayout[i]) :
                    if self.checkSeat(i-1, j+1):
                        adjacentSeats+=1

            #Center left
            if j-1 >= 0:
                if self.checkSeat(i, j-1):
                    adjacentSeats+=1

            # Center right
            if j+1 < len(self.seatLayout[i]) :
                if self.checkSeat(i, j+1):
                    adjacentSeats+=1

            # Bottom
            if i+1 < len(self.seatLayout) :
                if self.checkSeat(i+1, j) :
                    adjacentSeats+=1

                # Bot left
                if j-1 >= 0:
                    if self.checkSeat(i+1, j-1):
                        adjacentSeats+=1
                
                # Bot right
                if j+1 < len(self.seatLayout[i]) :
                    if self.checkSeat(i+1, j+1):
                        adjacentSeats+=1
        else : #v2 search
            # Top
            y = i
            while y > 0 :
                y-=1
                if self.seatLayout[y][j] != '.':
                    if self.checkSeat(y, j):
                        adjacentSeats += 1
                    break

            # Top left
            y = i
            x = j
            while y > 0 and x > 0:
                y -= 1
                x -= 1
                if self.seatLayout[y][x] != '.':
                    if self.checkSeat(y, x):
                        adjacentSeats += 1
                    break

            # Top right
            y = i
            x = j
            while y > 0 and x < len(self.inputData[0]) - 1:
                y -= 1
                x += 1
                if self.seatLayout[y][x] != '.':
                    if self.checkSeat(y, x):
                        adjacentSeats += 1
                    break

            # Center left
            x = j
            while x > 0 :
                x-=1
                if self.seatLayout[i][x] != '.':
                    if self.checkSeat(i, x):
                        adjacentSeats += 1
                    break
            
            # Center right
            x = j
            while x < len(self.inputData[0]) - 1:
                x += 1
                if self.seatLayout[i][x] != '.':
                    if self.checkSeat(i, x):
                        adjacentSeats += 1
                    break

            # Bottom
            y = i
            while y < len(self.inputData) - 1:
                y += 1
                if self.seatLayout[y][j] != '.':
                    if self.checkSeat(y, j):
                        adjacentSeats += 1
                    break
            
            # Bottom left
            y = i
            x = j
            while x > 0 and y < len(self.inputData) - 1:
                y += 1
                x -= 1
                if self.seatLayout[y][x] != '.':
                    if self.checkSeat(y, x):
                        adjacentSeats += 1
                    break

            # Bot right
            y = i
            x = j
            while x < len(self.inputData[0]) - 1 and y < len(self.inputData) - 1:
                y += 1
                x += 1
                if self.seatLayout[y][x] != '.':
                    if self.checkSeat(y, x):
                        adjacentSeats += 1
                    break
        
        return adjacentSeats

    def checkSeat(self, i, j):
        return self.seatLayout[i][j] == '#'

    def part2(self):
        #Reset seat layout
        self.seatLayout = self.ogBackup
        #Run simulation until stale
        stale = False
        loopCounter = 0

        while not stale:
            newLayout = self.heartbeat(True)

            if not self.seatLayout == newLayout :
                self.seatLayout = newLayout
            else : 
                stale = True

        return self.occupiedSeats()