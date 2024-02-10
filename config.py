import streamlit as st
import importlib.util
from pathlib import Path

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# focasting data apple (AAPL) Historical Stock Data 👋")

IMAGE_PATH = "44.jpeg"  # Replace "path_to_your_image.jpg" with the actual path to your image file

# Add image to the sidebar
st.sidebar.image(IMAGE_PATH, use_column_width=True)
st.sidebar.success("Select a above.")

PAGE_PATHS = {
    "Home": Path(r"C:\Users\Lenovo\tubes\home.py"),
    "About Data ": Path(r"C:\Users\Lenovo\tubes\about.py"),
    "Visualization": Path(r"C:\Users\Lenovo\tubes\expalantion.py"),
    "Conclusion": Path(r"C:\Users\Lenovo\tubes\app.py"),
}
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(PAGE_PATHS.keys()), key="nav")
page = None
if selection:
    page_path = PAGE_PATHS[selection]
    spec = importlib.util.spec_from_file_location(selection, page_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    page = module
if page:
    st.title(page.title)
    page.run()
    
st.sidebar.write("M HAIKAL")