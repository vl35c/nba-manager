import pygame
from ..scripts.manager import Manager
from ..scripts.settings import *


class Drawer:
    def __init__(self, manager: Manager):
        self.manager = manager
        self.window = pygame.display.get_surface()
        self.team = self.manager.team

        self.colors = sorted(TEAM_COLORS[self.team.name], key=lambda c: self.luminance(c), reverse=True)

    # function to calculate luminance of rgb color
    # numbers pulled from formula
    @staticmethod
    def luminance(color):
        return color[0] * 0.2126 + color[1] * 0.7152 + color[2] * 0.0722

    def half_court(self, x, y):
        color = self.colors[0]  # brightest color

        # baseline
        pygame.draw.line(self.window, color, (x-2, y), (x+503, y), 6)
        # sidelines
        pygame.draw.line(self.window, color, (x, y), (x, y+400), 6)
        pygame.draw.line(self.window, color, (x+500, y), (x+500, y+400), 6)
        # half court line
        pygame.draw.line(self.window, color, (x-2, y+400), (x+503, y+400), 6)
        # corner 3 lines
        pygame.draw.line(self.window, color, (x+50, y), (x+50, y+100), 6)
        pygame.draw.line(self.window, color, (x+451, y), (x+451, y+100), 6)
        # 3 point line
        pygame.draw.arc(self.window, color, (x+48, y-100, 408, 400), 3.14, 6.28, 6)
        # lane lines
        pygame.draw.line(self.window, color, (x+190, y), (x+190, y+200), 6)
        pygame.draw.line(self.window, color, (x+310, y), (x+310, y+200), 6)
        # free throw line
        pygame.draw.line(self.window, color, (x+190, y+200), (x+310, y+200), 6)
        # key circle
        pygame.draw.arc(self.window, color, (x+188, y+140, 127, 120), 3.14, 6.28, 6)
        pygame.draw.arc(self.window, color, (x+188, y+140, 127, 120), 0, .314, 6)
        pygame.draw.arc(self.window, color, (x+188, y+140, 127, 120), .628, .942, 6)
        pygame.draw.arc(self.window, color, (x+188, y+140, 127, 120), 1.256, 1.57, 6)
        pygame.draw.arc(self.window, color, (x+188, y+140, 127, 120), 1.884, 2.198, 6)
        pygame.draw.arc(self.window, color, (x+188, y+140, 127, 120), 2.512, 2.826, 6)
        # backboard
        pygame.draw.line(self.window, color, (x+215, y+30), (x+285,y+30), 6)
        # basket
        pygame.draw.circle(self.window, color, (x+250, y+45), 15, 6)


