import pygame

from ..scripts.manager import Manager
from ..scripts.display_pages.main_team_console import MainTeamConsole
from ..scripts.display_pages.main_games_console import MainGamesConsole
from ..scripts.display_pages.player_console import PlayerConsole
from ..scripts.settings import *


class DisplayHandler:
    def __init__(self, manager):
        pygame.init()

        self.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("NBA Manager")
        logo = pygame.image.load("assets/images/logo.png")
        pygame.display.set_icon(logo)

        self.main_team_console = MainTeamConsole(manager)
        self.player_console = PlayerConsole(manager)
        self.main_games_console = MainGamesConsole(manager)

        self.current = self.main_games_console

        self.current.setup_console(self.current)
