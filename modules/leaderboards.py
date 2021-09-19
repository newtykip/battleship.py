from structures.Board import Board
from modules.utils import cls, rootDir, exitGame
import csv
import time
import modules.formatting as formatting

BANNER = formatting.bold("""
  _                       _              _                             _ 
 | |                     | |            | |                           | |
 | |      ___   __ _   __| |  ___  _ __ | |__    ___    __ _  _ __  __| |
 | |     / _ \ / _` | / _` | / _ \| '__|| '_ \  / _ \  / _` || '__|/ _` |
 | |____|  __/| (_| || (_| ||  __/| |   | |_) || (_) || (_| || |  | (_| |
 |______|\___| \__,_| \__,_| \___||_|   |_.__/  \___/  \__,_||_|   \__,_|
""")

def getTopScores():
	with open(rootDir + '/scores.csv') as f:
		reader = csv.reader(f, delimiter=',')
		reader = sorted(reader, key=lambda x: (-int(x[1]))) # Sort the scores by highest
		filteredScores = []
		filteredScoresNames = []
		for score in reader:
			if len(score) > 0:
				# Only take the best score from each player
				scoreName = score[0]
				if scoreName not in filteredScoresNames:
					filteredScoresNames.append(scoreName)
					filteredScores.append({
						'name': score[0],
						'score': int(score[1])
					})
		return filteredScores

def saveScore(name: str, board: Board):
	with open(rootDir + '/scores.csv', 'a') as f:
		writer = csv.writer(f, delimiter=',')
		writer.writerow([name, board.score])

def renderLeaderboard(name: str):
	cls()
	topScores = getTopScores()
	print(BANNER)
	print('Here are the best of the best at Battleship.py!\n')
	if len(topScores) == 0:
		print(formatting.bold('No one has played Battleship.py yet! Be the first (:'))
	for i, score in enumerate(topScores):
		scoreName = score.get('name')
		entry = '%i) %s - %i points!' % (i + 1, scoreName, score.get('score'))
		if scoreName == name:
			entry += ' (it\'s you!)'
			entry = formatting.bold(entry)
		print(entry)
