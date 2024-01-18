# Here, we are using sports reference API to collect NBA game information, and storing in a DataFrame.

from sportsipy.nba.teams import Teams
from sportsipy.nba.schedule import Schedule
import time
import pandas as pd
import numpy as np


def collect_data():
    print("Starting out Sports Data Collection")

    teams = Teams()
    print(teams)

    team_dfs = []
    for team in teams:
        teamdataframe = team.dataframe
        team_dfs.append(teamdataframe)

    team_df = pd.concat(team_dfs, axis=0, ignore_index= False)

    team_abbreviations = ['CHI','BRK', 'MIA', 'MIL', 'PHI', 'CLE', 'CHO', 'TOR', 'WAS', 'BOS', 'NYK', 'ATL', 'IND', 'DET', 'ORL',
                        'PHO', 'GSW', 'UTA', 'MEM', 'DAL', 'DEN', 'LAL', 'LAC', 'MIN', 'POR', 'SAS', 'SAC', 'NOP', 'OKC', 'HOU']


    schedule_dfs = []
    for basketballteam in team_abbreviations:
        teamschedule = Schedule(basketballteam)

        individual_df = teamschedule.dataframe
        names = [basketballteam] * len(teamschedule)
        individual_df['Team_Name'] = names
        schedule_dfs.append(individual_df)
        time.sleep(60)

    schedule_df = pd.concat(schedule_dfs, axis=0, ignore_index= False)
    schedule_df.to_csv("secondsportsdataset.csv")

    team_df.to_csv("firstsportsdataset.csv")
    return



collect_data()