#!/usr/bin/env python
# coding: utf-8

# In[120]:


import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns


# In[29]:


movies_df1 = pd.read_csv("C:\\Users\\LENOVO\\OneDrive\\Desktop//movies.csv")


# In[ ]:





# In[30]:


ratings_df2 = pd.read_csv("C:\\Users\\LENOVO\\OneDrive\\Desktop//ratings.csv")


# In[31]:


links_df3 = pd.read_csv("C:\\Users\\LENOVO\\OneDrive\\Desktop//links.csv")


# In[32]:


#tags_ = pd.read_csv("C:\\Users\\LENOVO\\OneDrive\\Desktop//tags.csv")


# In[33]:


shape=df1.shape
print(shape)


# In[34]:


shape=df2.shape
print(shape)


# In[35]:


shape=df3.shape
print(shape)


# In[36]:


shape=df4.shape
print(shape)


# In[37]:


df1= pd.read_csv('movies.csv')


# In[24]:


movies_df


# In[59]:


tags = pd.read_csv("C:\\Users\\LENOVO\\OneDrive\\Desktop//tags.csv")
tags


# In[25]:


ratings_df


# In[60]:


ratings = pd.read_csv("C:\\Users\\LENOVO\\OneDrive\\Desktop//ratings.csv")
ratings


# In[90]:


ratings['rating'].describe()


# In[91]:


ratings.describe()


# In[92]:


ratings_count = ratings_df.groupby('movieId').size().reset_index(name='count')


# In[93]:


max_ratings_movie = ratings_count.loc[ratings_count['count'].idxmax()]


# In[94]:


print(f"Movie ID with the maximum number of user ratings: {max_ratings_movie['movieId']} with {max_ratings_movie['count']} ratings.")


# In[95]:


ratings_count = ratings_df.groupby('movieId').size().reset_index(name='count')


# In[96]:


max_ratings_movie_id = ratings_count.loc[ratings_count['count'].idxmax(), 'movieId']


# In[97]:


max_ratings_movie = movies_df[movies_df['movieId'] == max_ratings_movie_id]


# In[98]:


print(f"The movie with the maximum number of user ratings is: {max_ratings_movie['title'].values[0]}")


# In[ ]:





# In[99]:


print(movies_df.head())


# In[ ]:





# In[100]:


tags = pd.read_csv("C:\\Users\\LENOVO\\OneDrive\\Desktop//ratings.csv")
tags


# In[101]:


print(movies_df.head())


# In[106]:


matrix_movie_id = movies_df.loc[movies_df['title'] == "Matrix, The (1999)", 'movieId'].values[0]


# In[107]:


matrix_tags = tags_df[tags_df['movieId'] == matrix_movie_id]


# In[108]:


print(movies_df.head())
print(tags_df.head())


# In[109]:


matrix_movie_id = movies_df.loc[movies_df['title'] == "Matrix, The (1999)", 'movieId'].values[0]


# In[110]:


matrix_tags = tags_df[tags_df['movieId'] == matrix_movie_id]


# In[111]:


unique_tags = matrix_tags['tag'].unique()


# In[112]:


print(f"Tags submitted for 'The Matrix (1999)': {unique_tags}")


# In[ ]:





# In[ ]:





# In[113]:


terminator_movie_id = movies_df.loc[movies_df['title'] == "Terminator 2: Judgment Day (1991)", 'movieId'].values[0]


# In[114]:


terminator_ratings = ratings_df[ratings_df['movieId'] == terminator_movie_id]


# In[115]:


average_rating = terminator_ratings['rating'].mean()


# In[116]:


print(f"The average user rating for 'Terminator 2: Judgment Day (1991)' is: {average_rating:.2f}")


# In[ ]:





# In[ ]:





# In[117]:


fight_club_movie_id = movies_df.loc[movies_df['title'] == "Fight Club (1999)", 'movieId'].values[0]


# In[118]:


fight_club_ratings = ratings_df[ratings_df['movieId'] == fight_club_movie_id]


# In[121]:


plt.figure(figsize=(12, 6))


# In[122]:


# Histogram
plt.subplot(1, 2, 1)
sns.histplot(fight_club_ratings['rating'], bins=10, kde=True)
plt.title('Distribution of Ratings for Fight Club (1999)')
plt.xlabel('Rating')
plt.ylabel('Frequency')


# In[123]:


# Box Plot
plt.subplot(1, 2, 2)
sns.boxplot(x=fight_club_ratings['rating'])
plt.title('Box Plot of Ratings for Fight Club (1999)')
plt.xlabel('Rating')


# In[124]:


plt.tight_layout()
plt.show()


# In[ ]:





# In[130]:


average_ratings = ratings_df.groupby('movieId')['rating'].median().reset_index()


# In[131]:


average_ratings = average_ratings.merge(movies_df, on='movieId')


# In[132]:


most_popular_movie = average_ratings.loc[average_ratings['rating'].idxmax()]


# In[133]:


print(f"The most popular movie based on average user ratings is:")
print(f"Title: {most_popular_movie['title']}")
print(f"Average Rating: {most_popular_movie['rating']:.1f}")


# In[ ]:





# In[134]:


ating_counts = ratings_df.groupby('movieId').size().reset_index(name='rating_count')


# In[135]:


rating_counts = rating_counts.merge(movies_df, on='movieId')


# In[136]:


top_5_movies = rating_counts.sort_values(by='rating_count', ascending=False).head(5)


# In[ ]:





# In[47]:


df1.head(10)


# In[48]:


df2.head(10)


# In[51]:


df3.head(10)


# In[52]:


df4.head(10)


# In[53]:


# Dictionary storing movies and their respective number of user ratings
movies = {
    "Matrix": 1900000,
    "Pulp Fiction": 2000000,
    "Forrest Gump": 1800000,
    "Shawshank Redemption": 2500000
}

# Find the movie with the maximum number of ratings
max_movie = max(movies, key=movies.get)

# Output the movie with the maximum ratings and the number of ratings
print(f"The movie with the maximum number of user ratings is: {max_movie} with {movies[max_movie]} ratings.")


# In[54]:


#Merge the two dataframes on the 'movieId' column
merged_df = df1.merge(df2, on='movieId')


# In[55]:


ratings_per_movie = merged_df.groupby('movieId')['userId'].nunique()


# In[56]:


# Finding the movie with the most ratings
most_rated_movie_id = ratings_per_movie.idxmax()
most_rated_movie_count = ratings_per_movie.max()

# Get the movie title using the movieId
most_rated_movie_title = merged_df[merged_df['movieId'] == most_rated_movie_id]['title'].iloc[0]

print("Movie with the most ratings:", most_rated_movie_title)
print("Number of ratings:", most_rated_movie_count)


# In[57]:


df3.tail(10)


# In[ ]:




