from Board import Board
from helper import cls, currentDir
import csv

def viewLeaderboards(name: str):
	cls()
	print('TODO')
	exit()

def saveScore(name: str, board: Board):
	with open(currentDir + '/scores.csv', 'w') as f:
		writer = csv.writer(f, delimiter=',')
		writer.writerow([name, board.score])
