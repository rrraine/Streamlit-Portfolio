import streamlit as st
from streamlit_drawable_canvas import st_canvas

st.title("🎨 Canvas Test")

canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",
    stroke_width=3,
    stroke_color="#000000",
    background_color="#ffffff",
    height=300,
    width=700,
    drawing_mode="freedraw",
    key="canvas_test",
)

if canvas_result.image_data is not None:
    st.write("✅ Canvas rendered successfully!")
