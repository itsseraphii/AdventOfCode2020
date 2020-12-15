from utils.aoc_utils import AOCDay, day
import copy

@day(14)
class Day14(AOCDay):
    def common(self):
        return 0

    def part1(self):
        return self.getTotalEmulator(1)
    
    def part2(self):
        return self.getTotalEmulator(2)

    def getTotalEmulator(self, version) :
        crntMask = (420, 69) # Haha funny number
        dictMem = {}
        for line in self.inputData:
            # sort if set mask or data manip
            if line[:3] == 'mem' :

                value = int(line.split('=')[1][1:])
                memAddress = int(line[4:].split(']')[0])
                if version == 1 :
                    newValue = self.getValue(crntMask, value)
                    dictMem[memAddress] = newValue
                else :
                    for address in self.getMaskAddresses(crntMask, memAddress) :
                        dictMem[address] = value

            else : #Set mask
                # [::-1] reverses the string, better suited for manips with forloop (its 1am aaaa)
                newmask = line[7:][::-1]
                crntMask = []
                # Make list of tuples for positions where
                # data can't go through
                # (position (2^pos), value)
                for i in range(len(newmask)):
                    crntMask.append((i, newmask[i]))

        total = 0
        # Get total in memory
        for value in dictMem.values() : total += value
        return total

    def getMaskAddresses(self, mask, address) :
        # P1 : Mask address
        binAddress = self.makeBinaryArray(address, 36)

        #Mask the address with current mask
        for tup in mask:
            if tup[1] == '1' :
                binAddress[tup[0]] = '1'
            elif tup[1] == 'X' :
                binAddress[tup[0]] = 'X'
        
        # P2 Get all possible addresses with floating points
        nbPos = 2**binAddress.count('X') 
        memAddresses = []

        for i in range(nbPos) :
            # Copy binary address
            tempAdrs = copy.copy(binAddress)

            #Turn i into reversed binary address
            for val in self.makeBinaryArray(i, binAddress.count('X')):
                #Replace first X found, does this for all X
                tempAdrs[tempAdrs.index('X')] = val

            memAddresses.append(self.binaryToInt(tempAdrs))

        return memAddresses

    def makeBinaryArray(self, value, numOfZeros):
        binStrVal = str(bin(value))[2:][::-1]

        sentVal = list(binStrVal)

        for i in range(len(sentVal), numOfZeros) : sentVal.append('0')
        return sentVal


    def binaryToInt(self, binArray) :
        binStrVal = ""
        return int(binStrVal.join(binArray)[::-1],2)

    def getValue(self, mask, value):
        sentVal = self.makeBinaryArray(value, 36)

        #Mask the value with current mask
        for tup in mask:
            if (tup[1] != 'X') :
                sentVal[tup[0]] = tup[1]

        # Reverse, turn to decimal number and write to memory address
        return self.binaryToInt(sentVal)
        
