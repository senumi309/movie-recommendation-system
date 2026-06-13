import streamlit as st
from src.recommender import MovieRecommender


st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬"
)

st.title("🎬 Movie Recommendation System")

st.write(
    "Enter a movie title and get similar movie recommendations."
)

recommender = MovieRecommender()

movie_title = st.selectbox(
    "Select a Movie",
    sorted(recommender.movies["title"].tolist())
)

if st.button("Get Recommendations"):

    recommendations = recommender.recommend_by_title(
        movie_title,
        5
    )

    if recommendations.empty:
        st.error("Movie not found.")
    else:
        st.success("Recommendations generated!")

        st.dataframe(
            recommendations[
                ["title", "genres", "similarity_score"]
            ]
        )