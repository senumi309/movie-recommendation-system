import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


class MovieRecommender:

    def __init__(self):
        self.movies = pd.read_csv("data/movies.csv")
        self.ratings = pd.read_csv("data/ratings.csv")

        self.movie_matrix = None
        self.movie_similarity_df = None

    def build_model(self):
        self.movie_matrix = self.ratings.pivot_table(
            index="userId",
            columns="movieId",
            values="rating"
        )

        similarity_matrix = cosine_similarity(
            self.movie_matrix.fillna(0).T
        )

        self.movie_similarity_df = pd.DataFrame(
            similarity_matrix,
            index=self.movie_matrix.columns,
            columns=self.movie_matrix.columns
        )

        print("Recommendation model built successfully!")

    def recommend_by_movie_id(self, movie_id, number_of_recommendations=5):
        if self.movie_similarity_df is None:
            self.build_model()

        if movie_id not in self.movie_similarity_df.columns:
            return pd.DataFrame()

        similar_movies = self.movie_similarity_df[movie_id]
        similar_movies = similar_movies.sort_values(ascending=False)
        similar_movies = similar_movies.iloc[1:number_of_recommendations + 1]

        recommendations = self.movies[
            self.movies["movieId"].isin(similar_movies.index)
        ].copy()

        recommendations["similarity_score"] = recommendations["movieId"].map(similar_movies)

        return recommendations[["movieId", "title", "genres", "similarity_score"]]

    def recommend_by_title(self, movie_title, number_of_recommendations=5):
        if self.movie_similarity_df is None:
            self.build_model()

        movie = self.movies[
            self.movies["title"] == movie_title
        ]

        if len(movie) == 0:
            return pd.DataFrame()

        movie_id = movie.iloc[0]["movieId"]

        return self.recommend_by_movie_id(movie_id, number_of_recommendations)