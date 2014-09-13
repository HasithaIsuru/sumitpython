import sys
from numpy import *
from time import *

class Square :
    def __init__(self):
        self.listOfIndex = []
        self.listOfUnfilledSlots = []

    def addCoord(self, x, y):
        self.listOfIndex.append((x,y))

    def printCoordList(self):
        print self.listOfIndex

    def getCoordList(self):
        return self.listOfIndex

    def generateUnFilledSlots(self, fixdList):
        self.listOfUnfilledSlots = set(self.listOfIndex).difference(fixdList)

    def getUnFilledSlots(self):
        return self.listOfUnfilledSlots

def findFixedPositions(data):
    pos = []
    for x in range(GRIDSIZEX):
        for y in range(GRIDSIZEY):
            if (data[x,y] != -1):
                pos.append((x,y))
    return pos

def createAllSquares(sq, fixed):
    for x in range(GRIDSIZEX):
        for y in range(GRIDSIZEY):
            squareIndex_X = x / 3
            squareIndex_Y = y / 3
            sq[squareIndex_X][squareIndex_Y].addCoord(x,y)

    for x in range(GRIDSIZEX):
        for y in range(GRIDSIZEY):
            squareIndex_X = x / 3
            squareIndex_Y = y / 3
            sq[squareIndex_X][squareIndex_Y].generateUnFilledSlots(fixed)

def getMissingCoordinatesInSq(sq):
    coord = sq.getCoordList()
    allMissingCoord = []

    coord = sq.getCoordList()
    for (x,y) in coord:
        number = grid[x,y]
        if (number == -1) :
            allMissingCoord.append((x,y))
    return allMissingCoord

def getMissingNumbersInSq(sq):
    allNum = [x for x in range(1, 10)]
    coord = sq.getCoordList()
    for (x,y) in coord:
        number = grid[x,y]
        if (number != -1) :
            allNum[number-1] = 0
    return allNum

def initializeSquare(sq):
    missingNum = getMissingNumbersInSq(sq)
    missingCoord = getMissingCoordinatesInSq(sq)

    while (len(missingCoord) != 0):
        while True:
            randomIndexInMissingNumList = random.randint(0, len(missingNum))
            if ( missingNum[randomIndexInMissingNumList] != 0):
                break

        randomIndexInMissingCoord = random.randint(0, len(missingCoord))
        m,n = missingCoord[randomIndexInMissingCoord]
        grid[m,n] = missingNum[randomIndexInMissingNumList]
        missingNum[randomIndexInMissingNumList] = 0
        missingCoord.remove((m,n))

def initializeAllSquares():
    for x in range(3):
        for y in range(3):
            initializeSquare(squares[x][y])


def getCurrentCost():
    missingAcrossRows = []
    missingAcrossCols = []
    for i in range(0, GRIDSIZEY):
        missingInRow = ((grid[i]).shape[1]) - len(unique(array(grid[i])))
        missingAcrossRows.append(missingInRow )
        missingInCol = ((grid[:,i]).shape[0]) - len(unique(array(grid[:,i])))
        missingAcrossCols.append(missingInCol)
    rowSum = 0

    colSum = 0
    for i in missingAcrossRows:
        rowSum += i
    for i in missingAcrossCols:
        colSum += i
    return colSum + rowSum

def getCoord(x,y, tileNum):
    rowNum = 3*x + tileNum / 3
    colNum = 3*y + tileNum % 3
    return (rowNum, colNum)

def swap(x,y):      # Square Number (0,0)  to (3,3) -- since there are 9 squares
    # number of unfulfilled Slots
    unFilled = squares[x][y].getUnFilledSlots()
    num = len(unFilled)
    tile1 = random.randint(0,num)
    tile2 = random.randint(0,num)
    unFilledList = list(unFilled)
    return unFilledList[tile1], unFilledList[tile2]

def blank_if_negative(x):
	if x < 0:
		return ' '
	return x


GRIDSIZEX = 9
GRIDSIZEY = 9

row= []

missingAcrossRows = []
missingAcrossCols = []

alpha = .949999          # Cooling Factor -- newTemp = alpha * initialTemp

for i in range(1, len(sys.argv)):
    row.append(int(sys.argv[i]))

temp = matrix(row)
minCost = 50
minGrid = temp.reshape((GRIDSIZEX,GRIDSIZEY))
minAlpha = 1

# grid has the actual data at any current time
grid = temp.reshape((GRIDSIZEX,GRIDSIZEY))

fixedPositions = findFixedPositions(grid)

squares = [[Square() for x in xrange(3)] for x  in xrange(3)]
createAllSquares(squares, fixedPositions)

print "Starting Board Input"
print "====================\n"
zz = [blank_if_negative(x) for x in row]
b = matrix(zz)
board = b.reshape((GRIDSIZEX,GRIDSIZEY))
print `board`

initializeAllSquares()
currentCost = getCurrentCost()
#print currentCost

currentTemp = initialTemp = 1.8

# alpha should be between - 0 and 1 -- we will start with Alpha= 0.9 -- this will need experimentation

# Number of iterations when we do not reduce the temperature
M = len(fixedPositions) * len(fixedPositions)
N = 100    # Number of Markov Chains

for i in range(N):
    for i in range(M):
        # choose a Square which we want to swap the tiles ( Squares are numbered from 1 - 9 ) row major
        sqNumber = random.randint(1,9)
        x = (sqNumber-1) / 3
        y = (sqNumber-1) % 3
        coord1, coord2 = swap(x, y)     ## we choose the Sq - and then within the sq - 2 non fixed points are chosen for swapping
        x1,y1 = coord1[0], coord1[1]
        x2,y2 = coord2[0], coord2[1]

        #print "swapping Square (" + `x` + ", " + `y` + ") Locations (" + `x1` + ", " + `y1` + ") with (" + `x2` + ",  " + `y2` + ")"
        grid[x1, y1], grid[x2, y2] = grid[x2, y2], grid[x1, y1]

        #print grid
        newCost = getCurrentCost()
        #print "1 Iteration of Swapping Done - New Cost = "  + `newCost`

        if (newCost == 0):
            print "Found Solution\n\n"
            print grid
            sys.exit
        else:
            randomNumber = random.random(1)
            exponentNumber = exp([(currentCost - newCost)/(float(currentTemp))])
            if (newCost < currentCost) or (randomNumber < exponentNumber):
                currentCost = newCost
                if currentCost < minCost:
                    minCost = currentCost
                    minGrid = grid
                    minAlpha = alpha

            else:   # Undo the swap
                grid[x1, y1], grid[x2, y2] = grid[x2, y2], grid[x1, y1]

    newTemp = alpha * currentTemp
    currentTemp = newTemp

    # reHeat the process
    # using the current Grid Position
 #       currentTemp = 100

print "No Solution Found"
print "Number of Digits in Misplaced Positions " + repr(minCost)
print "Best possible solution after Simulated Annealing\n\n" + repr(minGrid)
