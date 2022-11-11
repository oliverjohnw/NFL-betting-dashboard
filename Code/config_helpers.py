import pandas as pd

def parse_matchups_info(source_info):
    """
    Function to create a dictionary of weekly matchups
    Parameters 
    ----------
    source_info : dict
        dictionary containing source information

    Returns
    -------
    matchups_dict : dict
        dictionary of weekly matchups and all betting info
    """
    matchups_info_dict = dict()

    for i in range(len(source_info['events'])):
        matchups_info_dict[source_info['events'][i]['description']] = source_info['events'][i]['displayGroups'][0]['markets']

    return matchups_info_dict


def scrape_weekly_spreads(matchups_info_dict):
    """
    Function to create spread information for weekly matchups
    Parameters 
    ----------
    matchups_info_dict : dict
        dictionary of weekly matchups and all betting info

    Returns
    -------
    weekly_spread_dict : dict
        dictionary of spreads for each game
    """
    weekly_spread_dict = {}
    for k,v in matchups_info_dict.items():
        for i in range(len(v)):
            if (v[i]['descriptionKey'] == "Main Dynamic Asian Handicap") & (v[i]['period']['description'] == "Game"):
                weekly_spread_dict[k] = {'Spread Info': [v[i]['outcomes'][0]['price']['handicap'], v[i]['outcomes'][0]['price']['american']]}

    return weekly_spread_dict

def scrape_weekly_totals(matchups_info_dict):
    """
    Function to create totals information for weekly matchups
    Parameters 
    ----------
    matchups_info_dict : dict
        dictionary of weekly matchups and all betting info

    Returns
    -------
    weekly_tota;_dict : dict
        dictionary of total for each game
    """
    weekly_total_dict = {}
    for k,v in matchups_info_dict.items():
        for i in range(len(v)):
            if (v[i]['descriptionKey'] == "Main Dynamic Over/Under") & (v[i]['period']['description'] == "Game"):
                weekly_total_dict[k] = {'Total Info': [v[i]['outcomes'][0]['price']['handicap'], v[i]['outcomes'][0]['price']['american']]}

    return weekly_total_dict
