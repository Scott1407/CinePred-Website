import streamlit as st
import pandas as pd
from PIL import Image
import base64
import numpy as np
import requests


#Background
@st.cache
def load_image(path):
    with open(path, 'rb') as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()
    return encoded


def image_tag(path):
    encoded = load_image(path)
    tag = f'<img src="data:image/png;base64,{encoded}">'
    return tag


def background_image_style(path):
    encoded = load_image(path)
    style = f'''
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded}");
        background-size: cover;
    }}
    </style>
    '''
    return style


image_path = '../images/b.jpeg'
image_link = 'https://www.google.com/search?q=background+black+&tbm=isch&ved=2ahUKEwiZkbSs9r30AhWSDGMBHfUmBJYQ2-cCegQIABAA&oq=background+black+&gs_lcp=CgNpbWcQAzIHCCMQ7wMQJzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDoGCAAQCBAeUOQKWKgUYLoWaABwAHgAgAFiiAHdBJIBAjEwmAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=tvakYZneKZKZjLsP9c2QsAk&bih=630&biw=1433&hl=en#imgrc=45B6kmexcKSPFM'



st.write(background_image_style(image_path), unsafe_allow_html=True)

# Side bar
make_choice = st.sidebar.selectbox('Pages:', ['New Movies','Create Your Own Movie'])

# First Page - New Movies Prediction
if make_choice == 'New Movies':
    '''
    # CinePred 🎥
    '''
    '''
    ## The Website Predicting The Next Blockbusters
    '''
    #Background image
    image_bat = Image.open('../images/Batman22.jpg')
    image_Jur = Image.open('../images/Jurassic.jpeg')
    image_wil = Image.open('../images/williams.jpeg')

    col1, col2, col3 = st.columns(3)
    col1.image(image_bat,caption='The Batman - April 2022',use_column_width="auto", width = 10)
    col2.image(image_Jur,
               caption='Jurassic World: Dominion - June 2022',
               use_column_width="auto")
    col3.image(image_wil,caption='King Richard - December 2021',use_column_width="auto")

    '''
    # Choose a movie going out soon 🍿
    '''

    title = st.text_input('Movie title', 'The Batman')
    st.write(f'Our revenue prediction for {title} is:')


    #prediction
    if st.button('Revenue Prediction'):
        st.write(' ## $100.000.000')
        st.balloons()

    #Side bar Image
    image_spider = Image.open('../images/Spiderman.jpeg')
    st.sidebar.image(image_spider,
                     caption='Spiderman - No Way Home',
                     use_column_width="auto")
    #audio
    audio_file = open('../images/music1.mp3', 'rb')
    audio_bytes = audio_file.read()
    st.sidebar.audio(audio_bytes, format='audio/ogg')




