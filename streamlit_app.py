from model.string_matcher import StringMatcher
import pandas as pd
import streamlit as st

"""
# Strings Matcher
Texto explicativo em markdown
"""

# form ainda não disponível na cloud
#with st.form(key='my_form'):
#    conteúdo do form
#    submit_button = st.form_submit_button(label='Submit')
#if submit_button:
#    st.write(f'threshold = {threshold}')

#st.header('This is some header.')
st.subheader('Upload your Excel files')
st.text('Upload excel files with only one column, even if you put multiple columns only the first one will be used')
file_lookup = st.file_uploader("Lookup list", help="List with values to be matched, in the Left-join that's the left side")
file_match = st.file_uploader("Match list", help="List with values to match with, in the Left-join that's the right side")

st.subheader('Parâmetros')
threshold = st.slider("Similarity threshold", 0.0, 1.0, 0.7, help="Minimum similarity score to return, it goes from 0 to 1. If 1 it works exactly like a Left-join or Vlookup")
top = st.number_input("Enter a number", value=1, help="Maximum number of matches to return. If 1 it shows only the best match, if greater than 1 it shows multiple matches")

if st.button('Submit'):
    st.write(f'threshold = {threshold}')

    if file_lookup is not None:
        file_lookup
        
        #bytes_data = file_lookup.getvalue()
        #st.write(bytes_data)

        dataframe = pd.read_excel(file_lookup["dtf_lookup"])
        #st.write(dataframe)
        st.write("entrou")
    else:
        st.write('aqui')

    if file_match is not None:
        file_match
    else:
        st.write('aqui 2')
        
    #dtf_lookup = pd.read_excel(file_lookup["dtf_lookup"])
    #dtf_match = pd.read_excel(file_match["dtf_match"])
       
    #dtf_lookup = pd.read_excel(flask.request.files["dtf_lookup"])
    #dtf_match = pd.read_excel(flask.request.files["dtf_match"])
    #threshold = float(flask.request.form["threshold"])
    #top = 1 if flask.request.form["top"].strip() == "" else int(flask.request.form["top"])
    #app.logger.warning("--- Inputs Received ---")

    ## match
    model = StringMatcher(dtf_lookup, dtf_match)
    dtf_out = model.vlookup(threshold=threshold, top=top)
    xlsx_out = model.write_excel(dtf_out)
    
else:
    st.write('')
