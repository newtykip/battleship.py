from modules.utils import ensureSettingsExists
from modules.pregame import onboarding, mainMenu

# Ensure that settings.json exists
ensureSettingsExists()

# Figure out the player's name and trigger the main menu
playerName = onboarding()
mainMenu(playerName)
