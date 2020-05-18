# https://www.youtube.com/watch?v=jO9BM5pa398 2 hours tutorial with PyAndy
from leaguefm import League
from teamfm import Team
from playerfm import generate_player, Player
from managerfm import Manager
import random

'''
https://github.com/herepete/football_manager_2
Choose team to manage: https://github.com/garrincha33/PythonFootballManager/blob/master/venv/__main__.py
'''

def main():
    # Setup for data
    # Generate some players
    players = []

    for i in range(100):
        players.append(generate_player())

        # Set ut teams manually
    teams = [
        Team('Chelsea'),
        Team('Man City'),
        Team('Arsenal'),
        Team('West Ham'),
        Team('Hull City'),
    ]

    for team in teams:
        for player_num in range(11):
            # give them 11 starting players
            selected_player = random.choice(players)
            team.players.append(selected_player)
            players.remove(selected_player)



    first_league = League('Premiership League')
    first_league.set_teams(teams)

    # Create manager
    manager = Manager(random.choice(teams), first_league)

    print('Season begins')
    for i in range(10):
        first_league.play_round()
    print('Season ends')


if __name__ == '__main__':
    main()
