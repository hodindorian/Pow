import streamlit as st
from io import StringIO
import pandas as pd

def  statistics(df):
    nan_counts = df.isnull().sum(axis=1).sum()

    st.write("*Number of columns*:", len(df.columns))
    st.write("*Number of rows*:", len(df.index))
    
    st.write("*Nan Counts*: ", nan_counts)
    st.write(df.isna().sum())

def display_df_first_and_lasts_lines(df):
    fl = df.head(10)
    ll = df.tail(10)
    concat = pd.concat([fl, ll])
    st.dataframe(concat)

def nav_bar():
    st.page_link("./home.py", label="Import", icon="⬆️", help=None)
    st.page_link("pages/clean.py", label="Clean", icon="🧼", help=None)
    st.page_link("pages/visualize.py", label="Visualize", icon="👁️", help=None)
    st.page_link("pages/prediction.py", label="Predict", icon="🔮", help=None)
    st.page_link("pages/evaluate.py", label="Evaluate", icon=None, help=None)

def clean_dataframe(line):
    # Call to function to clean data
    line.empty()
    line.write("Dataframe has been cleaned")

def main():
    nav_bar()
    st.write("# Pow: Your data analyser")

    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.session_state.orig_df = df
        st.write("## Dataframe (10 first/last lines)")
        display_df_first_and_lasts_lines(df)

        st.write("## Statistics")
        statistics(df)

        if st.button("Next"):
            st.switch_page("pages/clean.py")

main()
