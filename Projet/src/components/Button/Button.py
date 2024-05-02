
import src.utils as utils
from src.components.Modal.Modal import make_modal
path = "src/components/Button"

def make_button(st,label,redirection):
    #st.button(label ,on_click=on_click)
    utils.import_css(st,path+ "/Button.css")
     #            <div className="button button--piyo" style={{ scale: "0.8" }} onClick={onClick}>

    st.markdown(
        f"""
        <div style="justify-content: center; display: flex;">
            <div class="button button--piyo" style="scale: 0.8">
                <div class="button__wrapper">
                    <span class="button__text">{label}</span>
                </div>
                <div class="characterBox">
                    <div class="character wakeup">
                        <div class="character__face"></div>
                    </div>
                    <div class="character wakeup">
                        <div class="character__face"></div>
                    </div>
                    <div class="character">
                        <div class="character__face"></div>
                    </div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    with st.container():
        st.markdown('<div class="custom-button-container">', unsafe_allow_html=True)
        if st.button("Redirection", key="custom_button"):
            utils.switch_page(redirection)
        st.markdown('</div>', unsafe_allow_html=True)


     
def make_button_modal(st,label,onClick):
    #st.button(label ,on_click=on_click)
    utils.import_css(st,path+ "/Button.css")
     #            <div className="button button--piyo" style={{ scale: "0.8" }} onClick={onClick}>

    st.markdown(
        f"""
        <div style="justify-content: center; display: flex;" class="wave_button_modal">
            <div class="button button--piyo" style="scale: 0.8">
                <div class="button__wrapper">
                    <span class="button__text">{label}</span>
                </div>
                <div class="characterBox">
                    <div class="character wakeup">
                        <div class="character__face"></div>
                    </div>
                    <div class="character wakeup">
                        <div class="character__face"></div>
                    </div>
                    <div class="character">
                        <div class="character__face"></div>
                    </div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    with st.container():
        st.markdown('<div class="custom-button-container wave_button_modal">', unsafe_allow_html=True)
        if st.button("Redirection", key=label):
            onClick()
        st.markdown('</div>', unsafe_allow_html=True)
