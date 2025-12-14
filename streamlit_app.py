import streamlit as st
import time
from PIL import Image

# App title
st.title("Room Design AI App 🏠")

# Upload room image
image = st.file_uploader("Upload room image", type=["jpg", "png"])

if image:
    st.image(image, caption="Original Room", use_container_width=True)

# Select room type
room_type = st.selectbox(
    "Select Room Type",
    ["Bedroom", "Living Room", "Office"],
    key="room_type"
)

# Select design style
style = st.selectbox(
    "Select Design Style",
    ["Modern", "Minimalist", "Luxury"],
    key="design_style"
)

# Button
if st.button("Design My Room", key="design_btn"):
    with st.spinner("AI is redesigning your room..."):
        time.sleep(2)

    st.success("Design Completed!")

    # Load AI redesigned image (demo)
    if style == "Modern":
        redesigned_image = Image.open("sample_designs/modern.jpg")
    elif style == "Minimalist":
        redesigned_image = Image.open("sample_designs/minimalist.jpg")
    else:
        redesigned_image = Image.open("sample_designs/luxury.jpg")

    # Show redesigned room
    st.subheader("AI Redesigned Room ✨")
    st.image(redesigned_image, caption=f"{style} {room_type}", use_column_width=True)

    # AI suggestions
    st.subheader("AI Design Suggestions 🧠")
    st.write(f"""
    **Room Type:** {room_type}  
    **Design Style:** {style}

    - Optimized furniture placement  
    - Better lighting balance  
    - Color palette matching the style  
    - Space-efficient layout  
    """)
