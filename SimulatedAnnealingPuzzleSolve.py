import sys
import numpy
from numpy import random

class PuzzlePiece :
    def __init__(self, locX, locY):
        self.x = locX
        self.y = locY
        self.allocateRandomColors()

    def getColors(self):
        return (self.top, self.rhs, self.bottom, self.lhs)

    def setColors(self, tup):
        self.top, self.rhs, self.bottom, self.lhs = tup[0],tup[1],tup[2],tup[3]

    def allocateRandomColors(self):
        l =[]
        self.top = self.generaterandomNotIn(l)
        l.append(self.top)
        self.rhs = self.generaterandomNotIn(l)
        l.append(self.rhs)
        self.bottom = self.generaterandomNotIn(l)
        l.append(self.bottom)
        self.lhs = self.generaterandomNotIn(l)


    def generaterandomNotIn(self, l):
        while(1):
            num = random.randint(4)
            if num not in l:
                return num

    def showPiece(self):
        print str(self.x) + ',' + str(self.y) + '-' + str(self.top) + '_' + str(self.rhs) + '_' + str(self.bottom) + '_' + str(self.lhs)

    def printPiece(self):
        return str(self.x) + ',' + str(self.y) + '-' + str(self.top) + '_' + str(self.rhs) + '_' + str(self.bottom) + '_' + str(self.lhs)




def getNeighbours(i,j):
    if (isTopLeft(i,j)):
        return [(i+1,j),(i,j+1)]
    elif (isTopRight(i,j)):
        return [(i,j-1), (i+1,j)]
    elif (isBottomLeft(i,j)):
        return [(i,j+1), (i-1,j)]
    elif (isBottomRight(i,j)):
        return [(i-1,j), (i,j-1)]
    elif (isTopBoundaryrRow(i,j)):
        return [(i+1,j), (i,j+1), (i,j-1)]
    elif (isBottomBoundaryrRow(i,j)):
        return [(i-1,j), (i,j+1), (i,j-1)]
    elif (isLeftBoundaryrRow(i,j)):
        return [(i+1,j), (i,j+1), (i-1, j)]
    elif (isRightBoundaryrRow(i,j)):
        return [(i,j-1), (i-1,j), (i+1,j)]
    else:
        return [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]

def isTopLeft(x,y):
        return(x==0 and y==0)
def isTopRight(x,y):
        return(x==0 and y==GRIDSIZEY-1)
def isBottomLeft(x,y):
        return(x==GRIDSIZEX-1 and y==0)
def isBottomRight(x,y):
    return(x==GRIDSIZEX-1 and y==GRIDSIZEY-1)
def isTopBoundaryrRow(i,j):
    return i==0
def isBottomBoundaryrRow(i,j):
    return i==GRIDSIZEX-1
def isLeftBoundaryrRow(i,j):
    return j==0
def isRightBoundaryrRow(i,j):
    return j==GRIDSIZEY-1

def CalculatePoints():
    point = 0
    for i in range(GRIDSIZEX):
        for j in range(GRIDSIZEY):
            point += getPointsAroundAPiece(i,j)
    return point/2


def getPointsAroundAPiece(i,j):
    k = (i,j)
    l = getNeighbours(i,j)
    piece = allPieces.get(k)
    points = 0

    #            Neighbour1 = allPieces.get(l[0])
    #            Neighbour2 = allPieces.get(l[1])
    #            print "Piece : " + str(k)
    #            print "Neighbours : " + str(l)
    #            print Neighbour1.showPiece()
    #            print Neighbour2.showPiece()
    for coord in l:
        neighbourPiece = allPieces.get(coord)
        #print coord
        p = CommonColors(piece, neighbourPiece)
        #print piece.printPiece() + " AND " + neighbourPiece.printPiece() + " POINT = " + str(p)
        points += p
    return points


