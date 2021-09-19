from modules.pregame import onboarding, mainMenu

# Figure out the player's name and trigger the main menu
playerName = onboarding()
mainMenu(playerName)
