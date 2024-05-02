import src.utils as utils
path = "src/components/CardGraphic"
image_path = "./app/static/"

def make_card_graphic(st,legend, image,style="",classNameImageList="", classNameList = ""):
    #st.button(label ,on_click=on_click)
    utils.import_css(st,path+ "/CardGraphic.css")
     #            <div class="button button--piyo" style={{ scale: "0.8" }} onClick={onClick}>
    print(classNameImageList)
    st.markdown(
        f"""
        <div class="image_container {classNameList}" >
            <div class="border_image">
                <img style="{style}"class="{"image_main " + classNameImageList}" src={image_path + image} /><br></br>
                <div class="legend_image">{legend} </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

     