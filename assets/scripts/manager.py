from ..scripts.player import Player
from ..scripts.team import Team


class Manager:
    def __init__(self, teams, players):
        self.__teams: dict[str, Team] = teams
        self.__players: dict[str, Player] = players

        # temp hard coding
        self.team = self.__teams["Los Angeles Lakers"]
