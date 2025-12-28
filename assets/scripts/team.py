class Team:
    def __init__(
        self,
        name: str,
        tricode: str
    ):
        self.name = name
        self.tricode = tricode
        self.players = []
