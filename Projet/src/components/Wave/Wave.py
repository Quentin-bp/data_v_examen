
import os
import src.utils as utils
import streamlit as st
from streamlit import config
from src.components.Button.Button import make_button_modal
path = "src/components/Wave"
image = "./app/static/wave.png" #https://github.com/streamlit/static-file-serving-demo/blob/main/streamlit_app.py
def make_wave(st,label,description = "",onClick= "", _class= ""):
    #st.button(label ,on_click=on_click)
    utils.import_css(st,path+ "/Wave.css")
    st.markdown(f""" <div className={"wave_container " + _class}>  
                <img src="{image}"><div className="wave_text_container">{label}<br></br>
                    <br></br>
                </div>
                </div>
                """, unsafe_allow_html=True)
    if (description != "") and (onClick != ""):
        make_button_modal(st,description,onClick)