class VariableSettings:
    def __init__(self):
        self.current_day = CURRENT_DAY
        self.current_month = CURRENT_MONTH
        self.current_year = CURRENT_YEAR
        self.current_season = CURRENT_SEASON

        self.season_start_day = SEASON_START_DAY
        self.season_start_month = SEASON_START_MONTH

    def set_day(self, value):
        self.current_day = value

    def set_month(self, value):
        self.current_month = value

    def progress_date(self, amount=1):
        self.current_day += amount
        if self.current_day > DAYS_PER_MONTH[self.current_month]:
            self.current_day -= DAYS_PER_MONTH[self.current_month]
            self.current_month += 1
            self.current_month %= 12


ATTRIBUTE_ORDER = [
    'Outside Scoring',
    'Close Shot',
    'Mid-Range Shot',
    'Three-Point Shot',
    'Free Throw',
    'Shot IQ',
    'Offensive Consistency',
    'Athleticism',
    'Speed',
    'Acceleration',
    'Strength',
    'Vertical',
    'Stamina',
    'Hustle',
    'Overall Durability',
    'Inside Scoring',
    'Layup',
    'Standing Dunk',
    'Driving Dunk',
    'Post Hook',
    'Post Fade',
    'Post Control',
    'Draw Foul',
    'Hands',
    'Playmaking',
    'Pass Accuracy',
    'Ball Handle',
    'Speed with Ball',
    'Pass IQ',
    'Pass Vision',
    'Defense',
    'Interior Defense',
    'Perimeter Defense',
    'Steal',
    'Block',
    'Lateral Quickness',
    'Help Defense IQ',
    'Pass Perception',
    'Defensive Consistency',
    'Rebounding',
    'Offensive Rebound',
    'Defensive Rebound',
    'Intangibles',
    'Potential',
    'Total Attributes'
]

STAT_TYPE = {
    'Outside Scoring': [
        'Close Shot',
        'Mid-Range Shot',
        'Three-Point Shot',
        'Free Throw',
        'Shot IQ',
        'Offensive Consistency'
    ],
    'Inside Scoring': [
        'Layup',
        'Standing Dunk',
        'Driving Dunk',
        'Post Hook',
        'Post Fade',
        'Post Control',
        'Draw Foul',
        'Hands'
    ],
    'Defense': [
        'Interior Defense',
        'Perimeter Defense',
        'Steal',
        'Block',
        'Help Defense IQ',
        'Pass Perception',
        'Defensive Consistency'
    ],
    'Athleticism': [
        'Speed',
        'Agility',
        'Strength',
        'Vertical',
        'Stamina',
        'Hustle',
        'Overall Durability'
    ],
    'Playmaking': [
        'Pass Accuracy',
        'Ball Handle',
        'Speed with Ball',
        'Pass IQ',
        'Pass Vision'
    ],
    'Rebounding': [
        'Offensive Rebound',
        'Defensive Rebound'
    ]
}

STAT_COLORS = {
    'Outside Scoring': '#365ec9',
    'Inside Scoring': '#c98c36',
    'Defense': '#c93636',
    'Athleticism': '#3bc936',
    'Playmaking': '#9636c9',
    'Rebounding': '#36c9a9'
}

STAT_COLORS_DARKEN = {
    'Outside Scoring': '#041645',
    'Inside Scoring': '#523102',
    'Defense': '#6e0808',
    'Athleticism': '#054203',
    'Playmaking': '#2e0345',
    'Rebounding': '#034a3a'
}

ATTRIBUTE_AMOUNT = len(ATTRIBUTE_ORDER)

SALARY_CAP = 136_021_000

DAYS_PER_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

CURRENT_SEASON = 2024
CURRENT_YEAR = 2023
CURRENT_MONTH = 7
CURRENT_DAY = 6

SEASON_START_MONTH = 10
SEASON_START_DAY = 22

SEASON_END_MONTH = 4
SEASON_END_DAY = 13

DAYS_OFF = [
    (24, 12)
]

MONTHS_TRI = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

