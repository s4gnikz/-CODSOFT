# recommendation_system_user_input.py

import numpy as np

# ------------ Sample Data ----------------

movies = [
    {'title': 'The Matrix', 'genres': ['action', 'sci-fi']},
    {'title': 'Titanic', 'genres': ['romance', 'drama']},
    {'title': 'Die Hard', 'genres': ['action', 'thriller']},
    {'title': 'Interstellar', 'genres': ['adventure', 'sci-fi']}
]

user_movie_matrix = np.array([
    [1, 1, 0, 0],  # User 0
    [1, 0, 1, 0],  # User 1
    [0, 1, 1, 0],  # User 2
    [0, 0, 1, 1],  # User 3
])

def content_based_recommend(user_likes, movies):
    recommendations = [
        movie['title']
        for movie in movies
        if any(genre in user_likes for genre in movie['genres'])
    ]
    return recommendations

def collaborative_recommend(user_movie_matrix, user_index, movies):
    similarities = np.dot(user_movie_matrix, user_movie_matrix[user_index])
    similarities[user_index] = -1  # Exclude self
    most_similar_user = np.argmax(similarities)
    rec_indices = [
        i for i, (target_like, similar_like) in enumerate(
            zip(user_movie_matrix[user_index], user_movie_matrix[most_similar_user])
        ) if similar_like == 1 and target_like == 0
    ]
    recommendations = [movies[i]['title'] for i in rec_indices]
    return recommendations

def main():
    print("Available genres across movies include: action, sci-fi, romance, drama, thriller, adventure")
    user_input = input("Enter your preferred genres, separated by commas (e.g., action,sci-fi): ")
    user_likes = [genre.strip().lower() for genre in user_input.split(",") if genre.strip()]

    print("\nUsers available for collaborative filtering recommendation:")
    print("User indices: 0, 1, 2, 3")
    while True:
        try:
            user_index = int(input("Enter the user index to get recommendations for (0-3): "))
            if user_index not in range(user_movie_matrix.shape[0]):
                print("Invalid user index. Please enter a number between 0 and 3.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")

    cb_recs = content_based_recommend(user_likes, movies)
    cf_recs = collaborative_recommend(user_movie_matrix, user_index, movies)

    print("\nContent-based recommendations based on your preferred genres:")
    if cb_recs:
        for rec in cb_recs:
            print(f"- {rec}")
    else:
        print("No recommendations found for your selected genres.")

    print(f"\nCollaborative filtering recommendations for User {user_index}:")
    if cf_recs:
        for rec in cf_recs:
            print(f"- {rec}")
    else:
        print("No new recommendations found based on similar users.")

if __name__ == "__main__":
    main()
