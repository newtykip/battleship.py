import os
import modules.formatting as formatting
import urllib.request
import json
import time

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
  print('See you next time, %s (:' % (name))
  time.sleep(2)
  exit()

def getScores() -> list[dict]:
  r = urllib.request.urlopen(scoreUrl)
  r = json.load(r)
  return r['scores']

def getBans() -> list[str]:
  r = urllib.request.urlopen(scoreUrl)
  r = json.load(r)
  return r['bans']

def hasPlayed(name):
  found = False
  scores = getScores()
  for score in scores:
    if score.get('name').lower() == name.lower():
      found = True
      break
  return found

def error(txt):
  print(formatting.bold(formatting.red(txt)))

def checkSettings():
  # Fetch the default settings from GitHub gists
  defaultSettings = urllib.request.urlopen(settingsUrl)
  defaultSettings = json.load(defaultSettings)
  defaultSettings = defaultSettings.get('files').get('settings.json').get('content')
  defaultSettings = json.loads(defaultSettings)
  # If there is no settings file
  if not os.path.isfile(rootDir + '/settings.json'):
    # Save the default settings to a file
    with open(rootDir + '/settings.json', 'w') as f:
      f.write(json.dumps(defaultSettings, indent=2, sort_keys=True))
      f.close()
  else:
    newSettings = defaultSettings
    with open(rootDir + '/settings.json') as f:
      parsed = json.load(f)
      for key in defaultSettings.keys():
        for key2 in defaultSettings[key]:
          if key2 not in parsed[key].keys():
            newSettings[key][key2] = defaultSettings[key][key2]
      f.close()
    with open(rootDir + '/settings.json', 'w') as f:
      f.write(json.dumps(newSettings, indent=2, sort_keys=True))
      f.close()

rootDir = os.path.dirname(os.path.realpath(__file__)) + '/..'
settingsUrl = 'https://api.github.com/gists/27d2fe8d45dec9eb59b683b165daa563'
scoreUrl = 'https://jsonblob.com/api/jsonBlob/889122681291816960'
