from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Strings Matcher
Texto explicativo em markdown
"""

with st.form(key='my_form'):
    #st.header('This is some header.')
    st.subheader('Upload your Excel files')
    st.text('Upload excel files with only one column, even if you put multiple columns only the first one will be used')
    file_lookup = st.file_uploader("Lookup list", help="List with values to be matched, in the Left-join that's the left side")
    file_match = st.file_uploader("Match list", help="List with values to match with, in the Left-join that's the right side")

    st.subheader('Parâmetros')
    threshold = st.slider("Similarity threshold", 0.0, 1.0, 0.7, help="Minimum similarity score to return, it goes from 0 to 1. If 1 it works exactly like a Left-join or Vlookup")
    top_matches = st.number_input("Enter a number", value=1, help="Maximum number of matches to return. If 1 it shows only the best match, if greater than 1 it shows multiple matches")

    submit_button = st.form_submit_button(label='Submit')
    
if submit_button:
    st.write(f'threshold = {threshold}')
    
with st.echo(code_location='below'):
    total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))
