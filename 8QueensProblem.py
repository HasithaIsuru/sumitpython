import sys
GRIDSIZE = 8
threatMatrix = []

def resetMoveDictExceptTopRow():
    for keys in moveDict.iterkeys():
        if keys != 1:
            moveDict[keys] = None


def printAt(row, col, ch):
	if row > GRIDSIZE or col > GRIDSIZE:
		return
	if row <= 0 or col <= 0:
		return
	for i in range(1,GRIDSIZE+1):
		for y in range(1,GRIDSIZE+1):
			if ( i == row and y == col):
				print ch + " ",
			else:
				print "- ",
		print("")  # new line


def printEmptyBoard():
	for i in range(1,GRIDSIZE+1):
		for y in range(1,GRIDSIZE+1):
			print "- ",
		print("")  # new line

def getQueenMovesFrom(row, col):
	validMoves = []
#	print "getQueenMovesFrom " + str(row) + ", " + str(col)
	for i in range(1,GRIDSIZE+1):
		validMoves.append((i,col))
	for i in range(1,GRIDSIZE+1):
		validMoves.append((row,i))
	#print "getQueenMovesFrom " + str(validMoves)
	currentRow = row
	currentCol = col
	while currentRow != 1 and currentCol != 1:
		validMoves.append((currentRow-1,currentCol-1))
		currentRow -= 1
		currentCol -= 1
#	print "getQueenMovesFrom " + str(validMoves)
	currentRow = row
	currentCol = col
	while currentRow < GRIDSIZE and currentCol < GRIDSIZE:
		validMoves.append((currentRow+1,currentCol+1))
		currentRow += 1
		currentCol += 1
	currentRow = row
	currentCol = col
	while currentRow < GRIDSIZE and currentCol != 1 :
		validMoves.append((currentRow+1,currentCol-1))
		currentRow += 1
		currentCol -= 1
	currentRow = row
	currentCol = col
	while currentRow != 1  and currentCol < GRIDSIZE :
		validMoves.append((currentRow-1,currentCol+1))
		currentRow -= 1
		currentCol += 1


	return validMoves

def showPossibleQueenMoves(row, col):
	moves = getQueenMovesFrom(row, col)
	for i in range(1,GRIDSIZE+1):
		for y in range(1,GRIDSIZE+1):
			if ( i == row and y == col):
				print "Q ",
			elif (i,y) in moves:
				print "q ",
			else :
				print "- ",
		print("")  # new line


def getAllNonAttackingMoves():
	threatened = []

def initializeThreatMatrix():
#	l = []
#	for j in range(1, GRIDSIZE+1):
#		l.append(0)
	#print l
    #threatMatrix = []
    for i in range(1, GRIDSIZE+1):
		l = []
		for j in range(1, GRIDSIZE+1):
			l.append(0)
		threatMatrix.append(l)

def printThreatMatrix():
	for i in range(0, GRIDSIZE):
#		for j in range(0, GRIDSIZE):
		print str(threatMatrix[i])
		print ""

def getPossibleMovesInRow(row):
	rowThreats = threatMatrix[row-1]
	rowMoves = []
	for col in range(0,GRIDSIZE):
		if threatMatrix[row-1][col] == 0:
			rowMoves.append(col+1)
	return rowMoves


def setThreatMatrix(row, col, v):
	threatMatrix[row-1][col-1] = v

def updateThreatMatrix(listOfThreats, v, row, col):
	updatedList = []
	for threat in listOfThreats:
		#print threat
		r = threat[0]
		c = threat[1]
		if ( v == 1 ):
			if ( threatMatrix[r-1][c-1] != 1 ):
				threatMatrix[r-1][c-1] = v
				updatedList.append((r,c))
		else:
			threatMatrix[r-1][c-1] = 0
		#printThreatMatrix()
	threatMatrix[row-1][col-1] = v
	return updatedList


