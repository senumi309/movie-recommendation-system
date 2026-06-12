from src.recommender import MovieRecommender

recommender = MovieRecommender()

results = recommender.recommend_by_title("Toy Story", 5)

print(results)