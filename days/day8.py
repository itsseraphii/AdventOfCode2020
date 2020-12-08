from utils.aoc_utils import AOCDay, day

@day(8)
class Day8(AOCDay):
    def common(self):
        # Key of dictionnary is the line #
        # Returns operation and argument through a dictionnary
        self.dictInstructions = {}
        lineNum = 0

        for line in self.inputData :
            values = line.split(' ')
            
            dictInstr = {
                "op" : values[0],
                "arg" : int(values[1])
            }

            self.dictInstructions[lineNum] = dictInstr
            lineNum += 1

        return 0

    def part1(self):
        # TLDR Run operations until one is executed twice
        accu = 0
        executedSet = set() #Holds lineNb of executed instructions
        i = 0
        while i not in executedSet:
            executedSet.add(i)

            if self.dictInstructions[i].get("op") == "jmp":
                i += self.dictInstructions[i].get("arg")
            else:
                if self.dictInstructions[i].get("op") == "acc":
                    accu += self.dictInstructions[i].get("arg")
                i += 1

        return accu
    
    def part2(self):
        
        terminateVal = 0

        # Search for corrupted instruction 
        for index in self.dictInstructions.keys():
            if self.dictInstructions[index].get("op") == "acc":
                continue
            elif self.dictInstructions[index].get("op") == "jmp":
                newOp = "nop"
            else :
                newOp = "jmp"

            newInstruction = {
                "op": newOp,
                "arg": self.dictInstructions[index].get("arg")
            }

            #Loop program with replaced instruction
            accu = 0
            executedSet = set() #Holds lineNb of executed instructions
            executedSet.add(-1)
            i = 0

            while i not in executedSet and i < len(self.dictInstructions):
                executedSet.add(i)
                #Run program with replaced instruction
                if i == index :
                    executedInst = newInstruction
                else :
                    executedInst = self.dictInstructions[i]

                if executedInst.get("op") == "jmp":
                    i += executedInst.get("arg")
                else:
                    if executedInst.get("op") == "acc":
                        accu += executedInst.get("arg")
                    i += 1

                #End of code reached, replaced instruction was corrupted
                if i >= len(self.dictInstructions) :
                    i = -1

            # End of code reached
            if i == -1 :
                terminateVal = accu
                print("Corrupted instruction at line : ", index)
                break

        return terminateVal