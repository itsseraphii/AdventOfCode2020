from utils.aoc_utils import AOCDay, day

@day(13)
class Day13(AOCDay):
    def common(self):
        self.targetTime = int(self.inputData[0])
        data = self.inputData[1].split(',')
        # Array of tuple where [0] is value and [1] is offset
        self.buses = []
        for iBus in range(len(data)) :
            if data[iBus] != 'x' :
                busTuple = (int(data[iBus]), iBus)
                self.buses.append(busTuple)
        return 0

    def part1(self):
        bestOvertime = 42069 # haha funny number
        bestBus = 0
        for bus in self.buses :
            # Get first value that is over targetTime
            busTime = self.targetTime - (self.targetTime % bus[0]) + bus[0]
            
            overTime = busTime - self.targetTime
            if (overTime < bestOvertime):
                bestBus = bus[0]
                bestOvertime = overTime

        return bestBus * bestOvertime
    
    def part2(self):
        # We are searching for the first occurence where
        # all buses leave back to back (in order)

        time = 0
        nextDeparture = self.buses[0][0]

        for bus in self.buses :
            offset = None
            while True:
                if (time + bus[1]) % bus[0] == 0:
                    if offset is None:
                        # Saves time of first occurence
                        offset = time
                        # If last bus, we break (saves unnecessary loop)
                        if bus == self.buses[len(self.buses) - 1] :
                            break
                    else:
                        # Get length of offset where buses leave at
                        # the exact time we want
                        nextDeparture = time - offset
                        break

                time += nextDeparture


        return offset