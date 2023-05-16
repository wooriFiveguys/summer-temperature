import streamlit as st
from PIL import Image
import os

original_header = '<div style = "font-size:50px;display:inline;">🤭5조 </div><div style = "color:red;font-size:50px;display:inline;">\"초\"미니 </div><div style = "font-size:50px;display:inline;">프로젝트🤭</div>'
st.markdown(original_header,unsafe_allow_html=True)
image_file = '기상청.jpg'
folder = '/data/'
image_path = os.path.dirname(os.path.abspath(__file__))+folder+image_file
image=Image.open(image_path)

st.image(image)
