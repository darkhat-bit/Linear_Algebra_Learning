import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity
import seaborn as sns

# =====================================
# DATA: Movies with ratings
# =====================================

movies_data = {
    'Movie_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Name': ['Inception', 'Dark', 'Interstellar', 'The Matrix', 'Tenet',
             'Dune', 'Avatar', 'Avengers', 'Joker', 'Parasite'],
    'Genre_Sci-Fi': [1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    'Genre_Action': [1, 0, 0, 1, 1, 1, 1, 1, 0, 0],
    'Genre_Drama': [1, 1, 1, 0, 0, 1, 0, 0, 1, 1],
    'IMDb_Rating': [8.8, 8.8, 8.7, 8.7, 7.3, 8.0, 7.8, 8.0, 8.4, 8.6],
    'Budget_Million': [160, 90, 165, 63, 200, 165, 237, 220, 55, 11]
}

movies_df = pd.DataFrame(movies_data)

# =====================================
# USER RATINGS (Who rated what?)
# =====================================

user_ratings = {
    'User_ID': [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4],
    'Movie_ID': [1, 3, 4, 2, 5, 7, 1, 6, 9, 3, 8, 10],
    'Rating': [9, 8.5, 9, 8, 6, 7.5, 9, 8.5, 7, 8.5, 8, 8.5]
}

ratings_df = pd.DataFrame(user_ratings)

print("=" * 60)
print("MOVIES DATABASE")
print("=" * 60)
print(movies_df)
print("\n" + "=" * 60)
print("USER RATINGS")
print("=" * 60)
print(ratings_df)


# =====================================
# STEP 1: CREATE FEATURE MATRIX
# =====================================
# Each movie = vector of features (genre, rating, budget)

feature_cols = ['Genre_Sci-Fi', 'Genre_Action', 'Genre_Drama', 'IMDb_Rating', 'Budget_Million']
movie_features = movies_df[feature_cols].values

# Normalize budget (scale to 0-10 like ratings)
movie_features[:, -1] = (movie_features[:, -1] - movie_features[:, -1].min()) / \
                        (movie_features[:, -1].max() - movie_features[:, -1].min()) * 10

print("\n" + "=" * 60)
print("NORMALIZED MOVIE FEATURES")
print("=" * 60)
print(pd.DataFrame(movie_features, columns=feature_cols))


# =====================================
# STEP 2: CALCULATE SIMILARITY
# =====================================
# How similar is each movie to every other movie?

similarity_matrix = cosine_similarity(movie_features)

print("\n" + "=" * 60)
print("MOVIE SIMILARITY MATRIX")
print("=" * 60)
similarity_df = pd.DataFrame(
    similarity_matrix,
    index=movies_df['Name'],
    columns=movies_df['Name']
)
print(similarity_df.round(2))


# =====================================
# STEP 3: RECOMMENDATION FUNCTION
# =====================================

def recommend_movies(user_id, n_recommendations=3):
    """
    Recommend movies to user based on movies they liked
    """
    # Step 1: Find movies this user has rated
    user_movies = ratings_df[ratings_df['User_ID'] == user_id]
    
    if len(user_movies) == 0:
        return "User not found"
    
    # Step 2: Find movies they rated HIGH (>=8)
    liked_movies = user_movies[user_movies['Rating'] >= 8]
    liked_movie_ids = liked_movies['Movie_ID'].values - 1  # -1 for 0-indexing
    
    if len(liked_movie_ids) == 0:
        return "User hasn't rated any movie 8+"
    
    # Step 3: Calculate average similarity to liked movies
    similarities = np.zeros(len(movies_df))
    for movie_idx in range(len(movies_df)):
        # Don't recommend movies user already rated
        if movies_df.iloc[movie_idx]['Movie_ID'] in user_movies['Movie_ID'].values:
            similarities[movie_idx] = -1
        else:
            # Average similarity to all liked movies
            similarities[movie_idx] = np.mean([
                similarity_matrix[movie_idx, liked_id] 
                for liked_id in liked_movie_ids
            ])
    
    # Step 4: Get top N recommendations
    top_indices = np.argsort(similarities)[::-1][:n_recommendations]
    recommendations = movies_df.iloc[top_indices][['Name', 'IMDb_Rating']]
    
    return recommendations, similarities


# =====================================
# STEP 4: GET RECOMMENDATIONS
# =====================================

print("\n" + "=" * 60)
print("RECOMMENDATIONS")
print("=" * 60)

for user in [1, 2, 3, 4]:
    print(f"\n👤 USER {user}:")
    print(f"   Watched: {ratings_df[ratings_df['User_ID'] == user]['Movie_ID'].values}")
    
    recommendations, scores = recommend_movies(user, n_recommendations=2)
    print(f"\n   🎬 Recommended:")
    for idx, row in recommendations.iterrows():
        print(f"      • {row['Name']} (Rating: {row['IMDb_Rating']})")


# =====================================
# STEP 5: VISUALIZATIONS
# =====================================

fig, axes = plt.subplots(2, 2, figsize=(15, 12))

# Chart 1: Movie Ratings
ax1 = axes[0, 0]
ax1.barh(movies_df['Name'], movies_df['IMDb_Rating'], color='skyblue')
ax1.set_xlabel('IMDb Rating')
ax1.set_title('Movie Ratings Comparison')
ax1.set_xlim(0, 10)

# Chart 2: Budget vs Rating
ax2 = axes[0, 1]
colors = ['red' if x == 1 else 'blue' for x in movies_df['Genre_Sci-Fi']]
ax2.scatter(movies_df['Budget_Million'], movies_df['IMDb_Rating'], 
           s=200, c=colors, alpha=0.6)
for idx, row in movies_df.iterrows():
    ax2.annotate(row['Name'][:5], (row['Budget_Million'], row['IMDb_Rating']),
                fontsize=8, alpha=0.7)
ax2.set_xlabel('Budget (Million $)')
ax2.set_ylabel('Rating')
ax2.set_title('Budget vs Rating (Red=Sci-Fi, Blue=Other)')
ax2.grid(True, alpha=0.3)

# Chart 3: Similarity Heatmap (first 5 movies)
ax3 = axes[1, 0]
sns.heatmap(similarity_matrix[:5, :5], annot=True, fmt='.2f', 
           xticklabels=movies_df['Name'][:5],
           yticklabels=movies_df['Name'][:5],
           cmap='YlOrRd', ax=ax3)
ax3.set_title('Movie Similarity Heatmap (First 5)')

# Chart 4: User Ratings Distribution
ax4 = axes[1, 1]
for user in ratings_df['User_ID'].unique():
    user_data = ratings_df[ratings_df['User_ID'] == user]
    ax4.scatter(user_data['Movie_ID'], user_data['Rating'], 
               label=f'User {user}', s=100, alpha=0.7)
ax4.set_xlabel('Movie ID')
ax4.set_ylabel('Rating')
ax4.set_title('User Ratings Pattern')
ax4.legend()
ax4.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('movie_recommendation_analysis.png', dpi=300, bbox_inches='tight')
print("\n" + "=" * 60)
print("📊 Visualization saved as 'movie_recommendation_analysis.png'")
print("=" * 60)

plt.show()


# =====================================
# STEP 6: STATISTICS & INSIGHTS
# =====================================

print("\n" + "=" * 60)
print("INSIGHTS & STATISTICS")
print("=" * 60)

print(f"\n📈 Average Rating: {movies_df['IMDb_Rating'].mean():.2f}")
print(f"📈 Highest Rated: {movies_df.loc[movies_df['IMDb_Rating'].idxmax(), 'Name']}")
print(f"📈 Lowest Rated: {movies_df.loc[movies_df['IMDb_Rating'].idxmin(), 'Name']}")

print(f"\n💰 Budget Statistics:")
print(f"   Average: ${movies_df['Budget_Million'].mean():.1f}M")
print(f"   Max: ${movies_df['Budget_Million'].max():.1f}M")
print(f"   Min: ${movies_df['Budget_Million'].min():.1f}M")

print(f"\n🎬 Genre Distribution:")
print(f"   Sci-Fi: {movies_df['Genre_Sci-Fi'].sum()} movies")
print(f"   Action: {movies_df['Genre_Action'].sum()} movies")
print(f"   Drama: {movies_df['Genre_Drama'].sum()} movies")

# Correlation analysis
correlation = np.corrcoef(movies_df['Budget_Million'], movies_df['IMDb_Rating'])[0, 1]
print(f"\n📊 Budget-Rating Correlation: {correlation:.3f}")
print(f"   (Higher budget → {'better' if correlation > 0 else 'worse'} ratings)")