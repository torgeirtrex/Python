import random
import pandas
from openpyxl import load_workbook

class Player:
    '''
    Player is on a single team with many other players
    Players play a in a game for a team
    '''
    def __init__(self, name, skill):
        self.name = name

        # Skill
        self.skill = skill
        # Salary

    def salary(self):
        return 5000 + self.skill * 10

    def __str__(self):
        return 'Name: {}, Skill: {}'.format(self.name, self.skill)


def generate_player():
    #Import player names from external file
#    df = pandas.read_excel('PlayersFMimport.xlsx', sheetname=0)
#   first_names2 = df['A'].tolist()
    wb = load_workbook('PlayersFMimport.xlsx')
    ws = wb.get_sheet_by_name('Ark1')
    column = ws['A']
    first_names = [column[x].value for x in range(len(column))]
    '''
    first_names = [
        'Ole', 'Petter', 'Jan', 'Per', 'Frode'
    ]
    '''
    first_name = random.choice(first_names)
    last_name = random.choice(first_names)

    full_name = '{} {}'.format(first_name, last_name)
    skill = 10 + random.randint(0, 90)
    return Player(full_name, skill)
