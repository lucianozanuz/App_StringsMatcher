from model.string_matcher import StringMatcher
import base64
import pandas as pd
import streamlit as st

def get_table_download_link(df):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    href = f'<a href="data:file/csv;base64,{b64}">Download csv file</a> (right-click and save as &lt;some_name&gt;.csv)'
    return href
    
"""
# Strings Matcher
Using the *pairwise cosine similarity* technique
"""

# form ainda não disponível na cloud
#with st.form(key='my_form'):
#    conteúdo do form
#    submit_button = st.form_submit_button(label='Submit')
#if submit_button:
#    conteúdo

#st.header('This is some header.')
st.subheader('Upload your Excel files')
st.text('Upload excel files with only one column, even if you put multiple columns only the first one will be used')
file_lookup = st.file_uploader("Lookup list", help="List with values to be matched, in the Left-join that's the left side")
file_match = st.file_uploader("Match list", help="List with values to match with, in the Left-join that's the right side")

st.subheader('Parâmetros')
threshold = st.slider("Similarity threshold", 0.0, 1.0, 0.7, help="Minimum similarity score to return, it goes from 0 to 1. If 1 it works exactly like a Left-join or Vlookup")
top = st.number_input("Top matches", value=1, help="Maximum number of matches to return. If 1 it shows only the best match, if greater than 1 it shows multiple matches")

if st.button('Submit'):
    if file_lookup is not None:
        dtf_lookup = pd.read_excel(file_lookup)
    else:
        st.write('file_lookup empty')

    if file_match is not None:
        dtf_match = pd.read_excel(file_match)
    else:
        st.write('file_match empty')
        
    if file_lookup is not None and file_match is not None:
        model = StringMatcher(dtf_lookup, dtf_match)
        dtf_out = model.vlookup(threshold=threshold, top=top)
        xlsx_out = model.write_excel(dtf_out) # todo: download xlsx_out file
        st.markdown(get_table_download_link(dtf_out), unsafe_allow_html=True)
        dtf_out
        
else:
    st.write('')
