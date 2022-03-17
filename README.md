# Children's Songs Recommendation

## Description

The project consists of five parts:

- `\flask-song-app\` A web application that provides recommendation for children's songs. Users can select a song, and the app will recommend similar songs.  Deployed to Heroku: [https://children-song-app.herokuapp.com/](https://children-song-app.herokuapp.com/)

- `\notebooks\1_*` Data scrapping and cleaning. 
  
- `\notebooks\2_*` Investigation of the relation between age-ratings and audio features. Used NLP to understand the lyrics.

- `\notebooks\3_*` Age-Rating Models using audio features and lyrics.
- `\notebooks\4_*` Song Recommender.

## Data Ingestion

- 2206 albums with age-ratings scrapped from [Common Sense Media](http://web.archive.org/web/20211024135317/https://www.commonsensemedia.org/music-reviews?sort=field_review_recommended_age&order=asc), a non-profit whose mission is to ensure digital well-being for kids by providing expert reviews. See more info on [how music is rated](http://web.archive.org/web/20220114100252/https://www.commonsensemedia.org/about-us/our-mission/about-our-ratings/music).

- Use Spotify API to obtain song tracks in each album. In total, 18K songs along with audio features and ISRC codes are founded.
  
- Use [MusixMatch API with ISRC codes](https://developer.musixmatch.com/documentation/api-reference/track-get) to obtain lyrics for 12K songs.

## Models

- **Two Age-Rating Models**:

  - **Use audio features to predict age ratings.**
  
    A tree regression model uses 13 audio features (key, tempo, duration, etc, explained [here](https://developer.spotify.com/documentation/web-api/reference/#/operations/get-audio-features)) and popularity to predict age-ratings. The model achieves an  R^2  score of 0.50, having `popularity` and `duration` as the two most important features.

  - **Use song lyrics to predict age ratings.**
  
    After basic text preprocessing (tokenization, lemmatization, removing stop words), the processed lyrics are then feed into a model pipeline consisting of `TfIdfVectorizer` and `RidgeRegressor`. `GridSearchCV` is used on a smaller subset to select the paramters: `min_df`, `max_df` for `TfIdfVectorizer`, and `alpha` for `RidgeRegressor`. The parameters for  `TfIdfVectorizer` will be used later for lyrics-based song recommendation with KNN model (where there is no metric to tune parameters.)

    The model achieves an R^2^ score of 0.4.  



- **Song Recommendation** K-Nearest Neighborhood model using the follow features:
  - Audio features: key, mode, time_signature, duration_ms, danceability, energy, loudness, speechiness, acousticness, instrumentalness, liveness valence, tempo. Explained [here](https://developer.spotify.com/documentation/web-api/reference/#/operations/get-audio-features).  
  - Song popularity: A Number between 0-100 computed based on the total number of plays the track has had and how recent those plays are. This number is provided by [Spotify API](https://developer.spotify.com/documentation/web-api/reference/#/operations/get-track).
  - Age rating of the album including the song track.
  - Song lyrics.
  

## Investigation

- What's the relation between age-ratings and audio features?
  
  - Age-rating is most correlated to `popularity` and `duration` (`popularity` measures how many users have played the track, and `duration` is the time length of the song). (See [correlation plot](https://github.com/ncchen55414/ChildrenSongRecommendation/blob/main/figures/variable_correlation.png) or `2.2_Variables_Relation.ipynb`)
  
  - `Melodic modes` (major vs minor): In the age group of 2-5, more than 80% of the songs are in major keys, while the age group of 13-18 have only 65% in major keys. (See [plot](https://github.com/ncchen55414/ChildrenSongRecommendation/blob/main/figures/age_vs_mode.png) or `2.2_Variables_Relation.ipynb`)

- What's the relation between age-ratings and lyrics?
  
  - Visualized by plotting word-polarity: Divide the lyrics into two age-groups: young vs old, and use the conditional word log-probabilities as the (x,y)-coordinate. In the plot, neutral words will approximately lie on the line x=y. (See [plot](https://github.com/ncchen55414/ChildrenSongRecommendation/blob/main/figures/word_polarity.png) or `2.5_NLP_Visualize_Lyrics_Word_Polarity.ipynb`)

- What are the albums sing about? 

  - LDA topic modeling is used to define 10 topics among all lyrics. Each topic is described by its topic keywords. (See `2.4_NLP_Topic_Modeling_Using_Song_Lyrics.ipynb`)