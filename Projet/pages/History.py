import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import mpld3
import streamlit.components.v1 as components
import os
import seaborn as sns

import src.utils as utils
from src.components.Wave.Wave import make_wave
from src.components.Modal.Modal import make_modal
from src.components.CardGraphic.CardGraphic import make_card_graphic
from src.components.FontBookBackground.FontBookBackground import make_font_book_background
from src.components.FontTextBackground.FontTextBackground import make_font_text_background
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

path = "pages/css/History"
colors = ['#F5B7B1', '#9F5F9E', '#85C1E9', '#E3A98C']
#colors = ['#E5B793', '#9F5F9E', '#5494C3', '#E3A98C']  # Couleurs plus foncées

# on le met aussi debut pour pas faire ramer l'app
spark_book_1 = SparkSession.builder .appName("book_1").getOrCreate()
spark_book_2 = SparkSession.builder .appName("book_2").getOrCreate()
print("hey")
df_book_1 = spark_book_1.read.csv("static/data/book_data.csv", header=True)
df_book_2 = spark_book_2.read.csv("static/data/book_data_2.csv", header=True)
df_books_3= pd.read_csv('static/data/book_data_3.csv')

df_book_1.createOrReplaceTempView("livres")
df_book_2.createOrReplaceTempView("livres")

df_book_1_cleaned = df_book_1.filter(df_book_1['genres'].like('%|%'))
df_book_2 = df_book_2.na.drop()

def history_page():

    utils.import_css(st,path+"/History.css")
    st.title("Analyse de la littérature")

    #st.markdown('<h1 class="title_story">Analyse de la littérature</h1>', unsafe_allow_html=True)
    make_wave(st,"La lecture existe depuis aussi longtemps que l'écriture, c'est à dire à la préhistoire, avec les peintures.","📜 Un peu de culture ! 📜",openLascaux)
    utils.make_jump(st)
    make_font_book_background(st,"130 millions de livres uniques","En 2010, d'après les études de Google, il n'existerait pas moins de :")
    utils.make_jump(st)
    make_wave(st,"Évidemment, ce sont des chiffres estimatifs et à l'heure de la digitalisation et d'internet, il est fort probable que ce nombre soit déjà bien supérieur. \n Aujourd'hui, il existe également énormément de lecteurs, que ça soit occasionnels ou aguéris, et pour n'importe quel type de lecture")
   
    utils.make_jump(st)
    make_graphics_repartition_books()
    utils.make_jump(st)
    make_wave(st,"Beaucoup de livres, et une grande part de lecture, oui... Mais pour quelles raisons ?")
    utils.make_jump(st)
    make_font_text_background(st,"Genre, âge, expérience, goût, catégorie de livre ... \n Il est impossible d'estimer le nombre de livre qui pourraient convenir à un unique individu, mais il est possible de trouver un livre qui pourrait convenir à ses goûts", "Une histoire rien que pour vous","📚 Quelques facteurs ! 📚",openMentalCard)
    utils.make_jump(st)
    make_wave(st,"Pour vous donnez une petite idée... Saviez-vous que ce ne sont pas les personnes âgées qui lisent le plus? ")
    utils.make_jump(st)
    make_graphics_repartition_age_reading()
    utils.make_jump(st)
    make_wave(st,"Et pour briser les mythes... Sont-ce les femmes, ou bien les hommes qui lisent le plus ?")
    utils.make_jump(st)
    make_graphic_repartition_per_genre()
    utils.make_jump(st)
    make_wave(st,"Cela dit... De nos jours, avec autant de livres et de lecteurs... \nQu'en est-il de leur qualité, aux yeux des lecteurs ?")
    utils.make_jump(st)

    make_graphic_repartition_grade()
    make_research_book()
    utils.make_jump(st)
    utils.make_jump(st)
    make_font_book_background(st,"Même sans chercher \nvous pouvez trouver !","Il y a tellement de facteur à prendre en compte... \n C'est pour cela qu'on peut dire qu'il existe forcément un livre qui vous \n conviendra à la perfection !")

def openLascaux():
    make_modal(st,"L'art de la communication dans les temps anciens","PeintureLascaux.jpg","Peinture présente dans la grotte de Lascaux, dans le sud-ouest de la France")

def openMentalCard():
    make_modal(st,"Et vous, pourquoi lisez-vous?","categories_mental_card.jpg","Liste non exaustive des facteurs de lecture pour un individu ")


def make_graphics_repartition_books():
    img_name = "repartition_genres_livres.png"
    path_image = "static/" + img_name
    genres_distincts = df_book_1_cleaned.select(explode(split(df_book_1_cleaned['genres'], '\|')).alias('genre')).distinct().orderBy('genre')   
    if os.path.exists(path_image):
        make_card_graphic(st,"Top 20 des genres de livres les plus courant",img_name)
        ################### dropdown 
        utils.make_jump(st)
        selected_genre = st.selectbox("Sélectionner un genre", genres_distincts)
        count_genre = df_book_1_cleaned.filter(df_book_1_cleaned['genres'].like(f'%{selected_genre}%')).count()
        
        st.write(f"Genre : {selected_genre} - {count_genre} livres.")
        return
    resultats = df_book_1_cleaned.select(explode(split(df_book_1_cleaned['genres'], '\|')).alias('genre')) \
                        .join(genres_distincts, 'genre') \
                        .groupBy('genre') \
                        .agg(count('*').alias('nb_livres')) \
                        .orderBy('genre')

    resultats_tries = resultats.orderBy(resultats['nb_livres'].desc()).limit(20)

    resultats_liste = resultats_tries.collect()

    genres = [row['genre'] for row in resultats_liste[::-1]]
    nb_livres = [row['nb_livres'] for row in resultats_liste[::-1]]

    fig, ax = plt.subplots(figsize=(15, 10), facecolor='none')
    ax.barh(genres, nb_livres, color=colors)
    ax.set_xlabel('Nombre de livres')
    ax.set_ylabel('Genre')
    plt.xticks(rotation=45, ha='right')
    ax.patch.set_facecolor('none')

    #plt.show()
    #st.pyplot(fig)
    plt.savefig(path_image,dpi=300)
    #fig_html = mpld3.fig_to_html(fig)
    #components.html(fig_html, height=600)
    make_graphics_repartition_books()


