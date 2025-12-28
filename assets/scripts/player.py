import pygame
from ..scripts.payment import Payment
from ..scripts.contract import Contract
from ..scripts.trade import Trade
from ..scripts.suspension import Suspension
from ..scripts.g_league_movement import GLeagueMovement
from ..scripts.media_loader import MediaLoader


class Player:
    def __init__(
        self,
        name: str,
        draft_year: int,
        draft_round: int,
        draft_pick: int,
        position: str,
        hand: str,
        height: str,
        weight: str,
        dob: str,
        city_of_birth: str,
        country_state_of_birth: str,
        college: str,
        drafted_by: str,
        basketball_reference: str
    ):
        self.name = name
        self.draft_year = int(draft_year) if int(draft_year) != 0 else None
        self.draft_round = int(draft_round) if int(draft_round) != 0 else None
        self.draft_pick = int(draft_pick) if int(draft_pick) != 0 else None
        self.position = [p for p in position.split(' ')]
        self.hand = hand
        self.height = height
        self.weight = int(weight)
        self.dob = dob
        self.city_of_birth = city_of_birth
        self.country_state_of_birth = country_state_of_birth
        self.college = college
        self.drafted_by = drafted_by
        self.basketball_reference_id = basketball_reference

        # these fields are populated on the games startup
        self.teams = []
        self.current_team = None
        self.starter = False
        # playing position is -1 until the player is added to the current roster
        self.playing_position = -1
        self.attributes = {}
        self.payments: dict[str, Payment] = {}
        self.contracts: list[Contract] = []
        self.trades: list[Trade] = []
        self.suspensions: list[suspension] = []
        self.g_league_history: list[GLeagueMovement] = []
        self.transaction_history = []
        self.__original_image = None
        self.__image = None

        self.flags = {
            "swapping": False
        }

        self.__media_loader = MediaLoader()

    def __str__(self):
        return f"{self.name}"

    @property
    def image(self) -> pygame.Surface:
        if self.__image is None:
            path = "assets/images/player_photos/"
            filename = f"{'_'.join([a for a in self.current_team.name.split(' ')])}/{self.basketball_reference_id}.png"
            self.__original_image = self.__media_loader.load_image_to_size(f"{path}{filename.lower()}", (350, 254))
            self.__image = self.__media_loader.load_image_to_size(f"{path}{filename.lower()}", (140, 100))

        return self.__image
