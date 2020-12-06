from utils.aoc_utils import AOCDay, day

@day(6)
class Day6(AOCDay):
    def common(self):
        # Opening filestream
        file = open(self.inputPath, "r")

        self.inputData = []
        # Reading and appending each line to the inputData
        for line in file:
            line = line.replace('\n', '')
            self.inputData.append(line)
        #Add empty line at the end of the file
        self.inputData.append('')

        # Add empty line at the end of the file
        self.inputData.append('')

        # Closing filestream
        file.close()

        return 0

    def part1(self):
        # TLDR Find amount of unique chars on a line
        parsedInput = []
        buffer = ""
        # Put groups on a single line
        for line in self.inputData :
            if not line :
                if buffer != "":
                    #Remove whitespaces (just in case)
                    buffer = buffer.replace(' ', '')
                    parsedInput.append(buffer)
                    buffer = ""

            else :
                buffer += line


        sumOfCounts = 0

        for group in parsedInput :
            lstChars = []

            for i in range(len(group)) :
                if not group[i] in lstChars :
                    lstChars.append(group[i])
            
            sumOfCounts += len(lstChars)

        return sumOfCounts
    
    def part2(self):
        #P1 - Seperate into groups
        sumOfAllYes = 0
        group = []
        for line in self.inputData :
            if line :
                group.append(line)
            else : #Line is empty, treat group
                lstChars = []
                #Get all chars in groups
                for answer in group:
                    for i in range(len(answer)):
                        if not answer[i] in lstChars :
                            lstChars.append(answer[i])
                
                #Check if each char is in all answers, if so sum++
                for char in lstChars:
                    allYes = True
                    for answer in group:
                        if not char in answer:
                            allYes = False
                            break
                    
                    if allYes :
                        sumOfAllYes += 1

                #Reset group for next group
                group = []

        return sumOfAllYes