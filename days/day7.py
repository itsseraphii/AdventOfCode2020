from utils.aoc_utils import AOCDay, day

@day(7)
class Day7(AOCDay):
    def common(self):
        # Create a dictionnary with containing bag as key and
        # contains a dictionnary of contained bags with their amount
        self.rules = {}
        for bag in self.inputData:
            splitInput = bag.replace("bags", '').replace("bag", '').strip('.').split('contain')
            containerBag = splitInput[0].strip()

            ruleDict = {}

            for subBag in splitInput[1].split(','):
                subBag = subBag.strip()
                if subBag != "no other":
                    bagInfo = subBag.split(" ", 1)
                    bagName = bagInfo[1].strip()
                    bagAmount = bagInfo[0]
                    ruleDict[bagName] = int(bagAmount)

            self.rules[containerBag] = ruleDict
        return 0

    

    def part1(self):
        bagCounter = 0

        for bag in self.rules.keys():
            bagCounter += self.findBag(bag, 'shiny gold')

        return bagCounter

    # Recursive function that searches for a bag and returns
    # 1 if found, else 0 
    def findBag(self, key, searchedBag):
        found = False
        for bag in self.rules[key]:
            if bag == searchedBag:
                return 1
            else:
                if self.findBag(bag, searchedBag) == 1 :
                    found = True
                    break
                
        if found :
            return 1
        else :
            return 0
    
    def part2(self):
        return self.countSubBags("shiny gold")

    def countSubBags(self, containerBag):
        totalBags = 0
        for bag in self.rules[containerBag]:
            nbBags = self.rules[containerBag].get(bag)
            totalBags += nbBags + nbBags * self.countSubBags(bag)
        return totalBags
