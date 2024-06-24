import streamlit as st
import sys
sys.path.append('./back/')

import managing_missing_values as mmv
import load_csv as lc

if 'original_df' in st.session_state:
    df = st.session_state.original_df

    st.write("# 🧼 Data cleaning")

    st.write("## Missing data")
    rm_empty_rows_or_cols = st.checkbox("Remove empty rows or columns", True)


    st.write("#### Replace missing values")
    replace_methods = ["mean","median","mode","knn","regression"]
    replace_method = st.radio('Choose an option:', replace_methods)

    st.write("## Normalize data")
    normalize_methods = ["min-max","z-score","robust"]
    normalize_method = st.radio('Choose an option:', normalize_methods)

    is_cleaned = st.button("Clean dataset")
    if is_cleaned:
        if rm_empty_rows_or_cols:
            st.write("-  Removing hight null percentage values")
            df = mmv.drop_high_null_percentage(df)
            st.dataframe(df)

        st.write("- Handle missing values with method:", replace_method)
        df = mmv.handle_missing_values(df, replace_method)
        st.session_state.df = df
        st.dataframe(df)

        st.write("- Normalize with method:", normalize_method)
        df = lc.handle_normalization(df, normalize_method)
        st.session_state.df = df
        st.dataframe(df)

        st.switch_page("pages/visualize.py")
else:
    st.write("Please upload you dataset.")
