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

        print('Round begins')
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

        #ladder status
        self.ladder()

    def ladder(self):
        for team in sorted(self.teams, key=lambda t: t.wins):
            print('{} {} wins'.format(team, team.wins))

    def resolve_game(self, game):
        if game.home_team_won:
            #home team won
            game.home_team.wins += 1
            game.away_team.losses += 1

        else:
            #away team won
            game.away_team.wins += 1
            game.home_team.losses += 1


        game.home_team.pay_players()
        game.away_team.pay_players()


