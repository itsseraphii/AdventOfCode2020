from utils.aoc_utils import AOCDay, day
import re

@day(4)
class Day4(AOCDay):
    def common(self):
        buffer = ""
        self.parsedInput = []

        # Opening filestream
        file = open(self.inputPath, "r")

        self.inputData = []
        # Reading and appending each line to the inputData
        for line in file:
            line = line.replace('\n', '')
            self.inputData.append(line)

        # Add empty line at the end of the file
        self.inputData.append('')

        # Closing filestream
        file.close()

        # Put 1 passport per line
        for line in self.inputData :
            if not line :
                if buffer != "":
                    self.parsedInput.append(buffer)
                    buffer = ""

            elif buffer == "":
                buffer = line
                
            else:
                buffer += " " + line

        self.lstPassports = []
        for line in self.parsedInput :
            fields = line.split(' ')
            if len(fields) >= 7 :
                dictPassport = {}
                nbFields = 0
                for field in fields :
                    values = field.split(':')
                    if values[0] != "cid" :
                        nbFields += 1
                    
                    # Add key value pair
                    dictPassport[values[0]] = values[1]
                
                # All valid fields are in the dict
                if nbFields >= 7 :
                    self.lstPassports.append(dictPassport)

        return 0

    def part1(self):
        return len(self.lstPassports)
    
    def part2(self):
        validPassports = 0
        possibleEclVals = ["amb", "blu", "brn", "gry","grn", "hzl", "oth"]

        for passport in self.lstPassports :
            valid = True
            for key in passport.keys() :
                if key == "byr":
                    if int(passport[key]) < 1920 or int(passport[key]) > 2002:
                        valid = False
                elif key == "iyr":
                    if int(passport[key]) < 2010 or int(passport[key]) > 2020:
                        valid = False
                elif key == "eyr":
                    if int(passport[key]) < 2020 or int(passport[key]) > 2030:
                        valid = False
                elif key == "hgt":
                    if "cm" in passport[key] :
                        value = passport[key][:-2]
                        if int(value) < 150 or int(value) > 193:
                            valid = False
                    elif "in" in passport[key] :
                        value = passport[key][:-2]
                        if int(value) < 59 or int(value) > 76:
                            valid = False
                    else:
                        valid = False
                elif key == "hcl":
                    if not re.search("^#[0-9a-f]{6}$", passport[key]):
                        valid = False
                elif key == "ecl":
                    if not passport[key] in possibleEclVals :
                        valid = False
                elif key == "pid":
                     if not re.search("^[0-9]{9}$", passport[key]):
                        valid = False

            if valid :
                validPassports += 1

        return validPassports