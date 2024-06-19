import streamlit as st

st.write("# 🧼 Data cleaning")

st.write("## Missing data")
rm_empty_rows_or_cols = st.checkbox("Remove empty rows or columns", True)

st.write("#### Replace missing values")
replace_methods = ["Mean","Median","Mode","KNN","Regression"]
replace_method = st.radio('Choose an option:', replace_methods)

st.write("## Normalize data")
normalize_methods = ["Min-Max","Z-Score","Another One"]
normalize_method = st.radio('Choose an option:', normalize_methods)

if st.button("Clean dataset"):
    # TODO: Actual processing
    st.write("TODO")
