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
    with st.spinner("AI is redesigning your room..."):
        st.sleep(2)

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
