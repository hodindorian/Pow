import streamlit as st
import pandas as pd
import sys
sys.path.append('./back/')

import clustering_csv as cc
import prediction as p

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
        df_cols.remove(col)
        original_col = df[col]
        predicted_col = p.getColumnsForPredictionAndPredict(df, df_cols, "Route Type", "Linear Regression")

    if st.button("Random Forest"):
        col = "Route Type"
        df_cols.remove(col)
        original_col = df[col]
        predicted_col = p.getColumnsForPredictionAndPredict(df, df_cols, "Route Type", "Random Forest")

    ndf = pd.DataFrame()
    ndf['Original'] = original_col
    ndf['Predicted'] = predicted_col

    st.dataframe(ndf)

else:
    st.write("Please clean your dataset.")
