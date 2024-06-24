import streamlit as st
import matplotlib.pyplot as plt

import sys
sys.path.append('./back/')

import show_csv as sc

if 'df' in st.session_state:

    df = st.session_state.df
    df_columns = df.columns.tolist()

    st.write("# 📊 Visualization")

    st.write("## Histograms")
    hist_tabs = st.tabs(df_columns)

    for idx, tab in enumerate(hist_tabs):
        tab.write("##### "+df_columns[idx])
        tab.pyplot(sc.histo_col(df, df_columns[idx]))

    st.write("## Box & Whisker")
    baw_tabs = st.tabs(df_columns)

    for idx, tab in enumerate(baw_tabs):
        tab.write("##### "+df_columns[idx])
        fig, ax = plt.subplots()
        df[df_columns[idx]].plot(kind='box')
        tab.pyplot(fig)
else:
    st.write('Please clean your dataset.')
