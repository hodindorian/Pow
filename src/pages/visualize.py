import streamlit as st
import matplotlib.pyplot as plt

df = st.session_state.orig_df
df_columns = df.columns.tolist()

st.write("# 📊 Visualization")

st.write("## Histograms")
hist_tabs = st.tabs(df_columns)

for idx, tab in enumerate(hist_tabs):
    tab.write("##### "+df_columns[idx])
    tab.bar_chart(df[df_columns[idx]])

st.write("## Box & Whisker")
baw_tabs = st.tabs(df_columns)

for idx, tab in enumerate(baw_tabs):
    tab.write("##### "+df_columns[idx])
    fig, ax = plt.subplots()
    df[df_columns[idx]].plot(kind='box')
    st.pyplot(fig)
