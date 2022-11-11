import logging
import pandas as pd
from utils import read_json


def main():
    """Main Function"""
    # setup logger
    formatstr = '%(asctime)s: %(levelname)s: %(funcName)s Line: %(lineno)d %(message)s'
    datestr = '%m/%d/%Y %H:%M:%S'
    logging.basicConfig(
        level=logging.INFO, 
        format=formatstr, 
        datefmt=datestr, 
        handlers=[
            logging.FileHandler('betting_config.log'),
            logging.StreamHandler()
            ]
        )

    defense_df = pd.read_csv('../Input/PFF_Grades/defense_summary.csv')
    blocking_df = pd.read_csv('../Input/PFF_Grades/offense_blocking.csv')
    passing_df = pd.read_csv('../Input/PFF_Grades/passing_summary.csv')
    receiving_df = pd.read_csv('../Input/PFF_Grades/receiving_summary.csv')
    rushing_df = pd.read_csv('../Input/PFF_Grades/rushing_summary.csv')

    pass_rush = defense_df[(defense_df['position'] == 'DI') | (defense_df['position'] == 'ED') | (defense_df['position'] == 'LB')][['player', 'position', 'team_name', 'grades_pass_rush_defense']]
    rush_defense = defense_df[(defense_df['position'] == 'DI') | (defense_df['position'] == 'ED') | (defense_df['position'] == 'LB') | (defense_df['position'] == 'S')][['player', 'position', 'team_name', 'grades_run_defense']]
    pass_coverage = defense_df[(defense_df['position'] == 'CB') | (defense_df['position'] == 'S') | (defense_df['position'] == 'LB')][['player', 'position', 'team_name', 'grades_coverage_defense']]

    pass_block = blocking_df[(blocking_df['position'] == "T") | (blocking_df['position'] == "C") | (blocking_df['position'] == "G")][['player', 'position', 'team_name', 'grades_pass_block']]
    run_block = blocking_df[(blocking_df['position'] == "T") | (blocking_df['position'] == "C") | (blocking_df['position'] == "G") | (blocking_df['position'] == "TE")][['player', 'position', 'team_name', 'grades_run_block']]
    qb_pass = passing_df[passing_df['position'] == "QB"][['player', 'position', 'team_name', 'grades_pass']]
    rush = rushing_df[(rushing_df['position'] == 'HB') | (rushing_df['position'] == 'QB')][['player', 'position', 'team_name', 'grades_run']]
    receive = receiving_df[(receiving_df['position'] == "WR") | (receiving_df['position'] == "RB") | (receiving_df['position'] == "TE")][['player', 'position', 'team_name', 'grades_offense']]

    pass_rush.rename(columns = {'player': 'Player',
    'position': 'Position',
    'team_name': 'Team',
    'grades_pass_rush_defense' : 'Grade'}, inplace = True)

    rush_defense.rename(columns = {'player': 'Player',
    'position': 'Position',
    'team_name': 'Team',
    'grades_run_defense' : 'Grade'}, inplace = True)

    pass_coverage.rename(columns = {'player': 'Player',
    'position': 'Position',
    'team_name': 'Team',
    'grades_coverage_defense' : 'Grade'}, inplace = True)

    pass_block.rename(columns = {'player': 'Player',
    'position': 'Position',
    'team_name': 'Team',
    'grades_pass_block' : 'Grade'}, inplace = True)

    run_block.rename(columns = {'player': 'Player',
    'position': 'Position',
    'team_name': 'Team',
    'grades_run_block' : 'Grade'}, inplace = True)

    qb_pass.rename(columns = {'player': 'Player',
    'position': 'Position',
    'team_name': 'Team',
    'grades_pass' : 'Grade'}, inplace = True)

    rush.rename(columns = {'player': 'Player',
    'position': 'Position',
    'team_name': 'Team',
    'grades_run' : 'Grade'}, inplace = True)

    receive.rename(columns = {'player': 'Player',
    'position': 'Position',
    'team_name': 'Team',
    'grades_offense' : 'Grade'}, inplace = True)

    pass_rush.to_csv('../Output/PFF_Grades/pass_rush.csv', index = False)
    rush_defense.to_csv('../Output/PFF_Grades/rush_defense.csv', index = False)
    pass_coverage.to_csv('../Output/PFF_Grades/pass_coverage.csv', index = False)
    pass_block.to_csv('../Output/PFF_Grades/pass_block.csv', index = False)
    run_block.to_csv('../Output/PFF_Grades/run_block.csv', index = False)
    qb_pass.to_csv('../Output/PFF_Grades/qb_pass.csv', index = False)
    rush.to_csv('../Output/PFF_Grades/rush.csv', index = False)
    receive.to_csv('../Output/PFF_Grades/receive.csv', index = False)

    return

if __name__ == '__main__':
    main()