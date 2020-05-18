import random
from helpers import goals_scored

class Team:
    '''
    player
    ranking
    single mananger
    '''
    pass

    def __init__(self, name):
        self.name = name
        self.players = []

        self.wins = 0
        self.losses = 0

        self.money = 1000000

    def pay_players(self):
        for player in self.players:
            self.money -= player.salary()

    def rating(self):
        "What is the rating of the team"
        rating = 0
        for player in self.players:
            rating += player.skill

        return rating

    def __str__(self):
        return '{} {}'.format(self.name, self.rating())

class Game:
    '''
    plays a game between two teams
    game belongs to a leagues
    '''
    def __init__(self, league, home_team, away_team):
        self.league = league
        self.home_team = home_team
        self.away_team = away_team
        self.home_team_goals = 0

        self.home_team_won = None

        print('{} vs. {}'.format(self.home_team, self.away_team))

    def play(self):
        #Return who won
        #True means hometeam won, false away team win
        print('Play begins')
        #goals_by_home_team = goals_scored(self.home_team.rating())
        #goals_by_away_team = goals_scored(self.away_team.rating())
        goalshometeam = self.goals_scored(self.home_team.rating())
        goalsawayteam = self.goals_scored(self.away_team.rating())

        print(f"Home team scored {goalshometeam}")
        print(f"Away team scored {goalsawayteam}")

        if self.home_team.rating() > self.away_team.rating():
            print('{} wins'.format(self.home_team))
            self.home_team_won = True
            self.home_team_goals = random.randint(1, 5)
            print(self.home_team, 'scores {} goals'.format(self.home_team_goals))
        else:
            print('{} wins.'.format(self.away_team))
            self.home_team_won = False


        print('Play ends')

    def countgoals(self):
        goalcounter = self.home_team_goals

#Function to let rating influence goals scored but add an element of luck to goalscoring
    def goals_scored(self, rating):
        # rating * random number between 1 to 5 / rating
        return int((rating * random.randint(1, 5) / rating))
#TO DO
    def print_menu(self):
        print('1. Select to view your squad')
        print('2. Do something else')





