from assets.scripts.file_handler import FileHandler
from assets.scripts.player import Player
from assets.scripts.team import Team
from assets.scripts.manager import Manager
from assets.scripts.display_handler import DisplayHandler


# create file handler to load data
file_handler = FileHandler()

# load players and teams to pass to manager
players: dict[str, Player] = file_handler.players
teams: dict[str, Team] = file_handler.teams

# create display handler with the manager class
DisplayHandler(Manager(teams, players))
