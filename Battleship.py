from modules.utils import ensureSettingsExists, ensureScoreFileExists
from modules.pregame import onboarding, mainMenu

# Ensure that settings.json and scores.csv exist
ensureSettingsExists()
ensureScoreFileExists()

# Figure out the player's name and trigger the main menu
playerName = onboarding()
mainMenu(playerName)
