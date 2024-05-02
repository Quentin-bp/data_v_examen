import os
import src.utils as utils
path = "src/components/FontTextBackground"
image = "./app/static/text_font.jpg" #https://github.com/streamlit/static-file-serving-demo/blob/main/streamlit_app.py
from src.components.Button.Button import make_button_modal 
def make_font_text_background(st,description, main,description_modal="", onclick ="",_class= ""):
    #st.button(label ,on_click=on_click)
    utils.import_css(st,path+ "/FontTextBackground.css")
     #            <div className="button button--piyo" style={{ scale: "0.8" }} onClick={onClick}>
    with st.container():
        st.markdown(f""" 
            <div class={"font_text_main " + _class}> 
                <img src="{image}">
                <div class="section">
                    <div class="text_container"> {description}<br>
                        <span className="title">{main} </span> 
                    </div>
                </div>
            </div>

        """,    unsafe_allow_html=True)
        if (description_modal != "" and onclick != ""):
            make_button_modal(st,description_modal,onclick)