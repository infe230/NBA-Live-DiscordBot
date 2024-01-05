import datetime
from nba_api.stats.endpoints import commonallplayers
from scripts.general_functions import *
from table2ascii import table2ascii as t2a, PresetStyle

def lookup_player(player_name):
    players_endpoint = commonallplayers.CommonAllPlayers()
    players_data = players_endpoint.get_data_frames().iloc[:, :4]  # Limiting columns for simplicity

    # Search for the player by name
    player_name = player_name.lower()
    matching_players = players_data[players_data.apply(lambda row: player_name in f"{row['FIRST_NAME']} {row['LAST_NAME']}".lower(), axis=1)]

    return matching_players

def create_player_table(players_data):
    table = []
    headers = ['First Name', 'Last Name', 'Team', 'Position']
    
    # Add headers to the table
    table.append(headers)

    # Add player data to the table
    for _, player in players_data.iterrows():
        table.append([player['FIRST_NAME'], player['LAST_NAME'], player['TEAM_ABBREVIATION'], player['POS']])

    return table
