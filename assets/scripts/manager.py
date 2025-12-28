from ..scripts.player import Player
from ..scripts.team import Team


class Manager:
    def __init__(self, teams, players):
        self.teams: dict[str, Team] = teams
        self.players: dict[str, Player] = players
