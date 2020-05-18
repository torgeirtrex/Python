class Manager:
    '''
    runs a tem
    '''

    def __init__(self, team, league):
        self.team = team
        self.league = league

        print('You are a manager')
        print('You can chose from the following teams: '.format(self.team))

        print('You manage {}'.format(self.team))

        self.view_players()

#Print out all teams in the league
#  def __str__(self):
#       print('Team name: {}'.format(self.team))

    def manage(self):
        '''
        before every round we can make changes as a manager
        :return:
        '''
        print('')
        print('You team is {}'.format(self.team))
        print('You have {} wins out of {} games'.format(self.team.wins,
                                                        self.league.rounds_played))
        print('You currently have ${}'.format(self.team.money))
        print('')

    def view_players(self):
        for player in self.team.players:
            print(player)

