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

if st.button("Design My Room"):
    st.write("Designing your room...")
    
if st.button("Design My Room"):
    st.success("Design request received!")
    st.write("Room Type:", room_type)
    st.write("Design Style:", style)
