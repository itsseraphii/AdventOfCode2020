from utils.aoc_utils import AOCDay, day

@day(15)
class Day15(AOCDay):
    def common(self):
        self.startNums = []
        for i in self.inputData[0].split(',') : self.startNums.append(int(i))
        return 0

    def part1(self):
        return self.playGame(2020)

        
    
    def part2(self):
        # Probably optimisation that could be done, but
        # Math exam in less than 36 hours so haha byeee
        return self.playGame(30000000)

    def playGame(self, rounds):
        # Key is spoken number, value is when it was last said
        dictSpokenNums = {}

        #Setup first loop of players
        for i in range(1, len(self.startNums)+1) :
            dictSpokenNums[self.startNums[i-1]] = i

        lastNum = self.startNums[len(self.startNums)-1]

        for turn in range(len(self.startNums), rounds) :
            if lastNum in dictSpokenNums :
                lastTurnSaid = dictSpokenNums[lastNum]
                dictSpokenNums[lastNum] = turn
                lastNum = turn - lastTurnSaid
            else :
                dictSpokenNums[lastNum] = turn
                lastNum = 0

        return lastNum
