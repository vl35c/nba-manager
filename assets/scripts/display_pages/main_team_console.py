import pygame
from ..display import Display
from ..player import Player
from ..settings import *


class MainTeamConsole(Display):
    def __init__(self, manager):
        # positions to blit player images
        self.player_positions = [
            (740, 500),
            (560, 400),
            (900, 350),
            (620, 220),
            (800, 260),
            (560, 670),
            (680, 670),
            (800, 670),
            (920, 670)
        ]

        # colors to render player attribute scores
        self.player_attribute_colors = {}

        # indexes to keep track of where scrollable boxes are
        self.players_at_index = 0
        self.bench_at_index = 0

        super().__init__(manager)

    # returns a lerped color from dark green at ~3200 to light orange at ~2000
    @staticmethod
    def total_attribute_colors(player):
        colors = {
            3400: (0, 82, 3),
            3200: (0, 82, 3),
            3000: (0, 171, 6),
            2800: (57, 194, 19),
            2600: (95, 194, 19),
            2400: (130, 194, 19),
            2200: (162, 194, 19),
            2000: (194, 165, 19),
            1800: (194, 165, 19)
        }

        attr = int(player.attributes["Total Attributes"])
        low_color = attr // 200 * 200
        high_color = attr // 200 * 200

        pos = (high_color - attr) / 200
        color_vec = [colors[high_color][i] - colors[low_color][i] for i in range(3)]
        color = [c * pos for c in color_vec]
        color = [int(c + colors[low_color][i]) for i, c in enumerate(color)]

        return tuple(color)

    def setup_display(self):
        team = self.manager.team
        sorted_team = sorted(
            team.players, 
            key=lambda p: (p.starter, p.attributes["Total Attributes"]), 
            reverse=True
        )
        self.team = sorted_team

        for player in self.team:
            self.player_attribute_colors[player] = self.total_attribute_colors(player)
        
        self.starters = sorted(
            team.players, 
            key=lambda p: int(p.playing_position), 
            reverse=True
        )[:5][::-1]
        self.bench = sorted(
                team.players, 
                key=lambda p: (int(p.playing_position), p.attributes["Total Attributes"]),
                reverse=True
        )[5:]

    def draw_hud(self):
        team = self.manager.team

        pygame.draw.rect(self.window, TEAM_COLORS[team.name][1], (20, 240, 480, 550))
        pygame.draw.rect(self.window, TEAM_COLORS[team.name][0], (30, 250, 460, 530))

        pygame.draw.rect(self.window, TEAM_COLORS[team.name][1], (240, 70, 120, 40), 0, 10)
        pygame.draw.rect(self.window, TEAM_COLORS[team.name][1], (380, 70, 120, 40), 0, 10)
        players = self.fonts["HelveticaBold"].render("PLAYERS", True, WHITE)
        games = self.fonts["HelveticaBold"].render("GAMES", True, WHITE)

        self.window.blit(players, (245, 80))
        self.window.blit(games, (395, 80))

        text = self.fonts["HelveticaBold"].render("PLAYERS", True, WHITE)
        self.window.blit(text, (30, 210))

        for index, player in enumerate(self.team[self.players_at_index:self.players_at_index + 5]):
            self.draw_player(player, index)

    def draw_player(self, player: Player, index) -> None:
        pygame.draw.rect(self.window, WHITE, (40, 260 + 100 * index, 440, 102), 2)
        
        name = self.fonts["Helvetica"].render(player.name, True, WHITE)
        position = self.fonts["Helvetica"].render(player.position[0], True, WHITE)
        ovr = self.fonts["HelveticaLargeBold"].render(player.attributes["Total Attributes"], True, WHITE)

        self.window.blit(name, (170, 330 + 100 * index))
        self.window.blit(position, (170, 275 + 100 * index))
        pygame.draw.rect(
            self.window,
            self.player_attribute_colors[player],
            (353, 270 + 100 * index, 120, 80),
            0,
            16
        )
        self.window.blit(ovr, (370, 295 + 100 * index))

        if player.image is not None:
            self.window.blit(player.image, (30, 260 + 100 * index))

        # draw half court diagram
        self.drawer.half_court(560, 240)

    # mouse hover handling
    def hover_functions(self):
        mx, my = pygame.mouse.get_pos()
        hand = lambda: pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

        interactive = {
            (40, 260, 440, 502):  hand,
            (740, 500, 125, 100): hand,
            (560, 400, 125, 100): hand,
            (900, 350, 125, 100): hand,
            (620, 220, 125, 100): hand,
            (800, 260, 125, 100): hand,
            (510, 250, 30, 15):   hand,
            (510, 275, 30, 15):   hand,
            (560, 660, 506, 120): hand,
            (535, 705, 15, 30):   hand,
            (1072, 705, 15, 30):  hand,
            (240, 70, 120, 40):   hand,
            (380, 70, 120, 40):   hand
        }

        # checking collision this way as pygame.Rect is unhashable
        for z in interactive:
            if z[0] <= mx <= z[0] + z[2] and z[1] <= my <= z[1] + z[3]:
                interactive[z]()
                break
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
