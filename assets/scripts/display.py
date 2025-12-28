import pygame
import sys
from ..scripts.settings import *


class Display:
    def __init__(self, manager):
        self.manager = manager
        self.team = []

        self.window = pygame.display.get_surface()
        self.fonts = {
            "Helvetica": pygame.font.Font("assets/fonts/HelveticaNeueLight.otf", 24),
            "HelveticaSmall": pygame.font.Font("assets/fonts/HelveticaNeueLight.otf", 20),
            "HelveticaLargeBold": pygame.font.Font("assets/fonts/HelveticaNeueBold.otf", 40),
            "HelveticaBold": pygame.font.Font("assets/fonts/HelveticaNeueBold.otf", 24)
        }

        self.script = None

        self.logos = {}  # 200 x 200 team logo
        self.logos_upcoming_games = {}  # 100 x 100 team logo

        for team in TEAM_TRICODE_TO_NAME.values():
            filename = f"assets/images/team_logos/{'_'.join([a for a in team.lower().split(' ')])}.png"
            logo = pygame.image.load(filename)
            self.logos[team] = pygame.transform.smoothscale(logo, (200, 200))
            self.logos_upcoming_games[team] = pygame.transform.smoothscale(logo, (100, 100))

    def setup_console(self, console):
        self.script = console
        self.script.setup_display()
        self.script.run()

    def draw_background(self):
        self.window.fill(EIGENGRAU)

        # top bar
        team = self.manager.team
        pygame.draw.rect(self.window, TEAM_COLORS[team.name][0], (0, 0, SCREEN_WIDTH, 120))
        pygame.draw.rect(self.window, TEAM_COLORS[team.name][1], (0, 120, SCREEN_WIDTH, 10))

        # displaying team logo
        self.window.blit(self.logos[self.manager.team.name], (0, 0))

    def run(self):
        while True:
            self.draw_background()
            self.draw_hud()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