TEAM_TRICODE_TO_NAME = {
    'ATL': 'Atlanta Hawks',
    'BOS': 'Boston Celtics',
    'BRK': 'Brooklyn Nets',
    'CHA': 'Charlotte Hornets',
    'CHI': 'Chicago Bulls',
    'CLE': 'Cleveland Cavaliers',
    'DAL': 'Dallas Mavericks',
    'DEN': 'Denver Nuggets',
    'DET': 'Detroit Pistons',
    'GSW': 'Golden State Warriors',
    'HOU': 'Houston Rockets',
    'IND': 'Indiana Pacers',
    'LAC': 'Los Angeles Clippers',
    'LAL': 'Los Angeles Lakers',
    'MEM': 'Memphis Grizzlies',
    'MIA': 'Miami Heat',
    'MIL': 'Milwaukee Bucks',
    'MIN': 'Minnesota Timberwolves',
    'NOP': 'New Orleans Pelicans',
    'NYK': 'New York Knicks',
    'OKC': 'Oklahoma City Thunder',
    'ORL': 'Orlando Magic',
    'PHI': 'Philadelphia 76ers',
    'PHO': 'Phoenix Suns',
    'POR': 'Portland Trail Blazers',
    'SAC': 'Sacramento Kings',
    'SAS': 'San Antonio Spurs',
    'TOR': 'Toronto Raptors',
    'UTA': 'Utah Jazz',
    'WAS': 'Washington Wizards'
}

PPG_PER_TEAM = {
    'Atlanta Hawks': 118.3,
    'Boston Celtics': 120.6,
    'Brooklyn Nets': 110.4,
    'Charlotte Hornets': 106.6,
    'Chicago Bulls': 112.3,
    'Cleveland Cavaliers': 112.6,
    'Dallas Mavericks': 117.9,
    'Denver Nuggets': 114.9,
    'Detroit Pistons': 109.9,
    'Golden State Warriors': 117.8,
    'Houston Rockets': 114.3,
    'Indiana Pacers': 123.3,
    'Los Angeles Clippers': 115.6,
    'Los Angeles Lakers': 118.0,
    'Memphis Grizzlies': 105.8,
    'Miami Heat': 110.1,
    'Milwaukee Bucks': 119.0,
    'Minnesota Timberwolves': 113.0,
    'New Orleans Pelicans': 115.1,
    'New York Knicks': 112.8,
    'Oklahoma City Thunder': 120.1,
    'Orlando Magic': 110.5,
    'Philadelphia 76ers': 114.6,
    'Phoenix Suns': 116.2,
    'Portland Trail Blazers': 106.4,
    'Sacramento Kings': 116.6,
    'San Antonio Spurs': 112.1,
    'Toronto Raptors': 112.4,
    'Utah Jazz': 115.7,
    'Washington Wizards': 113.7
}

MAX_STATS = {
    'ppg': 140,
    'apg': 32,
    'rpg': 46,
    'spg': 13,
    'bpg': 9
}

DIVISION_BY_TEAM = {
    'Atlanta Hawks': 'Southeast',
    'Boston Celtics': 'Atlantic',
    'Brooklyn Nets': 'Atlantic',
    'Charlotte Hornets': 'Southeast',
    'Chicago Bulls': 'Central',
    'Cleveland Cavaliers': 'Central',
    'Dallas Mavericks': 'Southwest',
    'Denver Nuggets': 'Northwest',
    'Detroit Pistons': 'Central',
    'Golden State Warriors': 'Pacific',
    'Houston Rockets': 'Southwest',
    'Indiana Pacers': 'Central',
    'Los Angeles Clippers': 'Pacific',
    'Los Angeles Lakers': 'Pacific',
    'Memphis Grizzlies': 'Southwest',
    'Miami Heat': 'Southeast',
    'Milwaukee Bucks': 'Central',
    'Minnesota Timberwolves': 'Northwest',
    'New Orleans Pelicans': 'Southwest',
    'New York Knicks': 'Atlantic',
    'Oklahoma City Thunder': 'Northwest',
    'Orlando Magic': 'Southeast',
    'Philadelphia 76ers': 'Atlantic',
    'Phoenix Suns': 'Pacific',
    'Portland Trail Blazers': 'Northwest',
    'Sacramento Kings': 'Pacific',
    'San Antonio Spurs': 'Southwest',
    'Toronto Raptors': 'Atlantic',
    'Utah Jazz': 'Northwest',
    'Washington Wizards': 'Southeast'
}

