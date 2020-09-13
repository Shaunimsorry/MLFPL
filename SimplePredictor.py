import numpy as np
import pandas as pd
import tensorflow as tf

print ("Dependencies Loaded")
#Formatting Changes
pd.set_option('display.max_columns',20)
pd.set_option('display.max_rows',100)
pd.set_option('display.width',320)
np.set_printoptions(linewidth=320)

#Fetching Player Data
cleaned2019_Playerdata = pd.read_csv('data/2019-20/cleaned_players.csv')
cleaned2018_Playerdata = pd.read_csv('data/2018-19/cleaned_players.csv')
cleaned2017_Playerdata = pd.read_csv('data/2017-18/cleaned_players.csv')

#FetchFixturesData
season2019_fixtures = pd.read_csv('data/2019-20/fixtures.csv')
season2018_fixtures = pd.read_csv('data/2018-19/fixtures.csv')

#MappingTests since we are playing in the 2020/2021 season we dont care about relegated teams
teamCodes2021 = pd.read_csv('data/2020-21/teams.csv')

#Mapping Historical Data To Current teams [also maapping example]
season2018_fixtures['team_h'] = season2018_fixtures['team_h'].map(teamCodes2021.set_index('id')['name'])
season2018_fixtures['team_a'] = season2018_fixtures['team_a'].map(teamCodes2021.set_index('id')['name'])
season2019_fixtures['team_h'] = season2019_fixtures['team_h'].map(teamCodes2021.set_index('id')['name'])
season2019_fixtures['team_a'] = season2019_fixtures['team_a'].map(teamCodes2021.set_index('id')['name'])

#Basic Match Historical Data using Only data from 2018/2019
slim19Fixtures = season2019_fixtures[['team_a',
                                        'team_a_difficulty',
                                        'team_a_score',
                                        'team_h',
                                        'team_h_difficulty',
                                        'team_h_score']]

slim18Fixtures = season2018_fixtures[['team_a',
                                        'team_a_difficulty',
                                        'team_a_score',
                                        'team_h',
                                        'team_h_difficulty',
                                        'team_h_score']]
print (slim19Fixtures.head(100))