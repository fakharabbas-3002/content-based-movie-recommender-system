## Content based Movie Recommender System

#### Using movies genres, actors, directors and movie keywords to recommend top n similar movies for given movie. Used cosine similarity for analysis.

Below use cases can be for this analysis.
- If user have opened a movie then you can show him top n movies similar to it.
- Can recommend top n movies to user against his last rated movie.

Files and details about repo is below. 
- "Exploratory Analysis - Content.ipynb" is for basic exploratory analysis to get to know the data.
- "Content based recommendation system.ipynb" is main file for recommender system. I am showing 3 exapmles at the end and exporting data in pickle for web interface.
- "movie_recom.py" is getting similarty scores from previois model and generating streamlit based web application to recomment top 5 related movies against selected movie in drop down. Below is screeshot for web application. 

![Web interface for movie recommendation (code is in movie_recom py)](https://user-images.githubusercontent.com/22819467/224561529-44c03e34-a916-4aa6-8435-c878ca90e2fa.png)

##### I am "hetrec2011-movielens-2k" dataset for this analysis. Data is included in data folder of this repo. Details of dataset are below.
This dataset is an extension of MovieLens10M dataset, published by GroupLeans research group. http://www.grouplens.org 

   10197 movies
   
      20 movie genres
   20809 movie genre assignments
         avg. 2.040 genres per movie

    4060 directors
   95321 actors
         avg. 22.778 actors per movie
      
   13222 tags
   47957 tag assignments (tas), i.e. tuples [user, tag, movie]
         avg. 22.696 tas per user
         avg. 8.117 tas per movie
         
  
-----
Files
-----

   * movies.dat
   
   	This file contains information about the movies of the database.
   	
   	The original movie information -title and year- available at MovieLens10M dataset 
   	has been extended with public data provided in IMDb and Rotten Tomatoes websites:
   	   - Titles in Spanish
   	   - IMDb movie ids
   	   - IMDb picture URLs
           - Rotten Tomatoes movie ids
           - Rotten Tomatoes picture URLs
           - Rotten Tomatoes (all/top) critics' ratings, avg. scores, numbers of 
             reviews/fresh_scores/rotten_scores
           - Rotten Tomatoes audience' avg. ratings, number of ratings, avg. scores
   
   * movie_genres.dat
   
        This file contains the genres of the movies.
   
   * movie_directors.dat
   
   	This file contains the directors of the movies.
   
   * movie_actors.dat
   
   	This file contains the main actores and actresses of the movies.
   	
   	A ranking is given to the actors of each movie according to the order in which 
   	they appear on the movie IMDb cast web page.
   
   * tags.dat
   
   	This file contains the set of tags available in the dataset.
    
   * movie_tags.dat
   
        This file contains the tags assigned to the movies, and the number of times 
        the tags were assigned to each movie.
  
