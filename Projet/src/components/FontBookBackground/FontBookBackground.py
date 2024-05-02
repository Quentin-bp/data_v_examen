import os
import src.utils as utils
path = "src/components/FontBookBackground"
image = "./app/static/font_book1.jpg" #https://github.com/streamlit/static-file-serving-demo/blob/main/streamlit_app.py

def make_font_book_background(st,main,description,_class= ""):
    #st.button(label ,on_click=on_click)
    utils.import_css(st,path+ "/FontBookBackground.css")
     #            <div className="button button--piyo" style={{ scale: "0.8" }} onClick={onClick}>
    with st.container():
        st.markdown(f""" 
            <div class={"font_book_main " + _class}> 
                <img src="{image}"><div class="section"><div class="text_container">{description}<br><span className="title">{main} </span></div>
                </div>
            </div>

""",    unsafe_allow_html=True)