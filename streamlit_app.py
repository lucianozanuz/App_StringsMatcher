from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""


#with st.echo(code_location='below'):
threshold = st.slider("Similarity threshold", 0.7, 0, 1, help='Minimum similarity score to return, it goes from 0 to 1. If 1 it works exactly like a Left-join or Vlookup')
top_matches = st.st.number_input("Enter a number", value=1, help="Maximum number of matches to return. If 1 it shows only the best match, if greater than 1 it shows multiple matches")
