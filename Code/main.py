import streamlit as st
import pandas as pd

from utilities import read_json

spread_dict = read_json('../Output/spread_info.json')
total_dict = read_json('../Output/total_info.json')

st.title ("NFL Betting Dashboard")
st.header("Week 5 Games")

for k,v in spread_dict.items():
    spread_team_var = k.split(" @")[0]

    if float(v[0]) >= 0:
        spread_sign = "+"
    else:
        spread_sing = "-"

    st.subheader(f"{k}")
    st.caption(f"Spread: {spread_team_var} {spread_sign}{v[0]} ({v[1]})")
    st.caption(f"Total O/U: {total_dict[k][0]} ({total_dict[k][1]})")


st.subheader("this is the subheader")
st.caption("this is the caption")
st.code("x=2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''') 