import streamlit as st
import pickle
import requests
import bz2

def fetch_poster(movie_id):
    url = 'https://api.themoviedb.org/3/movie/{}?api_key=f9441f158f659246832a69e9575ee441&language=en-US'.format(movie_id)

    # Disguise the request as coming from a standard web browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
    }

    try:
        # Added headers and a 5-second timeout
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status() # Will raise an error for 404, 401, etc.
        data = response.json()

        if 'poster_path' in data and data['poster_path']:
            return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
        else:
            return "https://via.placeholder.com/500x750?text=No+Poster"

    except requests.exceptions.RequestException as e:
        # If the connection drops, return a placeholder instead of crashing the whole app
        print(f"Error fetching poster for {movie_id}: {e}")
        return "https://via.placeholder.com/500x750?text=Connection+Error"


# 1. Load the movies DataFrame and the COMPRESSED similarity matrix
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(bz2.BZ2File('similarity.pkl.bz2', 'rb'))


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_lists = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []

    for i in movies_lists:
        # FIXED: Changed from .movie_id to .id (or change to ['movie_id'] depending on your pickle file)
        # If your column is named 'movie_id', use: movie_id = movies.iloc[i[0]]['movie_id']
        movie_id = movies.iloc[i[0]].id

        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_posters


st.title('Movie Recommender System')

# 2. Create the list of titles just for the selectbox dropdown
movie_titles = movies['title'].values.tolist()

selected_movie_name = st.selectbox(
    "Select a movie you like:",
    movie_titles
)

if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])