def make_graphics_repartition_age_reading():
    img_name = "repartition_lecture_age.png"
    path_image = "static/" + img_name
    if os.path.exists(path_image):
        make_card_graphic(st,"Proportion des lecteurs par tranche d'âge",img_name, classNameList="little")
        utils.make_jump(st)
        return
    df_age_avg = df_book_2.groupBy("User-ID").agg(avg("Age").alias("avg_age"))

    df_with_age_groups = df_age_avg.withColumn(
        "age_group",
        when(col("avg_age") <= 18, "0-18")
        .when((col("avg_age") > 18) & (col("avg_age") <= 25), "19-25")
        .when((col("avg_age") > 25) & (col("avg_age") <= 50), "26-50")
        .otherwise("51-120")
    )
    age_group_counts = df_with_age_groups.groupBy('age_group').count()
    total_users = df_with_age_groups.count()
    age_group_percentage = age_group_counts.withColumn('percentage', (age_group_counts['count'] / total_users) * 100)

    age_group_percentage_pandas = age_group_percentage.toPandas()

    fig, ax = plt.subplots(figsize=(5, 5),facecolor='none')
    ax.pie(age_group_percentage_pandas['percentage'], labels=age_group_percentage_pandas['age_group'], autopct='%.1f%%', colors=colors)
    ax.axis('equal')

    ax.patch.set_facecolor('none')

    plt.savefig(path_image,dpi=300)
    make_graphics_repartition_age_reading()


def make_graphic_repartition_per_genre():
    img_name = "repartition_per_genre.png"
    path_image = "static/" + img_name
    if os.path.exists(path_image):
        make_card_graphic(st,"Proportion des lecteurs par genre",img_name, classNameList="medium_1")
        utils.make_jump(st)
        return
    df_users = pd.read_excel('static/data/01_user.xlsx', sheet_name='Result 1')
    df_users_book = pd.read_excel('static/data/04_user_book.xlsx', sheet_name='Result 1')

    merged_data = pd.merge(df_users_book, df_users, on='user_id', how='inner')

    user_counts = merged_data['user_id'].value_counts().reset_index()
    user_counts.columns = ['user_id', 'count']

    total_users = len(user_counts)

    male_users = merged_data[merged_data['gender'] == 'M']['user_id'].nunique()
    female_users = merged_data[merged_data['gender'] == 'F']['user_id'].nunique()
    other_users = merged_data[~merged_data['gender'].isin(['M', 'F'])]['user_id'].nunique()

    male_proportion =  np.round(male_users / total_users, 2)
    female_proportion =  np.round(female_users / total_users, 2)
    other_users_proportion =  np.round(other_users / total_users, 2)

    labels = ['Hommes', 'Femmes', 'Autres']
    sizes = [male_proportion, female_proportion, other_users_proportion]

    fig, ax = plt.subplots(figsize=(8, 8),facecolor='none')
    ax.pie(sizes, labels=labels, autopct='%.1f%%', colors=colors)
    ax.axis('equal')

    ax.patch.set_facecolor('none')

    plt.savefig(path_image,dpi=300)

    make_graphic_repartition_per_genre()


def make_graphic_repartition_grade():
    img_name = "repartition_grade.png"
    path_image = "static/" + img_name
    if os.path.exists(path_image):
        make_card_graphic(st,"Distribution des notes",img_name)
        utils.make_jump(st)
        return

    df_books_3_cleaned = df_books_3[df_books_3['CountsOfReview'] >= 100]

    sns.set_style("whitegrid")
    plt.figure(figsize=(10,6))
    sns.histplot(df_books_3_cleaned, x="Rating", kde=True, palette=colors)
    plt.xlabel('Note')
    plt.ylabel('Nombre de livres')
    #plt.show()

    plt.savefig(path_image, dpi=300, transparent=True)

    make_graphic_repartition_grade()



def make_research_book():
    recherche = st.text_input("Entrez l'ISBN ou le nom du livre :")

    if recherche:
        note = search_book_grade(recherche)
        if note is not None :
            st.write(f"La note du livre est : {note:.2f}")

            df_filtre = df_books_3[df_books_3['ISBN'].astype(str).str.lower() == recherche]
            fig, ax = plt.subplots(figsize=(8, 6),facecolor='none')
            ax.bar(['Nombre de commentaires', 'Note'], [df_filtre['CountsOfReview'].iloc[0], df_filtre['Rating'].iloc[0]],color=colors[:2])
            ax.set_ylabel('Valeurs')
            ax.set_title('Nombre de commentaires par rapport à la note')
            ax.patch.set_facecolor('none')
            st.pyplot(fig)
        else:
            st.write("Aucun livre trouvé avec cette recherche.")


def search_book_grade(recherche):
    recherche = recherche.lower()
    
    df_filtre = None
    if len(recherche) == 10:
        print(recherche)
        df_filtre = df_books_3[df_books_3['ISBN'] == recherche]
        print(df_filtre)
    else :
        df_filtre = df_books_3[df_books_3['Name'].str.lower().str.contains(recherche, na=False)]
        
    if not df_filtre.empty:
        note = df_filtre.iloc[0]['Rating']
        return note

    return None


if __name__ == "__main__":
    history_page()
    with open("index.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

