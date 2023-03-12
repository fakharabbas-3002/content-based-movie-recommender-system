import pickle
import streamlit as st

base_path = 'data/'

def recommend_top_5_movies(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    top_5_movies = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].id
        top_5_movies.append(movies.iloc[i[0]].title)

    return top_5_movies


st.header('Movie Recommendation System')
#st.success('Results will be shown here:')

movies = pickle.load(open(base_path+'whole_data.pkl','rb'))
similarity = pickle.load(open(base_path+'similarity_score.pkl','rb'))

movie_list = movies['title'].values
#with st.sidebar.form(key ='Form'):
selected_movie = st.selectbox("Type or Select a movie", movie_list)
submit_button = st.button("Submit")

if submit_button:
    #st.success('Results:')
    recommended_movies = recommend_top_5_movies(selected_movie)
    recommended_movies_display = '\n\n'.join(movie_name for movie_name in recommended_movies)
    st.success(recommended_movies_display)