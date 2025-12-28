from ..display import Display


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
