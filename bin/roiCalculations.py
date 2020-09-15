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
cleaned2016Data = pd.read_csv('../data/2016-17/cleaned_players.csv', encoding='windows-1252')
print ('PlayerData Loaded')

#import 2020 raw player data
raw2020PlayerData = pd.read_csv('../data/2020-21/players_raw.csv')
#import 2020 TeamsList
fpl_teams_data = pd.read_csv('../data/2020-21/teams.csv')

#Lets Setup a list of players
EPLfpl2020_PlayerList = []

#Load in the previous GWData
gw_keyword = 'gw1'
gw_data = pd.read_csv('../data/2020-21/gws/'+str(gw_keyword)+'.csv')

#player_db = [['first_name','second_name','team','2020Season_points','2019Season_points', '2018Season_points', '2017Season_points']]
player_db = [['first_name',
              'second_name',
              'team',
              'position',
              'this round chance',
              'next round chance',

              '2020Season_points',
              '2020Season_cost',
              '2020Season_roi',

              '2019Season_points',
              '2019Season_cost',
              '2019Season_roi',

              '2018Season_points',
              '2018Season_cost',
              '2018Season_roi',

              '2017Season_points',
              '2017Season_cost',
              '2017Season_roi',

              'average_ROI']]

player_tempRowCount = 0

##THis is just a sample:
# while player_tempRowCount < (cleaned2020Data.shape[0]):
#     #attempt to find the team name
#     playerSecondName = cleaned2020Data.loc[player_tempRowCount].second_name
#     playerTeamId = raw2020PlayerData.loc[raw2020PlayerData.second_name == playerSecondName].team.index[0]
#     playerTeamName = fpl_teams_data.loc[fpl_teams_data.id == raw2020PlayerData.loc[playerTeamId].team].name.index[0]
#     player_team_shortName = (fpl_teams_data.loc[playerTeamName].short_name)
#
#     #Make sure to keep the shape of this identical to the one above
#     newDatabase.append(
#         [cleaned2020Data.loc[player_tempRowCount].first_name,
#          cleaned2020Data.loc[player_tempRowCount].second_name,
#          player_team_shortName,
#          cleaned2020Data.loc[player_tempRowCount].total_points,
#          cleaned2020Data.loc[player_tempRowCount].now_cost])
#     player_tempRowCount = player_tempRowCount + 1
# print ("Finished Setting Up Player List")
#
# #Setupthe Dataframe
# dataFrame = pd.DataFrame(newDatabase)
# print (dataFrame)

