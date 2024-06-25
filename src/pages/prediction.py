import streamlit as st
import pandas as pd
import sys
import matplotlib.pyplot as plt
import numpy as np
sys.path.append('./back/')

import clustering_csv as cc
import prediction as p

def handle_column_multiselect(df, method_name):
    selected_columns = st.multiselect(f"Select the columns you want for {method_name}:", df.columns.tolist(), placeholder="Select dataset columns")
    return selected_columns
    
def df_prediction_results(df, targetCol, sourceColumns, method):
    original_col = df[targetCol]
    predicted_col = p.getColumnsForPredictionAndPredict(df, sourceColumns, targetCol, method)
    
    new_df = pd.DataFrame()
    new_df['Original'] = original_col
    new_df['Predicted'] = predicted_col

    return new_df

if 'df' in st.session_state:
    df = st.session_state.df

    st.write("# 🔮 Prediction")

    tab1, tab2 = st.tabs(["Clustering", "Predictions"])

    with tab1:
        st.header("Clustering")
        selected_columns = handle_column_multiselect(df, "clustering")

        if len(selected_columns) >= 3:
            dimensions = st.radio("Reduce to dimensions X with PCA:",[2,3],index=0)
        else:
            dimensions = 2
        
        tab_names = ["K-means", "DBSCAN"] 
        cluster_tabs = st.tabs(tab_names)

        for idx, tab in enumerate(cluster_tabs):
            if tab.button(f"Start {tab_names[idx]}"):
                if tab_names[idx] == "K-means":
                    fig = cc.launch_cluster_knn(df, selected_columns, dimensions=dimensions)
                else:
                    fig = cc.launch_cluster_dbscan(df, selected_columns, dimensions)

                tab.pyplot(fig)

    with tab2:
        st.header("Predictions")
        target_column = st.selectbox(
                            "Target column:",
                            df.columns.tolist(),
                            index=None,
                            placeholder="Select target column"
                        )

        if target_column != None:
            selected_columns_p = handle_column_multiselect(df, "predictions")
        
        tab_names = ["Linear Regression", "Random Forest"] 
        prediction_tabs = st.tabs(tab_names)

        for idx, tab in enumerate(prediction_tabs):
            if tab.button(f"Start {tab_names[idx]}"):
                tab.pyplot(p.correlation_matrix(df, selected_columns_p+[target_column]))
                tmp_df = df_prediction_results(df, target_column, selected_columns_p, tab_names[idx])
                tab.dataframe(tmp_df)
else:
    st.write("Please clean your dataset.")
