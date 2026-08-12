import pandas as pd 
import numpy as np
import streamlit as st
import joblib
import os 

st.set_page_config(
    page_title='Movie Recommendation System',
    page_icon="🎥",
    layout='centered'
)
import requests

def fetch_poster_by_id(movie_id):
    api_key = "57a45b8e1ac3adaeb3d5a089431b7e01"
    
    # ID base structural URL
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        # Response se raw image path text nikalna
        poster_path = data['poster_path']
        
        # Pura final live image link banana
        full_image_url = "https://image.tmdb.org/t/p/w500" + poster_path
        return full_image_url
    except:
        # Agar image na miley ya internet issue ho toh broken check image dikhein
        return "https://placeholder.com"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR,'models','clean_data.pkl')
FUNC_PATH=os.path.join(BASE_DIR,'models','recommed_function.pkl')
SIMILARITI_PATH=os.path.join(BASE_DIR, 'models'  , 'similarity.pkl')
# Movies Data

try:
    with open(DATA_PATH ,'rb') as f:
        movies=joblib.load(f)
    print("✅ Model loaded successfully!")
except FileNotFoundError:
    st.write("❌ data load nia howa")
    # print(f"❌ ERROR: Model not found at {DATA_PATH}")
    # print("   Make sure you saved 'best_model.pkl' in the 'models' folder.")
    movies = None  # Set to None so we can check later

# getting  similarity  function 
try:
    with open(SIMILARITI_PATH, 'rb') as f:
        similarity=joblib.load(f)
    print("✅ Model loaded successfully!")
except FileNotFoundError:
    st.write("❌ similarity  score  ni howa")
    # print(f"❌ ERROR: Model not found at {DATA_PATH}")
    # print("   Make sure you saved 'best_model.pkl' in the 'models' folder.")
    similarity= None
def recommend_movie(movie):
    movie_idx=movies[movies['title']==movie].index[0] # Getting index form data frame 
    distances=similarity[movie_idx] # getting similairty score
    movie_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    top_recommend_movies_title=[]
    top_recommend_movies_poster=[]
    for i in movie_list:
        actual_index = i[0]
        top_recommend_movies_title.append(movies.iloc[actual_index].title)
        movie_id=movies.iloc[actual_index].movie_id
        top_recommend_movies_poster.append(fetch_poster_by_id(movie_id))
    return top_recommend_movies_title,top_recommend_movies_poster

movies_name_list=movies['title'].values # getting the all name of movies
st.title("Recommenation System")
selected_movie=st.selectbox("Select the Movie name",placeholder="movie name",options=movies_name_list)
# 2. When the user clicks the button
if st.button('Recommend'):
    
    # Run your updated function that returns lists of titles and poster URLs
    names, posters = recommend_movie(selected_movie)
    
    # Create 5 equal columns side-by-side
    col1, col2, col3, col4, col5 = st.columns(5)
    
    # Column 1 Display
    with col1:
        st.text(names[0])          # Display Movie Name 1
        st.image(posters[0])       # Display Movie Poster 1
        
    # Column 2 Display
    with col2:
        st.text(names[1])          # Display Movie Name 2
        st.image(posters[1])       # Display Movie Poster 2
        
    # Column 3 Display
    with col3:
        st.text(names[2])          # Display Movie Name 3
        st.image(posters[2])       # Display Movie Poster 3
        
    # Column 4 Display
    with col4:
        st.text(names[3])          # Display Movie Name 4
        st.image(posters[3])       # Display Movie Poster 4
        
    # Column 5 Display
    with col5:
        st.text(names[4])          # Display Movie Name 5
        st.image(posters[4])       # Display Movie Poster 5

