from utils.aoc_utils import AOCDay, day

@day(2)
class Day2(AOCDay):
    def common(self):
        #Dictionnary with parsed dictionnaries
        self.dictInput = {}

        for i in range(len(self.inputData)):
            #Dictionnary of the parsed line
            line = {
                "minVal" : 0,
                "maxVal" : 0,
                "password" : "",
                "char" : ""
            }
            #Set password in the dictionnary
            result = self.inputData[i].split(':')
            line["password"] = result[1]

            params = result[0]
            result = params.split(' ')
            line["char"] = result[1]

            result = result[0].split('-')
            line["minVal"] = int(result[0])
            line["maxVal"] = int(result[1])

            # Add dictionnary to dict accessible by solution code
            self.dictInput[i] = line

    def part1(self):
        validCounter = 0
        for i in range(len(self.inputData)):
            numChars = self.dictInput[i].get("password").count(self.dictInput[i].get("char"))

            if numChars >= self.dictInput[i].get("minVal") and numChars <= self.dictInput[i].get("maxVal") :
                validCounter+=1

        return validCounter
    
    def part2(self):
        validCounter = 0
        for i in range(len(self.inputData)):
            valOne = self.dictInput[i].get("password")[self.dictInput[i].get("minVal")]
            valTwo = self.dictInput[i].get("password")[self.dictInput[i].get("maxVal")]

            numChars = (valOne + valTwo).count(self.dictInput[i].get("char"))
            if numChars == 1 : validCounter += 1

        return validCounter