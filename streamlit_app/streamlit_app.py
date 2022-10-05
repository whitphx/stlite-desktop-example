import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("stlite desktop demo app")

df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(df)

size = st.slider("Sample size", 100, 1000, 100)
arr = np.random.normal(1, 1, size=size)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)
