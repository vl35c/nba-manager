from ..scripts.player import Player
from ..scripts.team import Team
from ..scripts.settings import *


class FileHandler:
    def __init__(self):
        self.players = {}
        self.teams = {}

        self.__load_players()
        self.__load_teams()
        self.__add_players_to_team()

    @staticmethod
    def get_data_from_file(filename: str) -> list[str]:
        try:
            with open(f"assets/data/{filename}", "r") as file:
                return file.readlines()
        except FileNotFoundError:
            return []

    def __load_players(self) -> dict[str, Player]:
        players = {}

        # get all player data
        player_data = self.get_data_from_file("player_data.csv")
        # ignore first line as it contains row headers
        for line in player_data[1:]:
            line = line.rstrip('\n')
            players.update({line.split(',')[0]: Player(*line.split(','))})

        attribute_data = self.get_data_from_file("player_attributes.csv")
        for line in attribute_data:
            line = line.rstrip('\n')
            player = line.split(',')[0]
            # enumerate over list of attributes and add into dict
            for index, value in enumerate(line.split(',')[1:]):
                # ATTRIBUTE_ORDER is used to get name of attribute
                players[player].attributes.update({ATTRIBUTE_ORDER[index]: value})

        self.players = players

    def __load_teams(self) -> dict[str, Team]:
        teams = {}

        team_data = self.get_data_from_file("team_data.csv")
        for line in team_data:
            data = line.split(',')
            teams.update({data[0].rstrip('\n'): Team(*data[:-1], data[-1].rstrip('\n'))})

        self.teams = teams

    def __add_players_to_team(self) -> None:
        roster_data = self.get_data_from_file("team_roster_24.csv")

        for line in roster_data:
            items = line.split(',')

            for player in items[1:]:
                team = self.teams[items[0]]
                try:
                    team.add_player(self.players[player.rstrip('\n')])
                    self.players[player.rstrip('\n')].current_team = team
                except KeyError:
                    player, position = ' '.join(player.split(' ')[:-1]), player.split(' ')[-1].rstrip('\n')
                    team.add_player(self.players[player.rstrip('^\n')])
                    self.players[player].current_team = team
                    self.players[player].starter = True
                    self.players[player].playing_position = position