def CommonColors(P1,P2):
    #print 'CommonColors'
    #P1.showPiece()
    #P2.showPiece()
    #print '---'
    count=0
    if (isTopLeft(P1.x, P1.y)):
        if (P1.y==P2.y) and (P1.bottom == P2.top):
            return 1
        elif (P1.x==P2.x) and (P1.rhs==P2.lhs):
            return 1
        else:
            return 0
    elif (isTopRight(P1.x, P1.y)):
        if (P1.y==P2.y) and (P1.bottom == P2.top):
            return 1
        elif (P1.x==P2.x) and (P1.lhs==P2.rhs):
            return 1
        else:
            return 0
    elif (isBottomLeft(P1.x, P1.y)):
        if (P1.y==P2.y) and (P1.top == P2.bottom):
            return 1
        elif (P1.x==P2.x) and (P1.rhs==P2.lhs):
            return 1
        else:
            return 0
    elif (isBottomRight(P1.x, P1.y)):
        if (P1.y==P2.y) and (P1.top == P2.bottom):
            return 1
        elif (P1.x==P2.x) and (P1.lhs==P2.rhs):
            return 1
        else:
            return 0
    elif (isTopBoundaryrRow(P1.x,P1.y)):
        if (P1.y==P2.y) and (P1.bottom==P2.top): return 1
        elif (P1.x==P2.x) and (P1.y==P2.y+1) and (P1.lhs==P2.rhs): return 1
        elif (P1.x==P2.x) and (P1.y+1==P2.y) and (P1.rhs==P2.lhs): return 1
        else: return 0
    elif (isBottomBoundaryrRow(P1.x,P1.y)):
        if (P1.y==P2.y) and (P1.top==P2.bottom): return 1
        elif(P1.x==P2.x) and (P1.y==P2.y+1)  and (P1.lhs==P2.rhs) : return 1
        elif(P1.x==P2.x) and (P1.y+1==P2.y) and (P1.rhs==P2.lhs) : return 1
        else: return 0
    elif (isLeftBoundaryrRow(P1.x,P1.y)):
        if(P1.y==P2.y) and (P1.x==P2.x+1 ) and (P1.top==P2.bottom): return 1
        elif(P1.y==P2.y) and (P1.x+1==P2.x) and (P1.bottom==P2.top): return 1
        elif(P1.x==P2.x) and (P1.rhs==P2.lhs):return 1
        else: return 0
    elif (isRightBoundaryrRow(P1.x,P1.y)):
        if(P1.y==P2.y) and (P1.x==P2.x+1) and (P1.top==P2.bottom): return 1
        elif(P1.y==P2.y) and (P1.x+1==P2.x) and (P1.bottom==P2.top): return 1
        elif(P1.x==P2.x) and (P1.lhs==P2.rhs): return 1
        else: return 0
    else:
        if(P1.x==P2.x) and (P1.y==P2.y+1) and (P1.lhs==P2.rhs): return 1
        elif(P1.x==P2.x) and (P1.y+1==P2.y) and (P1.rhs==P2.lhs): return 1
        elif(P1.y==P2.y) and (P1.x==P2.x+1) and (P1.top==P2.bottom): return 1
        elif(P1.y==P2.y) and (P1.x+1==P2.x) and (P1.bottom==P2.top): return 1
        else: return 0


def swapPieces(coord1X, coord1Y, coord2X, coord2Y):
    first = (coord1X, coord1Y)
    second = (coord2X, coord2Y)
    firstPiece = allPieces.get(first)
    secondPiece = allPieces.get(second)
    firstPieceColors = firstPiece.getColors()
    secondPieceColors = secondPiece.getColors()
    firstPiece.setColors(secondPieceColors)
    secondPiece.setColors(firstPieceColors)

def adjacent(firstX, firstY, secX, secY):
    if (firstX == secX) and (firstY == secY + 1): return True
    if (firstX == secX) and (secY == firstY + 1): return True

    if (firstY == secY) and (firstX+1 == secX ): return True
    if (firstY == secY) and (firstX == secX + 1): return True
    return False

def printAllPieces():
    for k in allPieces.keys():
        allPieces.get(k).showPiece()


def printAllPiecesInOrder():
    for x in range(0, GRIDSIZEX):
        rowList = []
        for y in range(0, GRIDSIZEY):
            rowList.append(allPieces.get((x,y)))
        topRow=[]
        middleRow=[]
        bottonRow=[]
        for i in rowList:
            topRow.append(i.top)
            middleRow.append((i.lhs, i.rhs))
            bottonRow.append(i.bottom)
        printTop(topRow)
        printMiddle(middleRow)
        printBottom(bottonRow)


print "Color Legend"
print "\x1B["+"31;94m" + "Blue" + "\x1B[" + "0m"
print "\x1B["+"31;92m" + "Green" + "\x1B[" + "0m"
print "\x1B["+"31;91m" + "Red" + "\x1B[" + "0m"
print "\x1B["+"31;90m" + "Brown" + "\x1B[" + "0m"


