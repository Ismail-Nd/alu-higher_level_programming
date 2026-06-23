import streamlit as st
import pandas as pd

df = pd.read_csv('imdb.csv')

st.title('Movie Search')
user_movie = st.text_input('Search for a movie:')

if user_movie: 
    # partial, case-insensitive search
    matches = df[df['title'].str.lower().str.contains(user_movie.lower(), na=False)]

    if matches.empty:
        st.error("Your movie doesn't exist in this dataset")
    else:
        st.success(f"Found {len(matches)} movie(s)")
        for _, row in matches.head(10).iterrows():
            st.subheader(row['title'])
            st.write(f"Year: {row['year']}")
            st.write(f"Runtime: {row['runtime_minutes']} minutes")
            st.write(f"Genres: {row['genres']}")
            st.write(f"Rating: {row['average_rating']} ({row['num_votes']} votes)")
            st.markdown(f"[IMDb link]({row['imdb_url']})")
            st.divider()