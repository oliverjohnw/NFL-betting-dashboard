import json
import os.path as osp

def read_json(*args):
    """
    Function to load a json file as a dictionary
    Parameters
    ----------
    args: List[str]
        input path to the json file to be read, separate arguments will be combined in to a single path: ie foo, bar, test.json -> foo/bar/test.json    
    Returns
    -------
    data: Dict[str, ?]
        json file as a dictionary
    """
    path = osp.join(*args)
    with open(path, 'r') as f:
        data = json.load(f)
    return data


def write_json(data: dict, *args, indent:int = 4, **kwargs) -> None:
    """
    Function to write a dictionary out to a json file --- according to the json standards, the dictionary keys must be strings
    Parameters 
    ----------
    data : dict
        dictionary to be written to a json file
    args : str
        path for the file to be written to
    kwargs : dict
        additional keyword arguments to json.dump
    """
    out_path = osp.join(*args)

    with open(out_path, 'w') as fp:
        json.dump(data, fp, indent=indent, **kwargs)

    return

def create_weekly_matchups(source_info):

    weekly_matchups = {}

    for i in range(len(source_info['events'])):
        weekly_matchups[source_info['events'][i]['description']] = 0

    return weekly_matchups


def create_weekly_game_source_info(source_info):

    weekly_game_info_dict = {}
    for i in range(len(source_info['events'])):
        weekly_game_info_dict[source_info['events'][i]['description']] = source_info['events'][i]['displayGroups'][0]['markets']

    return weekly_game_info_dict

def scrape_weekly_spreads(weekly_game_info_dict):
    weekly_spread_dict = {}
    for k,v in weekly_game_info_dict.items():
        for i in range(len(v)):
            if (v[i]['descriptionKey'] == "Main Dynamic Asian Handicap") & (v[i]['period']['description'] == "Game"):
                weekly_spread_dict[k] = [v[i]['outcomes'][0]['price']['handicap'], v[i]['outcomes'][0]['price']['american']]

    return weekly_spread_dict

def scrape_weekly_totals(weekly_game_info_dict):
    weekly_total_dict = {}
    for k,v in weekly_game_info_dict.items():
        for i in range(len(v)):
            if (v[i]['descriptionKey'] == "Main Dynamic Over/Under") & (v[i]['period']['description'] == "Game"):
                weekly_total_dict[k] = [v[i]['outcomes'][0]['price']['handicap'], v[i]['outcomes'][0]['price']['american']]


    return weekly_total_dict


