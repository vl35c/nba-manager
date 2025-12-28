from assets.scripts.file_handler import FileHandler
from assets.scripts.player import Player
from assets.scripts.team import Team
from assets.scripts.manager import Manager
from assets.scripts.display_handler import DisplayHandler


file_handler = FileHandler()

players: dict[str, Player] = file_handler.players
teams: dict[str, Team] = file_handler.teams

DisplayHandler(Manager(teams, players))
