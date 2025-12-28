from ..scripts.player import Player


class Team:
    def __init__(
        self,
        name: str,
        tricode: str
    ):
        self.name = name
        self.tricode = tricode
        self.players: list[Player] = []

    def add_player(self, player: Player) -> None:
        self.players.append(player)
