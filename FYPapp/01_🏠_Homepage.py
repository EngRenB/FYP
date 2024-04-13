
#this is the main file which contains the interface for the system

#imported packages 
import streamlit as st 
import pandas as pd
from PIL import Image

#link python files that contain the preprocessing and the classification
#import Preprocessing

#import logo
logo = Image.open(r"/Users/Ren/fypvenv/FYPapp/Logo.png")

#page title and logo
st.set_page_config('CyperParent', page_icon= logo)


#columns to organize the page 
col1, col2 = st.columns([2,2])

#header
st.title("**CyperParent**")
st.markdown("#### is an ML model to detect grooming in textual and image files")
st.write("If you’re worried about the content of your child's chats please upload the file and **we will take care of it**")

#recieve a file as an input 
file = st.file_uploader("")

#hide made by streamlit and main menue 
hide_st_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)