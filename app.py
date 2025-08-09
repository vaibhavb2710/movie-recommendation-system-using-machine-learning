import pickle
import streamlit as st
import requests
import random

# CSS for hover effect & styling
st.markdown("""
<style>
.movie-card {
    transition: transform 0.3s ease;
    cursor: pointer;
    text-align: center;
}
.movie-card:hover {
    transform: scale(1.07);
}
.movie-title {
    font-weight: bold;
    color: #FFD700;
    font-size: 16px;
    margin-top: 5px;
}
.rating {
    color: #00FF00;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    data = requests.get(url).json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
    return recommended_movie_names, recommended_movie_posters

# App Header
st.markdown("<h1 style='text-align: center; color: #E50914;'>🍿 Movie Recommender System</h1>", unsafe_allow_html=True)

# Load data
movies = pickle.load(open('artifacts/movie_list.pkl', 'rb'))
similarity = pickle.load(open('artifacts/similarity.pkl', 'rb'))

# Movie selection
movie_list = movies['title'].values
selected_movie = st.selectbox(
    "🎥 Type or select a movie from the dropdown",
    movie_list
)

# Show recommendations
if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)

    # Display in grid: 3 movies per row
    for i in range(0, len(recommended_movie_names), 3):
        cols = st.columns(3)
        for col, name, poster in zip(cols, recommended_movie_names[i:i+3], recommended_movie_posters[i:i+3]):
            rating = round(random.uniform(6.0, 9.5), 1)  # Dummy IMDb-style rating
            with col:
                st.markdown(f"""
                <div class="movie-card">
                    <img src="{poster}" style="width:100%; border-radius:10px;">
                    <div class="movie-title">{name}</div>
                    <div class="rating">⭐ {rating}/10</div>
                </div>
                """, unsafe_allow_html=True)