CONFERENCE_BY_DIVISION = {
    'Atlantic': 'East',
    'Central': 'East',
    'Southeast': 'East',
    'Pacific': 'West',
    'Northwest': 'West',
    'Southwest': 'West'
}

# DISPLAY SETTINGS
SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 810

# colors
EIGENGRAU = '#16161d'
WHITE = '#fcf5e5'

TEAM_COLORS = {
    'Atlanta Hawks': [(200, 16, 46), (253, 185, 39), (0, 0, 0), (158, 162, 162), (255, 255, 255)],
    'Boston Celtics': [(0, 122, 51), (139, 111, 78), (150, 56, 33), (255, 255, 255), (0, 0, 0)],
    'Brooklyn Nets': [(0, 0, 0), (255, 255, 255)],
    'Charlotte Hornets': [(29, 17, 96), (0, 120, 140), (161, 161, 164)],
    'Chicago Bulls': [(206, 17, 65), (6, 25, 34)],
    'Cleveland Cavaliers': [(134, 0, 56), (4, 30, 66), (253, 187, 48), (0, 0, 0)],
    'Dallas Mavericks': [(0, 83, 188), (0, 43, 92), (187, 196, 202), (6, 25, 34)],
    'Denver Nuggets': [(13, 34, 64), (255, 198, 39), (139, 35, 50), (29, 66, 138)],
    'Detroit Pistons': [(200, 16, 46), (29, 66, 138), (181, 179, 179), (0, 45, 98)],
    'Golden State Warriors': [(29, 66, 138), (255, 199, 44)],
    'Houston Rockets': [(206, 17, 65), (6, 25, 34), (196, 206, 211)],
    'Indiana Pacers': [(0, 45, 98), (253, 187, 48), (190, 192, 194)],
    'Los Angeles Clippers': [(200,16,46), (29,66,148), (190,192,194), (0,0,0)],
    'Los Angeles Lakers': [(85, 37, 130), (253, 185, 39), (6, 25, 34)],
    'Memphis Grizzlies': [(93, 118, 169), (18, 23, 63), (255, 187, 34), (112, 114, 113)],
    'Miami Heat': [(152, 0, 46), (249, 160, 27), (6, 25, 34)],
    'Milwaukee Bucks': [(0, 71, 27), (240, 235, 210), (0, 125, 197), (6, 25, 34)],
    'Minnesota Timberwolves': [(12, 35, 64), (35, 97, 146), (158, 162, 162), (120, 190, 32)],
    'New Orleans Pelicans': [(0, 22, 65), (225, 58, 62), (180, 151, 90)],
    'New York Knicks': [(0, 107, 182), (245, 132, 38), (190, 192, 194), (35, 31, 32)],
    'Oklahoma City Thunder': [(0, 125, 195), (239, 59, 36), (0, 45, 98), (253, 187, 48)],
    'Orlando Magic': [(0, 125, 197), (196, 206, 211), (6, 25, 34)],
    'Philadelphia 76ers': [(0, 107, 182), (237, 23, 76), (0, 43, 92), (196, 206, 211)],
    'Phoenix Suns': [(29, 17, 96), (229, 95, 32), (6, 25, 34), (99, 113, 122), (249, 160, 27), (185, 89, 21), (190, 192, 194)],
    'Portland Trail Blazers': [(224, 58, 62), (6, 25, 34)],
    'Sacramento Kings': [(91, 43, 130), (99, 113, 122), (6, 25, 34)],
    'San Antonio Spurs': [(196, 206, 211), (6, 25, 34)],
    'Toronto Raptors': [(206, 17, 65), (6, 25, 34), (161, 161, 164), (180, 151, 90)],
    'Utah Jazz': [(0, 43, 92), (249, 160, 27), (0, 71, 27)],
    'Washington Wizards': [(0, 43, 92), (227, 24, 55), (196, 206, 212)]
}

PLAYER_JERSEY_INFO = {
    'Los Angeles Lakers': {
        'jamesle01': [(33, 99), 75, 32, 14]
    }
}
