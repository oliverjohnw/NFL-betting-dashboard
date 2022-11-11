#!/bin/bash

echo "Starting source"
python source_download.py ../Output/Configs/source_week10.json

echo "Starting Betting Info"
python generate_bet_info.py ../Output/Configs/source_week10.json ../Output/Configs/spread_week10.json ../Output/Configs/total_week10.json

echo "Starting PFF Info"
python pff_generate.py

echo "Complete"

