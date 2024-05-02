import streamlit as st
import src.utils as utils
from src.components.Button.Button import make_button
path_css = "pages/css/Home"

def home_page():
    #st.title("Accueil")
    mochi_peach = utils.make_gif("images/mochi-peach.gif")
    milk_and_mocha = utils.make_gif("images/milk-and-mocha-cute.gif")
    #st.image("images/milk-and-mocha-cute.gif", width=200)
    utils.import_css(st,path_css+"/Home.css")
    utils.import_css(st,path_css+"/particles.css")
    st.markdown("&nbsp;"*2000)
    make_button(st,"Un peu d'histoire ?","History")
    st.markdown(
        f"""
        
        <div class="particle-container">                 
                <div class="particles"><span class="circle"></span><span class="circle 1"></span><span class="circle 2"></span><span class="circle 3"></span><span class="circle 4"></span><span class="circle 5"></span><span class="circle 6"></span><span class="circle 7"></span><span class="circle 8"></span><span class="circle 9"></span><span class="circle 10"></span><span class="circle 11"></span><span class="circle 12"></span><span class="circle 13"></span><span class="circle 14"></span><span class="circle 15"></span><span class="circle 16"></span><span class="circle 17"></span><span class="circle 18"></span><span class="circle 19"></span><span class="circle 20"></span><span class="circle 21"></span><span class="circle 22"></span><span class="circle 23"></span><span class="circle 24"></span><span class="circle 25"></span><span class="circle 26"></span><span class="circle 27"></span><span class="circle 28"></span><span class="circle 29"></span></div>
        </div>
            <div id="home_page">
                <img src="data:image/gif;base64,{mochi_peach}" class="mochi_picture" alt="mochi_peach">
                <img src="data:image/gif;base64,{milk_and_mocha}" class="mochi_slap_picture" alt="milk_and_mocha"><br>
            </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    home_page()
    with open("index.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)