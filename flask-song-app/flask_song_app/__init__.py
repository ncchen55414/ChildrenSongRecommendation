from flask import Flask, render_template,request,redirect,url_for
from flask_song_app.data import all_songs, recommends 
#import all_songs, recommends
from wtforms import Form, SelectField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

class MyForm(Form):
  form = SelectField('song', choices=[(i, all_songs[i][0]) for i in range(len(all_songs))], validators = [DataRequired()])
  submit = SubmitField("Submit")


@app.route('/', methods=['GET','POST'])
def index():
  
    myform = MyForm(request.form)

    if request.method == 'POST':
      song_id = int(myform.form.data)
      return redirect(url_for("song_page", song_id=song_id))

    return render_template("index.html", template_form = myform)


@app.route('/<int:song_id>',methods=['GET','POST'])
def song_page(song_id):
  if request.method == 'POST': 
    songs=recommends[song_id]
    songs_filtered=[]
    for song in songs:
      if song[1] <= int(request.form.get('age')):
        songs_filtered.append(song)

    return render_template('result_filter.html', song= all_songs[song_id], songs= songs_filtered, song_id = song_id, filter = request.form.get('age'))

  return render_template('result.html', song=all_songs[song_id], songs=recommends[song_id], song_id = song_id)
  


if __name__ == '__main__':
  app.run()