while player_tempRowCount < cleaned2020Data.shape[0]:
    #Code To Decant The Team Code
    player_firstName = cleaned2020Data.loc[player_tempRowCount].first_name
    player_secondName = cleaned2020Data.loc[player_tempRowCount].second_name
    player_index = raw2020PlayerData.loc[raw2020PlayerData.second_name == player_secondName].index[0]
    playerTeamName = fpl_teams_data.loc[fpl_teams_data.id == raw2020PlayerData.loc[player_index].team].name.index[0]
    player_team_shortName = (fpl_teams_data.loc[playerTeamName].short_name)

    #Remap the data into the dynamic GWSheet
    playerNameString = str(str(player_firstName+" "+str(player_secondName)))
    playerGW_index = gw_data.loc[gw_data.name == playerNameString]

    #I noticed some players are in the cleaned2020 sheet but now in the GW sheet must ask why

    #Decant Chance of playing COP
    player_thisRoundChance = raw2020PlayerData.loc[player_index].chance_of_playing_this_round
    player_nextRoundChance = raw2020PlayerData.loc[player_index].chance_of_playing_next_round









    #Code To Decant 2019 total points of a player in THIS season

    player_2019_index = cleaned2019Data.loc[cleaned2019Data.second_name == player_secondName]
    #Check if this player even played in the 2019 Season and log a value for total_points
    if player_2019_index.empty == False:
        player_2019_index = cleaned2019Data.loc[cleaned2019Data.second_name == player_secondName].index[0]
        player_2019_total_points = cleaned2019Data.loc[player_2019_index].total_points
        player_2019_now_cost = cleaned2019Data.loc[player_2019_index].now_cost
    else:
        player_2019_now_cost = -1
        player_2019_total_points = -1

    #Repeat process for 2018
    player_2018_index = cleaned2018Data.loc[cleaned2018Data.second_name == player_secondName]
    if player_2018_index.empty == False:
        player_2018_index = cleaned2018Data.loc[cleaned2018Data.second_name == player_secondName].index[0]
        player_2018_total_points = cleaned2018Data.loc[player_2018_index].total_points
        player_2018_now_cost= cleaned2018Data.loc[player_2018_index].now_cost
    else:
        player_2018_now_cost = -1
        player_2018_total_points = -1

    #Repeat process for 2017
    player_2017_index = cleaned2017Data.loc[cleaned2017Data.second_name == player_secondName]
    if player_2017_index.empty == False:
        player_2017_index = cleaned2017Data.loc[cleaned2017Data.second_name == player_secondName].index[0]
        player_2017_total_points = cleaned2017Data.loc[player_2017_index].total_points
        player_2017_now_cost = cleaned2017Data.loc[player_2017_index].now_cost
    else:
        player_2017_now_cost = -1
        player_2017_total_points = -1

    #Build data for the average ROI calculation
    #Must change if player did NOT play in previous seasons

    player_avg3s_now_cost = 0
    player_avg3s_total_points = 0
    player_avg3s_roi = 0

    if player_2017_now_cost != -1:
        player_avg3s_now_cost = player_avg3s_now_cost + player_2017_now_cost
        player_avg3s_total_points = player_avg3s_total_points + player_2017_total_points

    if player_2018_now_cost != -1:
        player_avg3s_now_cost = player_avg3s_now_cost + player_2018_now_cost
        player_avg3s_total_points =  player_avg3s_total_points + player_2018_total_points

    if player_2019_now_cost != -1:
        player_avg3s_now_cost = player_avg3s_now_cost + player_2019_now_cost
        player_avg3s_total_points = player_avg3s_total_points + player_2019_total_points

    player_avg3s_now_cost =  player_avg3s_now_cost + cleaned2020Data.loc[player_tempRowCount].now_cost
    player_avg3s_total_points = player_avg3s_total_points + cleaned2020Data.loc[player_tempRowCount].total_points



    player_avg3s_roi = player_avg3s_total_points / player_avg3s_now_cost


    #Making the list before dataframe baking
    player_db.append([
        cleaned2020Data.loc[player_tempRowCount].first_name,
        cleaned2020Data.loc[player_tempRowCount].second_name,
        player_team_shortName,
        cleaned2020Data.loc[player_tempRowCount].element_type,
        player_thisRoundChance,
        player_nextRoundChance,

        cleaned2020Data.loc[player_tempRowCount].total_points,
        cleaned2020Data.loc[player_tempRowCount].now_cost,
        #ROI
        cleaned2020Data.loc[player_tempRowCount].total_points / cleaned2020Data.loc[player_tempRowCount].now_cost,

        player_2019_total_points,
        player_2019_now_cost,
        #ROI
        player_2019_total_points /  player_2019_now_cost,

        player_2018_total_points,
        player_2018_now_cost,
        #ROI
        player_2018_total_points / player_2018_now_cost,

        player_2017_total_points,
        player_2017_now_cost,
        #ROI
        player_2017_total_points / player_2017_now_cost,

        #Average 3Season ROI
        player_avg3s_roi



    ])

    player_tempRowCount = player_tempRowCount + 1
visual_dataFrame = pd.DataFrame(player_db)
print ("Printing Visual Reference")
print (visual_dataFrame)

player_db.remove(player_db[0])
dataFrame = pd.DataFrame(player_db)

