# Children's Songs Recommendation

## Description

The project consists of four parts:

- `\flask-song-app\` A web application that provides recommendation for children's songs. Users can select a song, and the app will recommend similar songs.  Deployed to Heroku: [https://children-song-app.herokuapp.com/](https://children-song-app.herokuapp.com/)

- `\notebooks\1_*` Data scrapping and cleaning. 
  
- `\notebooks\2_*` Investigation of the relation between age-ratings and song features.

- `\notebooks\3_*` Detailed analysis of song data and models

## Data Ingestion

- 2206 albums with age-ratings scrapped from [Common Sense Media](https://www.commonsensemedia.org/music-reviews?sort=field_review_recommended_age&order=asc), a non-profit whose mission is to ensure digital well-being for kids by providing expert reviews. See more info on [how music is rated](https://www.commonsensemedia.org/about-us/our-mission/about-our-ratings/music).

- Use Spotify API to obtain song tracks in each album. In total, 18K songs along with audio features and ISRC codes are founded.
  
- Use MusixMatch API and ISRC codes to obtain lyrics for 12K songs.

## Models

- Song Recommendation: K-Nearest Neighborhood model.
  
- Lyrics: Latent Dirichlet Allocation topic modeling.

- Age-Rating: Decision Tree model to predict age-ratings for songs based on audio features and lyrics.


## Investigation

- What's the relation between age-ratings and audio features?
  
  - Age-rating is most correlated to `popularity` and `duration` (`popularity` measures how many users have played the track, and `duration` is the time length of the song).
  
  - `Melodic modes` (major vs minor): In the age group of 2-5, more than 80% of the songs are in major keys, while the age group of 13-18 have only 65% in major keys.

- What's the relation between age-ratings and lyrics?

  - Use a decision tree models to predict age-ratings from song lyrics, and check feature-importance.  (Tried, need to improve)

- What are the albums sing about? What are the popular topics in albums?

  - Use LDA Topic Modeling to find popular topic in each age-group.     (Tried, need to improve).