def resetAllMovesForRowsBelow(dict, rowCount):
#	print "calling resetMovesForRowsBelow " + str(rowCount)
	for i in range(rowCount+1,GRIDSIZE+1):
		if dict.get(i) != None:
			dict[i] = None


def allMovesTested():
    for k in moveDict.keys():
        if moveDict[k]==None:
            continue
        else:
            return False
    return True

def inMoves(r,c,moves):
    for x,y in moves:
        if x == r and y == c:
            return True
    return False

def printQueen(moves):
	for x in range(1,GRIDSIZE+1):
		for y in range(1,GRIDSIZE+1):
			if ( inMoves(x,y,moves)):
				print "Q ",
			else:
				print "- ",
		print("")  # new line


GRIDSIZE = int(sys.argv[1])
#print GRIDSIZE
#printEmptyBoard()
#print "------------"
moves = []
#for i in range(1,9):
##		moves.append(len(getQueenMovesFrom(i, j)))
#print sorted(moves)
#showPossibleQueenMoves(1,1)
#print '------'
#showPossibleQueenMoves(2,3)
initializeThreatMatrix()
#printThreatMatrix()
#setThreatMatrix(0,0)
#setThreatMatrix(0,1)
#setThreatMatrix(0,2)
#print getPossibleMovesInRow(0)
moveDict = {}
rowCount = 1
updatedCoordinatesDict = {}

while True:
#    while rowCount < GRIDSIZE+1 and numOfTries < GRIDSIZE*GRIDSIZE:
    while rowCount < GRIDSIZE+1:
        allowableMovesOnThisRow = moveDict.get(rowCount)
    #	print 'Before allowableMovesOnThisRow[' + str(rowCount) + "] = " + str(allowableMovesOnThisRow)
        if allowableMovesOnThisRow == None:
    		allowableMovesOnThisRow  = getPossibleMovesInRow(rowCount)
    #	print 'After allowableMovesOnThisRow[' + str(rowCount) + "] = " + str(allowableMovesOnThisRow)
        if ( len(allowableMovesOnThisRow) != 0 ):
    		moveDict[rowCount] = allowableMovesOnThisRow
    		#print moveDict[rowCount]
    		currentMove = (rowCount,moveDict[rowCount].pop())
    #		print currentMove
    		currRow = rowCount
    		currCol = currentMove[1]
    		listOfThreats = getQueenMovesFrom(rowCount, currCol)
    #		print "List Of Threats " + str(listOfThreats)
    		#showPossibleQueenMoves(rowCount, currCol)
    		#printThreatMatrix()
    		#print moveDict[i]
    		if len(listOfThreats) > 0:
    			updatedCoordinates = updateThreatMatrix(listOfThreats, 1, rowCount, currCol)
    			updatedCoordinatesDict[currentMove] = updatedCoordinates
    			rowCount += 1
    			moves.append(currentMove)
    #		printThreatMatrix()
        else:
            moveDict[rowCount] = None
            if (len(moves) != 0):
                #print rowCount
                lastMove = moves.pop()
                lastMoveRow = lastMove[0]
                lastMoveCol = lastMove[1]
                resetAllMovesForRowsBelow(moveDict, rowCount)
                rowCount -= 1
                listOfThreatsToUndo = updatedCoordinatesDict.get(lastMove)
                #moveDict[rowCount] =
                updateThreatMatrix(listOfThreatsToUndo, 0, lastMoveRow, lastMoveCol)
            #		printThreatMatrix()
        if (len(moves) == GRIDSIZE):
            print "Possible Location = " + str(moves)
            printQueen(moves)

        if (allMovesTested()):
            break

    if (rowCount == GRIDSIZE+1):
        if(len(moveDict[1]) != 0):
            rowCount = 1
            updatedCoordinatesDict = {}
            threatMatrix = []
            moves = []
            initializeThreatMatrix()
            resetMoveDictExceptTopRow()
            continue
        else:
            break
    else:
        break

