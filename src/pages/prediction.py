import streamlit as st
import pandas as pd
import sys
sys.path.append('./back/')

import clustering_csv as cc
import prediction as p

def handle_column_multiselect(df, method_name):
    selected_columns = st.multiselect(f"Select the columns you want for {method_name}:", df.columns.tolist(), placeholder="Select dataset columns")
    return selected_columns
    
def display_prediction_results(df, targetCol, sourceColumns, method):
    original_col = df[targetCol]
    predicted_col = p.getColumnsForPredictionAndPredict(df, sourceColumns, targetCol, method)    
    
    new_df = pd.DataFrame()
    new_df['Original'] = original_col
    new_df['Predicted'] = predicted_col

    st.dataframe(new_df)    

if 'df' in st.session_state:
    df = st.session_state.df

    st.write("# 🔮 Prediction")

    tab1, tab2 = st.tabs(["Clustering", "Predictions"])

    with tab1:
        st.header("Clustering")
        selected_columns = handle_column_multiselect(df, "clustering")
            
        
        tab_names = ["K-means", "DBSCAN"] 
        tab11, tab12 = st.tabs(tab_names)

        with tab11:
            if st.button(f"Start {tab_names[0]}"):
                st.pyplot(cc.launch_cluster_knn(df, selected_columns))

        with tab12:
            if st.button(f"Start {tab_names[1]}"):
                st.pyplot(cc.launch_cluster_dbscan(df, selected_columns))

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
        tab21, tab22 = st.tabs(tab_names)

        with tab21:
            if st.button(f"Start {tab_names[0]}"):
                st.write(target_column)
                st.write(selected_columns_p)
                display_prediction_results(df, target_column, selected_columns_p, tab_names[0])

        with tab22:
            if st.button(f"Start {tab_names[1]}"):
                display_prediction_results(df, target_column, selected_columns_p, tab_names[1])
else:
    st.write("Please clean your dataset.")
