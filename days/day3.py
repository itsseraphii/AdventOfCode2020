from utils.aoc_utils import AOCDay, day

@day(3)
class Day3(AOCDay):
    def common(self):
        return 0

    def part1(self):
        nbTrees = 0
        xDistance = 0 #Start position of toboggan 

        for line in self.inputData:
            char = line[xDistance%len(line)]

            if char == '#' : 
                nbTrees+=1 #tree hit!

            #Move right for next line
            xDistance+=3

        return nbTrees
    
    def part2(self):
        #Dictionary with the values of each slope (right, down)
        dictSlopes = {
            "slope1" : {"right" : 1, "down" : 1},
            "slope2" : {"right" : 3, "down" : 1},
            "slope3" : {"right" : 5, "down" : 1},
            "slope4" : {"right" : 7, "down" : 1},
            "slope5" : {"right" : 1, "down" : 2}
        }

        nbTrees = 0
        for slope in dictSlopes :
            xDistance = 0
            slopeTrees = 0

            for i in range(0, len(self.inputData), dictSlopes[slope].get("down")):
                line = self.inputData[i]
                char = line[xDistance % len(self.inputData[i])]

                if char == '#' : 
                    slopeTrees+=1 #tree hit!

                xDistance+=dictSlopes[slope].get("right")

            if nbTrees == 0 :
                nbTrees+=slopeTrees
            else : 
                nbTrees *= slopeTrees

        return nbTrees