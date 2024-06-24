import streamlit as st
import pandas as pd
import sys
sys.path.append('./back/')

import clustering_csv as cc
import prediction as p

def display_prediction_results(df, targetCol):
    df_cols.remove(col)
    original_col = df[col]
    predicted_col = p.getColumnsForPredictionAndPredict(df, df_cols, "Route Type", "Linear Regression")    
    
    new_df = pd.DataFrame()
    new_df['Original'] = original_col
    new_df['Predicted'] = predicted_col

    st.dataframe(new_df)    

if 'df' in st.session_state:
    df = st.session_state.df
    df_cols = df.columns.tolist()

    st.write("# 🔮 Prediction")

    if st.button("K-means"):
        st.pyplot(cc.launch_cluster_knn(df, ["Route Type", "Traffic Control"]))

    if st.button("DBSCAN"):
        st.pyplot(cc.launch_cluster_dbscan(df, ["Route Type", "Traffic Control"]))

    if st.button("Linear Regression"):
        col = "Route Type"
        display_prediction_results(df, col)

    if st.button("Random Forest"):
        col = "Route Type"
        display_prediction_results(df, col)
else:
    st.write("Please clean your dataset.")
