import pygame
import sys
from ..scripts.settings import *


class Display:
    def __init__(self, manager):
        self.manager = manager

        pygame.init()

        self.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("NBA Manager")
        logo = pygame.image.load("assets/images/logo.png")
        pygame.display.set_icon(logo)

        self.script = None

    def setup_console(self, console):
        self.script = console
        self.script.run()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
