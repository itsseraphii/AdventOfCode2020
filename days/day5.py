from utils.aoc_utils import AOCDay, day

@day(5)
class Day5(AOCDay):
    def common(self):
        self.lstSeats = []
        for line in self.inputData :
            #Parse row search
            rowInfo = line[:7]
            rowInfo = rowInfo.replace('F', '0')
            rowInfo = rowInfo.replace('B', '1')

            #Parse columns
            colInfo = line[-3:]
            colInfo = colInfo.replace('L', '0')
            colInfo = colInfo.replace('R', '1')

            seatId = int(rowInfo, 2) * 8 + int(colInfo, 2)
            self.lstSeats.append(seatId)
            
        
        self.lstSeats.sort(reverse=True)
        return 0

    def part1(self):
        return self.lstSeats[0]

    
    def part2(self):
        for i in range(self.lstSeats[len(self.lstSeats) - 1], self.lstSeats[0]) :
            if not i in self.lstSeats :
                return i