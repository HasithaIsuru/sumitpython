import sys

LEFT = 1
RIGHT = 2

def findIndexOfMax(ls):
	if len(ls) == 0:
		return -1
	elif len(ls) == 1:
		return 0, ls[0]	# index is 0 pos
	else:
		max = ls[0]
#		print 'Max ' + str(max)
#		print 'ls ' + str(ls)
		for i in ls[1:]:
			if i > max:
				max = i
		return ls.index(max), max

def getArea(ls, leftOrRight):
	#print "LS = " + str(ls)
	# we need a min of length 3 to accomodate water
	if len(ls) == 1:
		return 0
	if (len(ls) == 0):
		return 0
	if (len(ls) == 2):
		return 0

	if leftOrRight == LEFT:
		# last number is the max ( since that is how the array has been partitioned )
		max = ls[-1]	# last Number which is the max number in this array
		max2Index, max2 = findIndexOfMax(ls[:-1])	# except the last one - which we know is max
		maxIndex = len(ls)-1
		diff = abs((len(ls) - 1) - max2Index - 1)

		#print "Left : " + str(max2) + ", " + str(max) + " Diff = " + str(diff)
		#print "max2Index : " + str(max2Index) + ", max : " + str(len(ls)-1)
		if abs(maxIndex - maxIndex) == 1:	# if they are adjacent
			return getArea(ls[:max2Index+1], LEFT)
		else:
			val = diff*(min(max,max2))
			if maxIndex > max2Index:
				for i in range(max2Index+1,maxIndex):
					val = val - ls[i]
			else:
				for i in range(maxIndex+1,max2Index):
					val = val - ls[i]
			#print "Left Value : " + str(val)
			return val + getArea(ls[:max2Index+1], LEFT)

	else:		# Right side
		# 1st number is the max
		max = ls[0]
		maxIndex = 0
		max2Index, max2 = findIndexOfMax(ls[1:])
		max2Index += 1		# since in this ls[1:] - we have eliminate the 1st element which is the max
		diff = abs(max2Index-1)
		#print "Right max2Index : " + str(max2Index)
		#print "Right : " + str(max) + ", "  + str(max2) + " Diff = " + str(diff)
		if max2Index == 1: # Since max is the 1st element of the list
			return getArea(ls[max2Index:], RIGHT)
		else:
			val = diff*(min(max, max2) )
			for i in range(maxIndex+1,max2Index):
				val = val - ls[i]
			#print "Right Value : " + str(val)
			return val + getArea(ls[max2Index+1:], RIGHT)
	return


def get1st2Max(ls):
	max = max2 = -1
	if (len(ls) == 0):
		return max, max2
	elif (len(ls) == 1):
		max = max2 = ls[0]
		return max, max2
	else:
#		print ls[0]
#		print ls[1]
		if ls[0] > ls[1]:
			max = ls[0]
			max2 = ls[1]
		else:
			max2 = ls[0]
			max = ls[1]

		for item in ls[2:]:
			if ( item < max2 ):	 # do nothing
				continue
			elif (item < max):
				max2 = item
			else:
				max2 = max
				max = item

	return max, max2


#print len(sys.argv)
l = []
for v in sys.argv[1:]:
#	print v
	l.append(int(v))

max, max2 = get1st2Max(l)
#print max, max2

maxIndex = l.index(max)

# have to be careful if both max and max2 are the same numbers
if (max != max2 ):
	max2Index = l.index(max2)
else:
	for i in range(len(l)):
		if i != maxIndex:
			if l[i] == max:
				max2Index = i
				break

#print maxIndex, max2Index
area = 0
leftList = []
leftIndex = 0
rightList = []
rightIndex = 0

if ( maxIndex > max2Index ):
	leftList = l[:max2Index+1]
	leftIndex = max2Index+1
	rightList = l[maxIndex:]
	rightIndex = maxIndex
else:
	leftList = l[:maxIndex+1]
	leftIndex = maxIndex+1
	rightList = l[max2Index:]
	rightIndex = max2Index

#print leftList, leftIndex
#print rightList, rightIndex

# which means that the 1st max and 2nd max are not adjacent
if abs(maxIndex-max2Index) != 1:
	val = (abs(maxIndex-max2Index) - 1)* min(max,max2)  # max2 is the min of max1 and max2
	#print "In Main Value : " + str(val)
	if maxIndex > max2Index:
		for i in range(max2Index+1,maxIndex):
			val = val - l[i]
	else:
		for i in range(maxIndex+1,max2Index):
			val = val - l[i]

	#print "In Main Corrected Value = " + str(val)
	#print "In Main : " + str(max) + ", " + str(max2) + " Val = " + str(val)
	area =  val + getArea(leftList, LEFT) + getArea(rightList, RIGHT)

print "Area = " + str(area)

