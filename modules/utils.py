import os
import modules.formatting as formatting
import csv
import urllib.request
import json

BANNER = formatting.bold("""
  ____          _    _    _             _      _                        
 |  _ \        | |  | |  | |           | |    (_)                       
 | |_) |  __ _ | |_ | |_ | |  ___  ___ | |__   _  _ __     _ __   _   _ 
 |  _ <  / _` || __|| __|| | / _ \/ __|| '_ \ | || '_ \   | '_ \ | | | |
 | |_) || (_| || |_ | |_ | ||  __/\__ \| | | || || |_) |_ | |_) || |_| |
 |____/  \__,_| \__| \__||_| \___||___/|_| |_||_|| .__/(_)| .__/  \__, |
                                                 | |      | |      __/ |
                                                 |_|      |_|     |___/ 
""")

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def exitGame(name):
	cls()
	print('See you next time, %s (:' % (name))
	exit()

def hasPlayed(name):
  with open(rootDir + '/scores.csv') as f:
    reader = csv.reader(f, delimiter=',')
    found = False
    for row in reader:
      for col in row:
        if col == name:
          found = True
          break
    return found

def error(txt):
  print(formatting.bold(formatting.red(txt)))

def ensureSettingsExists():
  # If there is no settings file
  if not os.path.isfile(rootDir + '/settings.json'):
    # Fetch the default settings from GitHub gists
    defaultSettings = urllib.request.urlopen('https://api.github.com/gists/27d2fe8d45dec9eb59b683b165daa563')
    defaultSettings = json.load(defaultSettings)
    # Save the default settings to a file
    with open(rootDir + '/settings.json', 'w') as f:
      f.write(defaultSettings['files']['settings.json']['content'])
      f.close()

def ensureScoreFileExists():
  # If there is no scores file
  if not os.path.isfile(rootDir + '/scores.csv'):
    # Create a scores file
    open(rootDir + '/scores.csv', 'x').close()

rootDir = os.path.dirname(os.path.realpath(__file__)) + '/..'
