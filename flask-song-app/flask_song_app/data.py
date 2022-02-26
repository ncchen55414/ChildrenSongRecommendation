from joblib import load
import os

#print (os.listdir())

knn = load('./flask-song-app/flask_song_app/data/knn.joblib')   
df = load('./flask-song-app/flask_song_app/data/songs_df.joblib')
distance, indices = knn.kneighbors()


def make_recommendation(idx, num=5):
    _ , indices = knn.kneighbors()
    num = min(num, 10)
    #return df.iloc[indices[idx]][0:num]
    return df.loc[indices[idx],['Track_Name','Age','preview_url','image_url']][0:num].values.tolist()

  
all_songs = df[['Track_Name','Age','preview_url','image_url']].values.tolist()


"""
all_songs =  [('Jingle Bells',
 3,
 'https://p.scdn.co/mp3-preview/d43fc23b4e0ef1d20800ded58e4cb673711aafc2?cid=825f4373e1624b2bbace97b26b56972e',
 'https://i.scdn.co/image/ab67616d0000b2736843822d862ba08a9e6245d7'),
('The Hokey Pokey',
 2,
 'https://p.scdn.co/mp3-preview/b2b72cb245993d46ce479c989d760aff5c606c31?cid=825f4373e1624b2bbace97b26b56972e',
 'https://i.scdn.co/image/ab67616d0000b2739f0237b74e72cb6d0b782d87'),
 ("Blowin' in the Wind",
 14,
 'https://p.scdn.co/mp3-preview/a8b496e6c30ada5c33efb1a613967f8e02115af4?cid=825f4373e1624b2bbace97b26b56972e',
 'https://i.scdn.co/image/ab67616d0000b273ec8bd4c7fd93b7a0cd80a994')
]

recommends ={0:[('Ooo, Ahh, Oww!',
  2,
  'https://p.scdn.co/mp3-preview/ae25a61f571599115932ad75519b7c07a4e21bf6?cid=825f4373e1624b2bbace97b26b56972e',
  'https://i.scdn.co/image/ab67616d0000b273be665703667a944cc9511be1'),
 ('Please, Can I Keep It?',
  2,
  'https://p.scdn.co/mp3-preview/fd06ea7abb0fdfad1d3a47fcb51693de363c74e2?cid=825f4373e1624b2bbace97b26b56972e',
  'https://i.scdn.co/image/ab67616d0000b273c7ca1b380ee823f72d83f5dc'),
 ('The Midnight Train',
  3,
  'https://p.scdn.co/mp3-preview/cbc967c585406e464743d9fdc3f35779547ba569?cid=825f4373e1624b2bbace97b26b56972e',
  'https://i.scdn.co/image/ab67616d0000b273b588f522aad8f200735ca0de'),
 ('The Tonsil Song',
  2,
  'https://p.scdn.co/mp3-preview/41281529ab7e4e8e7ef9824592805fd6be554aae?cid=825f4373e1624b2bbace97b26b56972e',
  'https://i.scdn.co/image/ab67616d0000b27365d867ba1dc8d74291e83d01'),
 ('Moon Moon Moon - Alternate Version',
  2,
  None,
  'https://i.scdn.co/image/ab67616d0000b273d13fb8639cc4db0bb2de4f01')],
  1: [('Side By Side',
  3,
  'https://p.scdn.co/mp3-preview/c336bc24eeeb894e7f95069cc5df283f41008db6?cid=825f4373e1624b2bbace97b26b56972e',
  'https://i.scdn.co/image/ab67616d0000b273cb680163fe690de42393489e'),
 ('So Nice To Meet You',
  2,
  'https://p.scdn.co/mp3-preview/2e43023ec69d4ea3b34c75416c368c046a603a10?cid=825f4373e1624b2bbace97b26b56972e',
  'https://i.scdn.co/image/ab67616d0000b273c2a36dfe783e9d62bba56e36'),
 ("Bein' Green",
  5,
  None,
  'https://i.scdn.co/image/ab67616d0000b273e8b83a879e062cdc0d0aef39'),
 ('Verde Luz',
  2,
  'https://p.scdn.co/mp3-preview/44ccbcb0cfaaae0152bf00136ce1bb460b0d47bc?cid=825f4373e1624b2bbace97b26b56972e',
  'https://i.scdn.co/image/ab67616d0000b27363fdf164e13903cb5f782f9b'),
 ("Soldier's Joy",
  2,
  'https://p.scdn.co/mp3-preview/474b4e5bf325283efa4e615a902bfbe0f71f071b?cid=825f4373e1624b2bbace97b26b56972e',
  'https://i.scdn.co/image/ab67616d0000b2732321f75c4b311b24081814cb')],
  2: [ ('Love Is A Losing Game',
  14,
  None,
  'https://i.scdn.co/image/ab67616d0000b27376ffb5b5ab045d22c81235c1'),
 ('Level',
  13,
  'https://p.scdn.co/mp3-preview/3aa91306af9895cea4cd3d46bb4a9eab252f4401?cid=825f4373e1624b2bbace97b26b56972e',
  'https://i.scdn.co/image/ab67616d0000b273aaafcdc8e35209dc99554017'),
   ("Where'd Ya Get That Dirt?",
  5,
  'https://p.scdn.co/mp3-preview/221a9547a70076fa605d96967a37e135e4b5b55e?cid=825f4373e1624b2bbace97b26b56972e',
  'https://i.scdn.co/image/ab67616d0000b2730c0d9bed51a84e95afe36b4f'),
 ('Dark Magic',
  9,
  'https://p.scdn.co/mp3-preview/4179c7a91f2f2a154f34c1bdfe1730dc2b3808db?cid=825f4373e1624b2bbace97b26b56972e',
  'https://i.scdn.co/image/ab67616d0000b27306b60d1915dcf60678a03105'),
 ('Outro (feat. Chilly Gonzales)',
  14,
  None,
  'https://i.scdn.co/image/ab67616d0000b27354ef13c30a024a7f1ba79efd')]}
"""