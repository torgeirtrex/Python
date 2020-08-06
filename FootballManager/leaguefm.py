import copy
import random
from teamfm import Game, Team

#Inspirasjon av videreutvikling: https://github.com/rajatagarwal/game_football_manager/blob/master/team.py

class League:
    '''
    League has many teams
    Each team has a ranking in this league
    '''

    def __init__(self, name):
        self.name = 'League 1'
        self.teams = []

    def set_teams(self, teams):
        self.teams = teams

    def play_round(self):
        '''
        Play a round
        '''

        print('/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/ \nRound begins')
        num_teams = len(self.teams)
        num_games = num_teams // 2

        teams_to_play = copy.copy(self.teams)

        for game_num in range(num_games):
            home_team = random.choice(teams_to_play)
            teams_to_play.remove(home_team)
            away_team = random.choice(teams_to_play)
            teams_to_play.remove(away_team)

            game = Game(self, home_team, away_team)
            game.play()
            self.resolve_game(game)

        print('Round ends')

        'print(game.countgoalshome())'
        'print(game.countgoalsaway())'

        #ladder status
        self.ladder()

    def ladder(self):
        for team in sorted(self.teams, key=lambda x: x.wins, reverse=True, ):
            print('{} Wins:{} Draws:{} Losses:{} Total Points:{}'.format(team, team.wins, team.draws,
                                                                                       team.losses, team.total_points,
                                                                                       ))

    def resolve_game(self, game):
        'Work in progress with goals scored  - play()[0]'
        if game.home_team_draw:
            game.home_team.draws += 1
            game.away_team.draws += 1
            game.home_team.total_points += 1
            game.away_team.total_points += 1
        elif game.home_team_won:
            #home team won
            game.home_team.wins += 1
            game.away_team.losses += 1
            game.home_team.total_points += 3
        else:
            #away team won
            game.away_team.wins += 1
            game.home_team.losses += 1
            game.away_team.total_points += 3


        game.home_team.pay_players()
        game.away_team.pay_players()


