import streamlit as st
import pickle

# Load the model and data
with open('movies.pkl', 'rb') as file:
    data = pickle.load(file)

with open('similarity.pkl', 'rb') as file:
    similarity = pickle.load(file)

# App title and description
st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>🎬 Movie Recommendation System</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Find movies similar to your favorite one!</h4>", unsafe_allow_html=True)
st.write("")

# Dropdown selection
movies_list = data['title'].values
selected_movie = st.selectbox('Search or choose a movie:', movies_list)

# Recommendation function
def recommend(movie):
    recommendation_list = []
    movie_index = data[data['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    for movie in movie_list:
        recommendation_list.append(data.iloc[movie[0]].title)
    return recommendation_list

# Recommend button
if st.button('🎥 Recommend Movies'):
    recommendation = recommend(selected_movie)
    st.markdown("## ⭐ Top 5 Recommendations for You:")
    for idx, title in enumerate(recommendation, 1):
        st.markdown(f"**{idx}.** 🎞️ {title}")
