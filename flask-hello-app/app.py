"""
An example for dropdown menu:
(1) User selects an item from a drop menu, press 'submit' button.
(2) Redender a webpage showing what the user selected.
"""

from flask import Flask, render_template,request, redirect, url_for
from wtforms import Form, SelectField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
choices = [(1, 'Song 1'), (2, 'Song 2'), (3, 'Song 3')]

class SongForm(Form):
    form = SelectField('song', choices = choices, validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route("/")
@app.route("/dropdown",methods=['GET','POST'])
def songSelect():
    songForm = SongForm(request.form)

    if request.method == 'POST':
        song_id = int(songForm.form.data)
        return redirect(url_for('song_page', song_id=song_id))
    else:
        return render_template('form.html', template_form = songForm)

@app.route('/<int:song_id>',methods=['GET'])
def song_page(song_id):
    return render_template('song.html', song_id=song_id)

if __name__ == '__main__':
    app.run()