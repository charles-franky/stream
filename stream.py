import streamlit as st
import mymodel as m
st.write("""
# Sales model
Below are our sales predictions
for this customer.
""")
window = st.slider("Forecast window(days)")
st.write(m.run(window=window))
