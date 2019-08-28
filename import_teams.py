from contest.models import Team

import csv

init_score = 350

from django.db import connection

def drop_team_table():
    # WARN: It makes bad things happen
    cursor = connection.cursor()
    table_name = Team._meta.db_table
    sql = "DROP TABLE %s;" % (table_name, )
    cursor.execute(sql)

import csv

with open('boys.csv', newline='', encoding='utf-8') as csvfile:
    teams_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    team = []
    for i, row in enumerate(teams_reader):
        if i > 1:
            team.append(row)
        if len(team) == 3:
            print(team)
            t = Team()
            t.name = team[0][1]
            t.score = init_score
            t.save()
            team = []