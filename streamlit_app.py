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
#    conteúdo

#st.header('This is some header.')
st.subheader('Upload your Excel files')
st.text('Upload excel files with only one column, even if you put multiple columns only the first one will be used')
file_lookup = st.file_uploader("Lookup list", help="List with values to be matched, in the Left-join that's the left side")
file_match = st.file_uploader("Match list", help="List with values to match with, in the Left-join that's the right side")

st.subheader('Parâmetros')
threshold = st.slider("Similarity threshold", 0.0, 1.0, 0.7, help="Minimum similarity score to return, it goes from 0 to 1. If 1 it works exactly like a Left-join or Vlookup")
top = st.number_input("Enter a number", value=1, help="Maximum number of matches to return. If 1 it shows only the best match, if greater than 1 it shows multiple matches")

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
        xlsx_out = model.write_excel(dtf_out)        
        dtf_out
        
else:
    st.write('')

    
    
    
import base64

st.header("File Download - A Workaround for small data")

text = """\
    There is currently (20191204) no official way of downloading data from Streamlit. See for
    example [Issue 400](https://github.com/streamlit/streamlit/issues/400)

    But I discovered a workaround
    [here](https://github.com/holoviz/panel/issues/839#issuecomment-561538340).

    It's based on the concept of
    [HTML Data URLs](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Data_URIs)

    You can try it out below for a dataframe csv file download.

    The methodology can be extended to other file types. For inspiration see
    [base64.guru](https://base64.guru/converter/encode/file)
    """
st.markdown(text)

data = [(1, 2, 3)]
# When no file name is given, pandas returns the CSV as a string, nice.
df = pd.DataFrame(data, columns=["Col1", "Col2", "Col3"])
csv = df.to_csv(index=False)
b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
href = f'<a href="data:file/csv;base64,{b64}">Download CSV File</a> (right-click and save as &lt;some_name&gt;.csv)'
st.markdown(href, unsafe_allow_html=True)
