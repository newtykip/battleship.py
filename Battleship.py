from pregame import onboarding, mainMenu

# Figure out the player's name and trigger the main menu
playerName = onboarding()
mainMenu(playerName)

# # Save the score to the csv file
# with open(currentDir + '/scores.csv', 'w') as f:
# 	writer = csv.writer(f, delimiter=',')
# 	writer.writerow([playerName, score])
