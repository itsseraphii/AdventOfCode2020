from utils.aoc_utils import AOCDay, day

@day(14)
class Day14(AOCDay):
    def common(self):
        return 0

    def part1(self):
        crntMask = (420, 69) # Haha funny number
        dictMem = {}
        for line in self.inputData:
            # sort if set mask or data manip
            if line[:3] == 'mem' :
                value = int(line.split('=')[1][1:])
                memAddress = int(line[4:].split(']')[0])

                # Turn value into 36 bit array
                binStrVal = str(bin(value))[2:][::-1]

                # Make value exactly 36 chars long
                sentVal = list(binStrVal)

                for i in range(len(sentVal), 36) : sentVal.append('0')

                #Mask the value with current mask
                for tup in crntMask:
                    sentVal[tup[0]] = tup[1]

                # Reverse, turn to decimal number and write to memory address
                binStrVal = ""
                dictMem[memAddress] = int(binStrVal.join(sentVal)[::-1],2)

            else : #Set mask
                # [::-1] reverses the string, better suited for manips with forloop (its 1am aaaa)
                newmask = line[7:][::-1]
                crntMask = []
                # Make list of tuples for positions where
                # data can't go through
                # (position (2^pos), value)
                for i in range(len(newmask)):
                    if newmask[i] != 'X':
                        crntMask.append((i, newmask[i]))

        total = 0
        # Get total in memory
        for value in dictMem.values() : total += value

        return total
    
    def part2(self):
        return 0