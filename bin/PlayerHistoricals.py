import numpy as np
import pandas as pd

print ("Dependencies Loaded")

pd.set_option('display.max_columns',20)
pd.set_option('display.max_rows',100)
pd.set_option('display.width',320)
np.set_printoptions(linewidth=320)

#2020Seasons Master Team List CSV
teamslist = pd.read_csv('../data/2020-21/teams.csv')

#LoadInThePlayerData from 2019 - 2017
raw2020Data = pd.read_csv('../data/2020-21/cleaned_players.csv')
raw2019Data = pd.read_csv('../data/2019-20/cleaned_players.csv')
raw2018Data = pd.read_csv('../data/2018-19/cleaned_players.csv')
raw2017Data = pd.read_csv('../data/2017-18/cleaned_players.csv')
raw2016Data = pd.read_csv('../data/2016-17/cleaned_players_v1.csv',encoding='windows-1252')
print ('PlayerData Loaded')


#column titles of interest from the csv
#second_name
#first_name
#team
#team_code

###TeamID seems to be difff from code in the 2020 teamsList so im mapping a name search's team_code
###to the 2020 list's CODE values and hence got arsenal [i was getting brighton before which is wrong]

#print ("Team Is")
#teamcode = sampleplayerFile.loc[sampleplayerFile.second_name == "Mustafi"].team_code[6]
#print (teamslist.loc[teamslist.code == teamcode])

#Lets Assume We Need All The Data On A GivenPlayer
#D1 = raw2018Data.loc[raw2018Data.second_name == playerSecondName].index[0]
#print (raw2018Data.loc[D1])

playerSecondName = 'Lacazette'
#Lets make a historical
S20 = raw2020Data.loc[raw2020Data.second_name == playerSecondName]
S19 = raw2019Data.loc[raw2019Data.second_name == playerSecondName]
S18 = raw2018Data.loc[raw2018Data.second_name == playerSecondName]
S17 = raw2017Data.loc[raw2017Data.second_name == playerSecondName]
S16 = raw2016Data.loc[raw2016Data.second_name == playerSecondName]

rawPlayerData = []
#We wont append S20's Data as yet (as its identical to S19)
rawPlayerData.append(S20)
rawPlayerData.append(S19)
rawPlayerData.append(S18)
rawPlayerData.append(S17)
rawPlayerData.append(S16)

cleanedPlayerData = []
for i in rawPlayerData:
    if i.empty == False:
        cleanedPlayerData.append(i)

print (cleanedPlayerData)