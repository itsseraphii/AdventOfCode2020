from utils.aoc_utils import AOCDay, day

@day(9)
class Day9(AOCDay):
    def common(self):
        return 0

    def part1(self):
        # Find first number which is not the sum of
        # two numbers in the previous 25 (prevNums) stated
        prevNums = 25
        self.xmasExploit = -1

        for i in range(prevNums, len(self.inputData)):
            targetNum = int(self.inputData[i])
            found = False

            for posNum1 in range(prevNums) :
                for posNum2 in range(posNum1, prevNums) :

                    num1 = int(self.inputData[i-prevNums+posNum1])
                    num2 = int(self.inputData[i-prevNums+posNum2])

                    if (num1 + num2 == targetNum) :
                        found = True
                    
                if found : 
                    break

            if not found :
                self.xmasExploit = int(self.inputData[i])
        
        return self.xmasExploit
    
    def part2(self):
        #Find set of numbers that = xmasExploit
        #and return min and max values of the set

        # Potential improvement, start from xmasExploit pos
        # and go down, its probably faster
        for minPos in range(len(self.inputData)) :
            maxPos = minPos
            overXmas = False

            setTotal = int(self.inputData[minPos])
            # List of all values in current set
            valList = [int(self.inputData[minPos])]

            while not overXmas :
                overXmas = False
                maxPos += 1

                setTotal += int(self.inputData[maxPos])
                valList.append(int(self.inputData[maxPos]))

                if setTotal > self.xmasExploit :
                    overXmas = True
                    continue

                if setTotal == self.xmasExploit :
                    print("First value in set:", self.inputData[minPos])
                    print("Last value in set:", self.inputData[maxPos])

                    return min(valList) + max(valList)
                

        return 0