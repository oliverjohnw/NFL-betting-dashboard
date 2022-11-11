import argparse
import logging
from utils import read_json, write_json
from config_helpers import parse_matchups_info, scrape_weekly_spreads, scrape_weekly_totals

def parse_args() -> argparse.Namespace:
    """Function to parse command line arguments"""

    parser = argparse.ArgumentParser()
    parser.add_argument('source_info_path', type=str, help='Path to the source info')
    parser.add_argument('spread_dict_path', type=str, help='Path to the save spread dictionary')
    parser.add_argument('totals_dict_path', type=str, help='Path to the save totals dictionary')
    args = parser.parse_args()

    return args

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

    args = parse_args()

    logging.info("Loading source info")
    source_info = read_json(args.source_info_path)

    weekly_matchup_dict = parse_matchups_info(source_info)
    weekly_spread_dict = scrape_weekly_spreads(weekly_matchup_dict)
    weekly_totals_dict = scrape_weekly_totals(weekly_matchup_dict)

    logging.info("Saving configs")
    write_json(weekly_spread_dict, args.spread_dict_path)
    write_json(weekly_totals_dict, args.totals_dict_path)

    return

if __name__ == '__main__':
    main()