# Second Page - Create your movie
if make_choice == 'Create Your Own Movie':
    '''
    # Create your own movie 🎞️
    '''
    #Background Image
    image_roc = Image.open('../images/Rocky.jpg')
    image_sta = Image.open('../images/Star.jpeg')
    image_jum = Image.open('../images/jumanji.jpeg')

    col1, col2, col3 = st.columns(3)
    col1.image(image_roc,caption='Rocky IV',use_column_width="auto")
    col2.image(image_sta,
               caption='Star Wars: The Force Awakens',
               use_column_width="auto")
    col3.image(image_jum,caption='Jumanji',use_column_width="auto")

    def get_select_box_data():

        return pd.DataFrame({
            'director': [
                "Sylvester Stallone", "Steven Spielberg", "Martin Scorsese",
                "Quentin Tarantino", "James Cameron", "Spike Lee",
                "Alfred Hitchcock", "Francis Ford Coppola", " George Lucas",
                "Steven Soderbergh", "Ridley Scott", "Oliver Stone"
            ],
            'writer': [
                "Woody Allen", "Luc Besson", "John Hughes", "Spike Lee",
                "William Shakespeare", "Christopher Nolan", "Clint Eastwood",
                "Tim Burton", "John Hughes", "Steven Knight", "Mike Leigh",
                "John Sayles"
            ],
            'Prod': [
                "Walt Disney Pictures", "DreamWorks", "Lionsgate",
                "Universal Pictures", "Warner Bros", "Fox 2000 Pictures",
                "Gaumont", "Columbia Pictures", "Paramount Pictures",
                "Metro Goldwyn Mayer", "Miramax", "Hollywood Pictures"
            ],
            'main_actor': [
                "Brad Pitt", "Leonardo DiCaprio	", "Johnny Depp",
                "Robert Downey Jr.", "Will Smith", "Robert De Niro",
                "Dwayne Johnson", "Harrison Ford", "Tom Cruise",
                "Charlize Theron", "Bruce Willis", "Daniel Craig"
            ],
            'second_actor': [
                "Jean Dujardin", "Franck Dubosc", "Angelina Jolie",
                "Arnold Schwarzenegger", "Denzel Washington", "Vin Diesel",
                "Cameron Diaz", "George Clooney", "Mark Wahlberg",
                "Matt Damon", "Jason Statham", "Ben Stiller"
            ],
            'Genres': [
                "Drama", "Action", "Comedy", "Horror", "Thriller", "Romance",
                "Animation", "Adventure", "Comedy", "Drama, Romance", "Family",
                "Action, Thriller"
            ],
            'Month': [
                "January", "February", "March", "April", "May", "June", "July",
                "August", "September", "October", "November", "December"
            ]
        })


    df = get_select_box_data()

    director = st.selectbox('Select a Director', df['director'])
    filtered_dir = df[df['director'] == director]

    writer = st.selectbox('Select a Writer', df['writer'])
    filtered_w = df[df['writer'] == writer]

    production = st.selectbox('Select a Production Company', df['Prod'])
    filtered_pd = df[df['Prod'] == production]

    main_actor = st.selectbox('Select a Main Actor', df['main_actor'])
    filtered_ma = df[df['main_actor'] == main_actor]

    second_actor = st.selectbox('Select a Second Actor',df['second_actor'])
    filtered_sa = df[df['second_actor'] == second_actor]

    budget = st.slider("Select your Budget", min_value= 0, max_value=100_000_000, step=1_000_000)

    duration = st.slider("Select the duration of your movie", min_value= 60, max_value=180, step=5)

    genres = st.selectbox('Select a Genre', df['Genres'])
    filtered_cou = df[df['Genres'] == genres]

    #months = st.selectbox('Select a Genre', df['Month'])
    #filtered_month = df[df['Month'] == months]

    months = st.slider("Select the duration of your movie",
                         min_value=1,
                         max_value=12,
                         step=1)

    st.write(f"Our revenue prediction for your {genres} movie directed by {director}, written by {writer}, produced by {production}, with {main_actor}, and {second_actor}, for a budget of ${budget}, for a duration of {duration} minutes, going out in 0{months}/2022, is:")
    if st.button('Revenue Prediction'):

        parameters = {
        'Director': director,
        'Writer': writer,
        'Production Company': production,
        'Main Actor': main_actor,
        'Second Actor': second_actor,
        'Genres': genres,
        'Duration': duration,
        'Year': 2022,
        'Sin': np.sin(2 * np.pi * months / 12),
        'Cos': np.cos(2 * np.pi * months / 12)
        }
        response = requests.get(url = 'http://localhost:8000/predict')#, params=parameters)

        pred = response.json()
        st.write(pred)
        #st.write(pred["prediction"])
        #st.write(' ## $100.000.000')
        st.balloons()




    #Side bar Image

    image_avenger = Image.open('../images/Avengers.jpeg')
    st.sidebar.image(image_avenger, caption= 'Avengers - End Game', use_column_width="auto")



#url = 'https://taxifare.lewagon.ai/predict'

#if url == 'https://taxifare.lewagon.ai/predict':
