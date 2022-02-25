import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import Normalizer
from sklearn.neighbors import NearestNeighbors



df = pd.read_csv("./data/all.csv")

columns = ['Track_ID','Track_Name','Artists', 'Age','popularity','danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness',
       'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo','duration_ms',
       'time_signature']
df = df[columns].astype({'key': 'Int64', 'mode':'Int64', 'duration_ms':'Int64', 'time_signature':'Int64'})

pipe = Pipeline([
    ('select features columns', ColumnTransformer([('select column','passthrough',slice(3,18))])),
    ('normalize', Normalizer())
    
])

df = df.dropna().drop_duplicates()
features = pipe.fit_transform(df)
nn = NearestNeighbors(n_neighbors=10).fit(features)

def make_recommendation(idx, num=5):
    dists, indices = nn.kneighbors(features[idx].reshape(1,-1))
    num = min(num, 20)
    return df.iloc[indices[0]][0:num]

print (make_recommendation(5)['Track_Name'])