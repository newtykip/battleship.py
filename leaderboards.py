from Board import Board
from helper import cls, currentDir, exitGame
import csv
import time

BANNER = """
  _                       _              _                             _ 
 | |                     | |            | |                           | |
 | |      ___   __ _   __| |  ___  _ __ | |__    ___    __ _  _ __  __| |
 | |     / _ \ / _` | / _` | / _ \| '__|| '_ \  / _ \  / _` || '__|/ _` |
 | |____|  __/| (_| || (_| ||  __/| |   | |_) || (_) || (_| || |  | (_| |
 |______|\___| \__,_| \__,_| \___||_|   |_.__/  \___/  \__,_||_|   \__,_|
"""

def getTopScores():
	with open(currentDir + '/scores.csv') as f:
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
	with open(currentDir + '/scores.csv', 'w') as f:
		writer = csv.writer(f, delimiter=',')
		writer.writerow([name, board.score])

def viewLeaderboards(name: str):
	renderLeaderboard(name)
	for i in range(1, 6):
		print('\n\nExiting in %i...' % (5 - i))
		time.sleep(1)
		renderLeaderboard(name)
	exitGame(name)

def renderLeaderboard(name: str):
	cls()
	topScores = getTopScores()
	print(BANNER)
	print('Here are the best of the best at Battleship.py!\n')
	for i, score in enumerate(topScores):
		scoreName = score.get('name')
		suffix = ''
		if scoreName == name:
			suffix = ' (it\'s you!)'
		print('%i) %s - %i points!%s' % (i + 1, scoreName, score.get('score'), suffix))
