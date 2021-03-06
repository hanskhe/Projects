#PyDoku is a Sudoku solver written in Python.
#Author: Hans Kristian
#GitHub: hanskhe

###Imports
from random import randint

###Globals
debug = True


def getBoard(filename, boardNumber):
	#Returns a board from the file. If no boardnumber is given, a random board is chosen
	f = open(filename, "r")
	lines = f.readlines()
	f.close()
	if (boardNumber != None):
		return lines[boardNumber]
	else:
		return lines[randint(0,len(lines))]

def parseBoard(raw_board, x, y):
	#Takes a board and parses it so the rest of the program can use it
	#x and y represents the size of the board in x and y direction. Standard sudoku is 9x9
	#Modify this metod to fit the input you are using
	pos = 0
	board = []
	for i in range(0,y):
		board.append([])
		for j in range(0,x):
			board[i].append(raw_board[pos])
			pos +=1
	if (debug):
		for i in range(0,len(board)):
			print(board[i])
	return board

def boardPrinter(board):
	#Prints the board in a friendly way
	print("-------------", end="")
	for i in range(0,len(board[0])):
		print("")
		for j in range(0,len(board[i])):
			if (j%3 == 0):
				print("|", end="")
			print(" " if str(board[i][j])=="." else str(board[i][j]), end="")
		print("|", end="")
	print("\n-------------")

def generatePossibilitiesList(board):
	#Makes a list of all possibilities for a cell. If a cell is not empty, there are no posibilities.
	#This list will be the basis for the solving of the Sudoku.
	possible = []
	for i in range(0,len(board[0])):
		possible.append([])
		for j in range(0,len(board[i])):
			if (board[i][j] == "."):
				print(i,j)
				possible[i].append(["1","2","3","4","5","6","7","8","9"])
			else:
				possible[i].append([])
	return possible

def checkRow(board, possible, row, rNumber):
	#Checks a row or column based on the bool row. Edits the possible list to reflect changes.
	newPossible = possible[:]
	if (row == True):
		numbersInRow = []
		for i in range(0,len(board[rNumber])):
			if (board[rNumber][i] != "."):
				numbersInRow.append(board[rNumber][i])
		if debug:
			print(numbersInRow)
		#Edit the newPossible list to reflect what we now know about the row
		#All numbers that are present in the row may not be placed in the row again
		for i in range(0,len(newPossible[rNumber])):
			for num in numbersInRow:
				if (num in newPossible[rNumber][i]):
					newPossible[rNumber][i].remove(num)
					if debug: print("Removed: "+num)
		return newPossible
	elif (row == False):
		#We are now checking a column
		numbersInColumn = []
		for i in range(0,len(board)):
			if (board[i][rNumber] != "."):
				numbersInColumn.append(board[i][rNumber])
		if debug:
			print(numbersInColumn)
		#Edit the newPossible list to reflect what we now know about the column
		#All numbers that are present in the column may not be placed in the column again
		for i in range(0,len(newPossible)):
			for num in numbersInColumn:
				if (num in newPossible[i][rNumber]):
					newPossible[i][rNumber].remove(num)
					if debug: print("Removed: " + num)
		return newPossible


testBoard = getBoard("Boards.txt", 0)
testParse = parseBoard(testBoard, 9,9)
boardPrinter(testParse)
possible = generatePossibilitiesList(testParse)
print(checkRow(testParse,possible,True,0))
print(checkRow(testParse,possible,False,3))