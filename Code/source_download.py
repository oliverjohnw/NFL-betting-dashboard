import argparse
import logging
import requests
from utils import write_json

def parse_args() -> argparse.Namespace:
    """Function to parse command line arguments"""

    parser = argparse.ArgumentParser()
    parser.add_argument('source_output_path', type=str, help='Path to the save source info')
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
            logging.FileHandler('source_config.log'),
            logging.StreamHandler()
            ]
        )

    args = parse_args()

    logging.info("Fetching Source Information")

    # scrape NFL information
    source = requests.get("https://www.bovada.lv/services/sports/event/v2/events/A/description/football/nfl").json()
    source_data = source[0]

    # save source info
    logging.info("Saving Source Information")
    write_json(source_data, args.source_output_path)

    return

if __name__ == '__main__':
    main()