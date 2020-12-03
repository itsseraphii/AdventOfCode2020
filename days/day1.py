from utils.aoc_utils import AOCDay, day

@day(1)
class Day1(AOCDay):
    def part1(self):
        # Find the two inputs that add up to 2020
        for x in range(len(self.inputData)):
            for y in range(len(self.inputData) - x):
                if (int(self.inputData[x]) + int(self.inputData[y + x])) == 2020 :
                    part1Answer = int(self.inputData[x]) * int(self.inputData[y + x])
                    return part1Answer
        return 0
    
    def part2(self):
        # Find three inputs that add up to 2020
        for x in range(len(self.inputData)):
            for y in range(len(self.inputData) - x):
                for z in range(len(self.inputData) - x):
                    if (int(self.inputData[x]) + int(self.inputData[y + x]) + int(self.inputData[z + x])) == 2020 :
                        part2Answer = int(self.inputData[x]) * int(self.inputData[y + x]) * int(self.inputData[z + x])
                        return part2Answer
        return 0