#This Script Aims to calculate all the ROI's of all the current players in the EPL FPL Season against all their previous appeareances for ROI calculations.

import numpy as np
import pandas as pd
import json
import requests as r

#Formatting
pd.set_option('display.max_columns',20)
pd.set_option('display.max_rows',100)
pd.set_option('display.width',320)
np.set_printoptions(linewidth=320)

#FPL API
fplapi_endpoint = 'https://fantasy.premierleague.com/api/bootstrap-static/'

#import historical cleaned data
cleaned2020Data = pd.read_csv('../data/2020-21/cleaned_players.csv', header=0)
cleaned2019Data = pd.read_csv('../data/2019-20/cleaned_players.csv')
cleaned2018Data = pd.read_csv('../data/2018-19/cleaned_players.csv')
cleaned2017Data = pd.read_csv('../data/2017-18/cleaned_players.csv')
cleaned2016Data = pd.read_csv('../data/2016-17/cleaned_players_v1.csv', encoding='windows-1252')
print ('PlayerData Loaded')

#import 2020 raw player data
raw2020PlayerData = pd.read_csv('../data/2020-21/players_raw.csv')
#import 2020 TeamsList
fpl_teams_data = pd.read_csv('../data/2020-21/teams.csv')

#Lets Setup a list of players
EPLfpl2020_PlayerList = []

newDatabase = [['first_name','second_name','team','total_points','now_cost',]]

player_tempRowCount = 0
while player_tempRowCount < (cleaned2020Data.shape[0]):
    #attempt to find the team name
    playerSecondName = cleaned2020Data.loc[player_tempRowCount].second_name
    playerTeamId = raw2020PlayerData.loc[raw2020PlayerData.second_name == playerSecondName].team.index[0]
    playerTeamName = fpl_teams_data.loc[fpl_teams_data.id == raw2020PlayerData.loc[playerTeamId].team].name.index[0]
    player_team_shortName = (fpl_teams_data.loc[playerTeamName].short_name)

    #Make sure to keep the shape of this identical to the one above
    newDatabase.append(
        [cleaned2020Data.loc[player_tempRowCount].first_name,
         cleaned2020Data.loc[player_tempRowCount].second_name,
         player_team_shortName,
         cleaned2020Data.loc[player_tempRowCount].total_points,
         cleaned2020Data.loc[player_tempRowCount].now_cost])
    player_tempRowCount = player_tempRowCount + 1
print ("Finished Setting Up Player List")

#Setupthe Dataframe
dataFrame = pd.DataFrame(newDatabase)
print (dataFrame)

