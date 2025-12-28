from ..scripts.player import Player
from ..scripts.team import Team


class Manager:
    def __init__(self, teams, players):
        self.__teams: dict[str, Team] = teams
        self.__players: dict[str, Player] = players
