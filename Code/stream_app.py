import streamlit as st
import pandas as pd

from utils import read_json

spread_dict = read_json('../Output/Configs/spread_week10.json')
total_dict = read_json('../Output/Configs/total_week10.json')

pass_block = pd.read_csv('../Output/PFF_Grades/pass_block.csv')
pass_coverage = pd.read_csv('../Output/PFF_Grades/pass_coverage.csv')
pass_rush = pd.read_csv('../Output/PFF_Grades/pass_rush.csv')
qb_pass = pd.read_csv('../Output/PFF_Grades/qb_pass.csv')
receive = pd.read_csv('../Output/PFF_Grades/receive.csv')
run_block = pd.read_csv('../Output/PFF_Grades/run_block.csv')
rush_defense = pd.read_csv('../Output/PFF_Grades/rush_defense.csv')
rush = pd.read_csv('../Output/PFF_Grades/rush.csv')

team_info = read_json('../Input/teams.json')

st.title ("NFL Betting Dashboard")
st.header("Week 10 Games")

for k,v in spread_dict.items():
    away_team = str(k.split(" @")[0])
    home_team = str(k.split("@ ")[1])

    mapped_away = team_info[away_team]
    mapped_home = team_info[home_team]

    if float(v['Spread Info'][0]) >= 0:
        spread_sign = "-"
    else:
        spread_sign = "+"

    st.subheader(f"{k}")
    st.caption(f"Spread: {home_team} {spread_sign}{v['Spread Info'][0]} ({v['Spread Info'][1]})")
    st.caption(f"Total O/U: {total_dict[k]['Total Info'][0]} ({total_dict[k]['Total Info'][1]})")



