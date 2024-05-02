import src.utils as utils
path = "src/components/Modal"
image_path = "./app/static/"

def make_modal(st,title,img, description,imgClass = ""):
    #st.button(label ,on_click=on_click)
    utils.import_css(st,path+ "/Modal.css")
     #            <div class="button button--piyo" style={{ scale: "0.8" }} onClick={onClick}>

    st.markdown(
        f"""
        <div class="darkBG"/>
            <div class="centered">
                <div class="modal">
                    <div class="modalHeader">
                        <h5 class="heading">{title}</h5>
                    </div>
                    <div className="closeBtn">
                        [R]
                    </div>
                    <div class="modalContent" >
                            <img src={image_path+img} class={imgClass}></img>
                            <div class="legend_modal">{description} </div>
                    </div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # appuyer sur R pour fermer... Pas trouver mieux dans streamlit


def close():
    print("close")
     