def lookup(i):
    if i==1: return "\x1B["+"31;91m" + "R" + "\x1B[" + "0m" #return 'R'
    if i==2: return "\x1B["+"31;94m" + "B" + "\x1B[" + "0m" #return 'B'
    if i==3: return "\x1B["+"31;92m" + "G" + "\x1B[" + "0m" #return 'Y'
    if i==0: return "\x1B["+"31;90m" + "Y" + "\x1B[" + "0m" #return 'G'

def printTop(row):
    for i in row:
        s = '-' + lookup(i) + '-'
        print(s),
def printMiddle(rowTuple):
    print
    for (l,r) in rowTuple:
        s = lookup(l)+ '-' + lookup(r)
        print(s),
def printBottom(row):
    print
    printTop(row)
    print
    print

def CalculateUsingSteepestAscent():
    currentPoints = CalculatePoints()
    print "Initial State " + `currentPoints`
    numberOfSwaps = 0
    tries = 0

    while (tries < tryCount):
        tries += 1
        # choose the 1st tile to replace
        firstX = random.randint(GRIDSIZEX)
        firstY = random.randint(GRIDSIZEY)

        # choose randomly the coordinate to replace the 1st tile with
        secX = random.randint(GRIDSIZEX)
        secY = random.randint(GRIDSIZEY)
        if ( firstX == secX) and (firstY==secY):
            continue
        first = (firstX,firstY)
        firtstNeighbour = getNeighbours(firstX,firstY)

        sec = (secX,secY)
        secNeighbour = getNeighbours(secX,secY)

        if not adjacent(firstX, firstY, secX, secY):
            removePoints = getPointsAroundAPiece(firstX, firstY) + getPointsAroundAPiece(secX, secY)
        else:
            removePoints = getPointsAroundAPiece(firstX, firstY) + getPointsAroundAPiece(secX, secY) - CommonColors(allPieces.get(first), allPieces.get(sec))

        swapPieces(firstX, firstY, secX, secY)
        if not adjacent(firstX, firstY, secX, secY):
            addPoints = getPointsAroundAPiece(firstX, firstY) + getPointsAroundAPiece(secX, secY)
        else:
            addPoints = getPointsAroundAPiece(firstX, firstY) + getPointsAroundAPiece(secX, secY) - CommonColors(allPieces.get(first), allPieces.get(sec))

        pointsAfterSwaps = currentPoints - removePoints + addPoints

        #print "After Swapping " + `first` + `sec` + " new score =  " + `pointsAfterSwaps`
        #print "After Swapping by calculation 1 - " + `CalculatePoints()`

        # if we are WEEE Close to the max - we are done - lets mark it done
        if ( abs(pointsAfterSwaps-maxPoints) == 2):
            return pointsAfterSwaps, numberOfSwaps

        # greedy strategy - if the NewPoint is > OlderPoint - Always go for it - GREEEEEEDY :-)
        if (pointsAfterSwaps >= currentPoints):
            currentPoints = pointsAfterSwaps
            numberOfSwaps += 1
            #print "Points after " + `numberOfSwaps` + " = " + `currentPoints`
            continue
        else:   # restore to prev state
            swapPieces(secX, secY,firstX, firstY)

    #print "Number of Tries = " + `tries`
    print "MaxScore Obtained Greedy Approach = " + `currentPoints` + "  Number of Swaps = " + `numberOfSwaps`
    return currentPoints, numberOfSwaps

