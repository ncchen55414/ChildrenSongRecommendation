# Children's Songs Recommendation

## Description

The project consists of four parts:

- `\flask-song-app\` A web application that provides recommendation for children's songs. Users can select a song, and the app will recommend similar songs.  Deployed to Heroku: [https://children-song-app.herokuapp.com/](https://children-song-app.herokuapp.com/)

- `\notebooks\1_*` Data scrapping and cleaning. 
  
- `\notebooks\2_*` Investigation of the relation between age-ratings and song features.

- `\notebooks\3_*` Age-Rating Models, LDA topic model

- `\notebooks\4_*` Song Recommender

## Data Ingestion

- 2206 albums with age-ratings scrapped from [Common Sense Media](http://web.archive.org/web/20211024135317/https://www.commonsensemedia.org/music-reviews?sort=field_review_recommended_age&order=asc), a non-profit whose mission is to ensure digital well-being for kids by providing expert reviews. See more info on [how music is rated](http://web.archive.org/web/20220114100252/https://www.commonsensemedia.org/about-us/our-mission/about-our-ratings/music).

- Use Spotify API to obtain song tracks in each album. In total, 18K songs along with audio features and ISRC codes are founded.
  
- Use MusixMatch API and ISRC codes to obtain lyrics for 12K songs.

## Models

- **Two Age-Rating Models**:

  - **Use audio features to predict age ratings.**
  
    A tree regression model uses 13 audio features (key, tempo, duration, etc, explained [here](https://developer.spotify.com/documentation/web-api/reference/#/operations/get-audio-features)) and popularity to predict age-ratings. The model achieves an  R^2  score of 0.50, with `popluarity` and `duration` being the two most important features.

  - **Use song lyrics to predict age ratings.**
  
    After basic text preprocessing (tokenization, lemmiztization, removing stop words), the processed lyrics are then feed into a model pipeline consisting of `TfIdfVectorizer` and `RidgeRegressor`. `GridSearchCV` is used on a smaller subset to select the paramters: `min_df` for `TfIdfVectorizer`, and `alpha` for `RidgeRegressor`. These parameteres will be used later for song recommendation with KNN model.

    The model achieves an R^2 score of 0.4.  



- **Song Recommendation** K-Nearest Neighborhood model using the follow features:
  - Audio features: key, mode, time_signature, duration_ms, danceability, energy, loudness, speechiness, acousticness, instrumentalness, liveness valence, tempo. Explained [here](https://developer.spotify.com/documentation/web-api/reference/#/operations/get-audio-features).  
  - Song popularity: A Number between 0-100 computed based on the total number of plays the track has had and how recent those plays are. Provied by [Spotify API](https://developer.spotify.com/documentation/web-api/reference/#/operations/get-track).
  - Age rating of the album that includes the song track.
  - Song lyrics.
  

## Investigation

- What's the relation between age-ratings and audio features?
  
  - Age-rating is most correlated to `popularity` and `duration` (`popularity` measures how many users have played the track, and `duration` is the time length of the song).
  
  - `Melodic modes` (major vs minor): In the age group of 2-5, more than 80% of the songs are in major keys, while the age group of 13-18 have only 65% in major keys.

- What's the relation between age-ratings and lyrics?

- What are the albums sing about? What are the popular topics in albums?

  - Use LDA Topic Modeling to find popular topic in each age-group.     (Tried, need to improve).