from modules.utils import checkSettings
from modules.pregame import mainMenu

# Ensure that settings.json exists
checkSettings()

# Trigger the main menu
mainMenu()
