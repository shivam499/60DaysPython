import streamlit as st
from PIL import Image

# for camera to take the photo
# with st.expander("Start Camera"):
#     camera_image = st.camera_input("Camera")

# to upload photo from computer
with st.expander("Upload Image"):
    camera_image = st.file_uploader("Upload Image")

if camera_image:
    img = Image.open(camera_image)

    gray_image = img.convert("L")
    st.image(gray_image)
