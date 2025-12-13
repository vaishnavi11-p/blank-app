import streamlit as st
import time

# App title
st.title("Room Design AI App")

# Image upload
image = st.file_uploader("Upload room image", type=["jpg", "png"])

if image:
    st.image(image, caption="Original Room")

# Room type selection
room_type = st.selectbox(
    "Select Room Type",
    ["Bedroom", "Living Room", "Office"],
    key="room_type"
)

# Design style selection
style = st.selectbox(
    "Select Design Style",
    ["Modern", "Minimalist", "Luxury"],
    key="design_style"
)

# Single button only
if st.button("Design My Room", key="design_btn"):
    with st.spinner("AI is redesigning your room..."):
        time.sleep(2)   # simulate AI work

    st.success("Design Completed!")

    st.subheader("AI Design Suggestions 🧠")

    st.write(f"""
    **Room Type:** {room_type}  
    **Style Chosen:** {style}

    ### Suggested Design:
    - Use light and neutral wall colors
    - Add minimal furniture to increase space
    - Prefer warm lighting for comfort
    - Place plants or artwork for aesthetics
    """)
