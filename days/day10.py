from utils.aoc_utils import AOCDay, day
import math

@day(10)
class Day10(AOCDay):
    def common(self):
        # Sort adapter list
        # Add 0 jolt input at the begining
        # Add 3 jolt "device adapter"
        self.jolts = [0]
        for line in self.inputData :
            self.jolts.append(int(line))
        self.jolts.sort(key = int)
        self.maxJoltage = self.jolts[len(self.jolts) - 1] + 3
        self.jolts.append(self.maxJoltage)
        return 0

    def part1(self):
        # TLDR when all values are chained, count #
        # of differences of 3 and 1 between each value
        self.oneDiff = 0
        self.twoDiff = 0
        self.threeDiff = 0
        for val in range(len(self.jolts) -1) :
            diff = self.jolts[val + 1] - self.jolts[val]
            if(diff == 3) :
                self.threeDiff += 1
            elif diff == 1:
                self.oneDiff += 1

        return self.oneDiff * self.threeDiff
    
    def part2(self):
        self.memory = {} 
        return self.recursiveMethod(0)

    def recursiveMethod(self, start):
        if (start == len(self.jolts) - 1):
            return 1
        elif start in self.memory :
            return self.memory[start]
        total = 0

        for i in range(start+1, len(self.jolts)):
            if (self.jolts[i] - self.jolts[start] <= 3) :
                total += self.recursiveMethod(i)

        self.memory[start] = total
        print(self.memory[start])

        return total
