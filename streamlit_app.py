import streamlit as st

st.title("Room Design AI App")

image = st.file_uploader("Upload room image", type=["jpg","png"])

if image:
    st.image(image, caption="Original Room")

room_type = st.selectbox(
    "Select Room Type",
    ["Bedroom", "Living Room", "Office"]
)

style = st.selectbox(
    "Select Design Style",
    ["Modern", "Minimalist", "Luxury"]
)

