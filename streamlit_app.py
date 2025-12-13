import streamlit as st

st.title("Room Design AI App")

image = st.file_uploader("Upload room image", type=["jpg","png"])

if image:
    st.image(image, caption="Original Room")

