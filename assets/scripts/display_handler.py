from ..scripts.manager import Manager
from ..scripts.display_pages.main_team_console import MainTeamConsole
from ..scripts.display_pages.main_games_console import MainGamesConsole
from ..scripts.display_pages.player_console import PlayerConsole


class DisplayHandler:
    def __init__(self, manager):
        self.main_team_console = MainTeamConsole(manager)
        self.player_console = PlayerConsole(manager)
        self.main_games_console = MainGamesConsole(manager)

        self.current = self.main_games_console

        self.current.setup_console(self.current)
