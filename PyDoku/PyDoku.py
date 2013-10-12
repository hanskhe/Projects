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
				possible[i].append([1,2,3,4,5,6,7,8,9])
			else:
				possible[i].append([])
	return possible

testBoard = getBoard("Boards.txt", 0)
testParse = parseBoard(testBoard, 9,9)
boardPrinter(testParse)
print(generatePossibilitiesList(testParse))