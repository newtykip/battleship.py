import json
from structures.board import Board
from modules.utils import cls, error, exitGame, getBans, getScores, scoreUrl
import modules.formatting as formatting
import urllib

BANNER = formatting.bold("""
  _                       _              _                             _ 
 | |                     | |            | |                           | |
 | |      ___   __ _   __| |  ___  _ __ | |__    ___    __ _  _ __  __| |
 | |     / _ \ / _` | / _` | / _ \| '__|| '_ \  / _ \  / _` || '__|/ _` |
 | |____|  __/| (_| || (_| ||  __/| |   | |_) || (_) || (_| || |  | (_| |
 |______|\___| \__,_| \__,_| \___||_|   |_.__/  \___/  \__,_||_|   \__,_|
""")

def getTopScores():
	scores = getScores()
	filteredScores = []
	filteredScoresNames = []
	for score in scores:
		name = score.get('name')
		scoreValue = score.get('score')
		torpedos = score.get('torpedos')
		ratio = scoreValue / torpedos
		formattedScore = {
			'name': name,
			'score': scoreValue,
			'torpedos': torpedos,
			'ratio': ratio
		}
		if name not in filteredScoresNames:
			filteredScoresNames.append(name)
			filteredScores.append(formattedScore)
		else:
			for oldScore in filteredScores:
				if name.lower() == oldScore.get('name').lower() and oldScore.get('ratio') < ratio:
					filteredScores.remove(oldScore)
					filteredScores.append(formattedScore)
	return sorted(filteredScores, key=lambda x: x['ratio'], reverse=True)

def saveScore(name: str, board: Board):
	scores = getScores()
	bans = getBans()
	if name in bans:
		error('You have been banned from score submission, so your score has not submitted!')
		exitGame(name)
	maxScore = 0
	for ship in board.ships:
		maxScore += ship.size
	if board.score > maxScore:
		error('That score isn\'t legitimate! >:(\n')
		bans.append(name.lower())
		data = bytes(json.dumps({ 'scores': scores, 'bans': bans }).encode('UTF-8'))
	else:
		newScore = {
			'name': name.lower(),
			'score': board.score,
			'torpedos': board.settings.get('torpedos')
		}
		scores.append(newScore)
		data = bytes(json.dumps({ 'scores': scores }).encode('UTF-8'))
	r = urllib.request.Request(scoreUrl, data=data, method='PUT')
	r.add_header("Content-type", "application/json; charset=UTF-8")
	urllib.request.urlopen(r)
	if board.score > maxScore:
		exitGame(name)

def renderLeaderboard(name: str):
	cls()
	topScores = getTopScores()
	print(BANNER)
	print('Here are the best of the best at Battleship.py!\n')
	if len(topScores) == 0:
		print(formatting.bold('No one has played Battleship.py yet! Be the first (:'))
	for i, score in enumerate(topScores):
		scoreName = score.get('name')
		entry = '%i) %s - %i points in %i torpedos!' % (i + 1, scoreName, score.get('score'), score.get('torpedos'))
		if scoreName.lower() == name.lower():
			entry += ' (it\'s you!)'
			entry = formatting.bold(entry)
		print(entry)
