import sys
SIZE = 8
def printKnightAt(row, col):
	if row > SIZE or col > SIZE:
		return
	if row <= 0 or col <= 0:
		return
	for i in range(1,SIZE+1):
		for y in range(1,SIZE+1):
			if ( i == row and y == col):
				print "K ",
			else:
				print "- ",
		print("")  # new line


def printEmptyBoard():
	for i in range(1,SIZE+1):
		for y in range(1,SIZE+1):
			print "- ",
		print("")  # new line

def getKnightMovesFrom(row, col):
	validMoves = []
	
	if ( row + 2 <= SIZE ):
		#row+2, col+1
		if ( col + 1 <= SIZE ):
			tup = (row+2, col+1)
			validMoves.append(tup)
		#row+2, col-1
		if ( col - 1 >= 1 ):
			tup = (row+2, col-1)
			validMoves.append(tup)
	if ( row - 2 >= 1 ):
		#row-2, col+1
		if ( col + 1 <= SIZE ):
			tup = (row-2, col+1)
			validMoves.append(tup)
		#row-2, col-1
		if ( col - 1 >= 1 ):
			tup = (row-2, col-1)
			validMoves.append(tup)
	if ( row + 1 <= SIZE ):
		#row+1, col+2
		if ( col + 2 <= SIZE ):
			tup = (row+1, col+2)
			validMoves.append(tup)
		#row+1, col-2
		if ( col - 2 >= 1 ):
			tup = (row+1, col-2)
			validMoves.append(tup)
	if ( row - 1 >= 1 ):
		#row-1, col+2
		if ( col + 2 <= SIZE ):
			tup = (row-1, col+2)
			validMoves.append(tup)
		#row-1, col-2
		if ( col - 2 >= 1 ):
			tup = (row-1, col-2)
			validMoves.append(tup)
	return validMoves

def getKnightMovesFromIfNotVisited(visitedList, row, col):
#	print "Calling getMovesIfNotVisited For : " + str(row) + ", " + str(col)
	validMoves = getKnightMovesFrom(row, col)
#	print validMoves
	newValidMoves  = []
#	print "ValidMoves in getMovesIfNotVisited : " + str(validMoves)
	for currentMove in validMoves:
#		print "Current location = " + str(currentMove)
#		printArray(visitedArr)
#		print ""
		if ( currentMove not in visitedList ):
			currentRow = currentMove[0]
			currentCol = currentMove[1]
			newValidMoves.append(currentMove)
		
	return newValidMoves

def showPossibleKnightMoves(row, col):
	moves = getKnightMovesFrom(row, col)
	print repr(moves)
	for i in range(1,SIZE+1):
		for y in range(1,SIZE+1):
			if ( i == row and y == col):
				print "K ",
			elif (i,y) in moves:
				print "k ",
			else :
				print "- ",
		print("")  # new line
	
def doKnightTour(row, col):
	listOfMoves = {}
	tour = []
	moves = getKnightMovesFromIfNotVisited(listOfMoves.keys(), row, col)
	currentRow = row
	currentCol = col
	if len(moves) != 0:
		listOfMoves[(row, col)] = moves
		tour.append((currentRow, currentCol))
	while len(tour) != SIZE*SIZE:
		print "currentRow, currentCol : " + str(currentRow) + ", " + str(currentCol) + " Moves = " + str(listOfMoves[(currentRow, currentCol)])
		if len(listOfMoves[(currentRow, currentCol)]) != 0:
			while len(listOfMoves[(currentRow, currentCol)]) > 0:
#				print len(listOfMoves[(currentRow, currentCol)])
				tryingCurrent = listOfMoves[(currentRow, currentCol)].pop()
#				print len(listOfMoves[(currentRow, currentCol)])
				tryingCurrentRow, tryingCurrentCol = tryingCurrent[0], tryingCurrent[1]
				moves = getKnightMovesFromIfNotVisited(listOfMoves.keys(), tryingCurrentRow, tryingCurrentCol)
				print "Moves from tryingCurrentRow, tryingCurrentCol : " + str(tryingCurrentRow) + ", " + str(tryingCurrentCol) + " = " + str(moves)
				if len(moves) != 0:
					listOfMoves[(tryingCurrentRow, tryingCurrentCol)] = moves
					currentRow = tryingCurrentRow
					currentCol = tryingCurrentCol
					tour.append((currentRow, currentCol))
					break;
				else:
					if(len(tour) == SIZE*SIZE-1) and (tryingCurrent not in tour):
						tour.append(tryingCurrent)
						print "Found Tour : " + str(tour)
						return tour;
		else:	
			del listOfMoves[(currentRow, currentCol)]
			#tour.remove((currentRow, currentCol))
			print "Tour Length = " + str(len(tour))
			print "Tour  = " + str(tour)
			tour.pop()
			if ( len(tour) > 0 ):
				nextMove = tour[-1]	# last one
				print "nextMove" + str(nextMove)
				currentRow,	currentCol = nextMove[0], nextMove[1]
			else:
				print "No Tour Found"
				break
	#print tour
	
def printArray(a):
	for x in range(len(a)):
		print a[x]
		
def isVisited(ar, r, c):
	if ar[r][c] == 1:	
		return True
	return False
	
def isAllVisited(arr):
	for i in range(0,SIZE):
		for j in range(0,SIZE):
			if arr[i][i] != 1:
				return False
	return True

		
#printEmptyBoard()
print "------------"
#printKnightAt(2,3)
#showPossibleKnightMoves(2,7)
#showPossibleKnightMoves(6,7)
#showPossibleKnightMoves(7,6)
SIZE = int(sys.argv[1])
startRow = int(sys.argv[2])
startCol = int(sys.argv[3])
tour = doKnightTour(startRow,startCol)

if tour != None:
	for (row,col) in tour:
		printKnightAt(row,col)
		print
		print 