def CalculateUsingGeneralizedSimualtedAnnealing():
    currentPoints = CalculatePoints()
    print "Initial State " + `currentPoints`
    numberOfSwaps = 0 # this is the temp as the number of swaps increases the probability of taking a swap - if the score decreases - also decreases
    maxScoreObtained = currentPoints
    tries = 0
    while (tries < tryCount):
        tries += 1
        firstX = random.randint(GRIDSIZEX)
        firstY = random.randint(GRIDSIZEY)

        secX = random.randint(GRIDSIZEX)
        secY = random.randint(GRIDSIZEY)
        if ( firstX == secX) and (firstY==secY):
            continue
        first = (firstX,firstY)
        firtstNeighbour = getNeighbours(firstX,firstY)

        sec = (secX,secY)
        secNeighbour = getNeighbours(secX,secY)

        if not adjacent(firstX, firstY, secX, secY):
            removePoints = getPointsAroundAPiece(firstX, firstY) + getPointsAroundAPiece(secX, secY)
        else:
            removePoints = getPointsAroundAPiece(firstX, firstY) + getPointsAroundAPiece(secX, secY) - CommonColors(allPieces.get(first), allPieces.get(sec))

        swapPieces(firstX, firstY, secX, secY)
        if not adjacent(firstX, firstY, secX, secY):
            addPoints = getPointsAroundAPiece(firstX, firstY) + getPointsAroundAPiece(secX, secY)
        else:
            addPoints = getPointsAroundAPiece(firstX, firstY) + getPointsAroundAPiece(secX, secY) - CommonColors(allPieces.get(first), allPieces.get(sec))

        pointsAfterSwaps = currentPoints - removePoints + addPoints

        #print "After Swapping " + `first` + `sec` + " new score =  " + `pointsAfterSwaps`
        #print "After Swapping by calculation 1 - " + `CalculatePoints()`

        # if we are WEEE Close to the max - we are done - lets mark it done
        if ( abs(pointsAfterSwaps-maxPoints) == 1):
            return pointsAfterSwaps, numberOfSwaps

        # If the swap results in a better state then of course take it
        if (pointsAfterSwaps >= currentPoints):
            currentPoints = pointsAfterSwaps
            numberOfSwaps += 1
            #print "Points after " + `numberOfSwaps` + " = " + `currentPoints`
            if currentPoints > maxScoreObtained:
                maxScoreObtained = currentPoints
            continue
        else: # come here if points have reduced after the swap
            # decide whether to take the swap or not - using how many swaps done, current points and pointsAfterSwap
            takeSwap = takeTheSwap(numberOfSwaps, currentPoints, pointsAfterSwaps)
            if (takeSwap):
                #print "Points prev, after Probability Calculation of Swaps = " + `currentPoints` +", " + `pointsAfterSwaps`
                currentPoints = pointsAfterSwaps
                numberOfSwaps += 1
                continue
            else:   # do not take the swap and hence restore the prev swap
                swapPieces(secX, secY,firstX, firstY)

    #print "Tries = " + `tries`
    print "MaxScore Obtained during the run = " + `currentPoints` + "  Number of Swaps = " + `numberOfSwaps`
    return currentPoints, numberOfSwaps

# We will improve on the heuristic here ( how do we measure that ) and add swapsDone ( as temperature count into consideration )
# This is applied only when the swap has resulted in decrease in the score

def takeTheSwap(swapsDone, currPoint, newPointAfterSwap):
    # if the state reduces a lot - then do not accept the swap
    #print "inside TakeSwap = " + `currPoint` +", " + `newPointAfterSwap` + ", " + `swapsDone`
##    if (currPoint-newPointAfterSwap > 3):   # when 2 tiles are swapped at most the score can increase / decrease by 8 points
##        return False
##    else:
    #decide =   # get a random float number
    if (swapsDone == 0):
        if (numpy.random.random_sample() < .5):
            return True
    elif (numpy.random.random_sample() > (1-swapsDone/tryCount)): # as the swapsDone increases over time the value  (1- swapsDone/tryCount) decreases
        return True
    return False;

# Program Parameters
# 1 - Grids in X Axis - int
# 2 - Grids in Y Axis - int
# 3 - Maximum number of tries after which the program terminates - int
# 4 - Mode of Simulated Annealing - "Greedy"  Or "any string" ( which means it is non greedy )

GRIDSIZEX = int(sys.argv[1])
GRIDSIZEY = int(sys.argv[2])
tryCount = int(sys.argv[3])
mode = str(sys.argv[4])


# Max surfaces that can match -- this is the max score that can  be obtained from the puzzle
maxPoints = ((GRIDSIZEX*GRIDSIZEY*4) - (2*GRIDSIZEY) -(2*GRIDSIZEX)) /2

print `tryCount`
# Generate Pieces
allPieces = {}
for i in range(GRIDSIZEX):
    for j in range(GRIDSIZEY):
        allPieces[(i,j)] = PuzzlePiece(i,j)

#printAllPieces()
print "Initial Pieces"

printAllPiecesInOrder()

print "Max Possible Score Possible for GridSize(" + `GRIDSIZEX` +"," + `GRIDSIZEY` +") = " + `maxPoints`

if mode == "Greedy":
    pts, tries = CalculateUsingSteepestAscent()
    print "Max achieved by Simulated Annealing with Steepest Ascent " + `pts`
else:
    pts, tries = CalculateUsingGeneralizedSimualtedAnnealing()
    print "Max achieved by Generalized Simulated Annealing " + `pts`

print "Current Max State After Generalized Simulated Annealing "
printAllPiecesInOrder()
