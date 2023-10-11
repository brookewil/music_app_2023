from flask import render_template, flash, request, redirect, url_for
from app import app
from app.forms import CreateArtistForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Ithaca Music')

@app.route('/artists', methods=['GET', 'POST'])
def artists():
    artists_list = ["John Brown's Body", "Gunpoets", "Donna The Buffalo", "The Blind Spots"]
    return render_template('artists.html',  artists_list=artists_list)

@app.route('/gunpoets', methods=['GET', 'POST'])
def gunpoets():
    details = {
        "name": "The Gunpoets",
        "hometown": "Ithaca",
        "description": "Voice as a weapon, words as bullets, spreading the universal message of peace, love, and justice through music. Sure, there's a cynical cultural tendency to make certain assumptions when you hear the word \"gun\" associated with rap music, but this seven-member live hip-hop band from Ithaca, NY, runs contrary to that image with their positive message and uplifting performances.",
        "events": ["The Commons on Thursday 9/6", "The Haunt next Friday 9/14"]
    }
    return render_template('gunpoets.html',  title='Gunpoets', details=details)

@app.route('/newartists', methods=['GET', 'POST'])
def newartists():
    form = CreateArtistForm()
    if form.is_submitted():
        flash('Page created for {}'.format(form.name.data))
        details = request.form
        return render_template('artist.html', details=details)
    return render_template('newartists.html',  title='Create a New Artist', form=form)

@app.route('/reset_db')
def reset_db():
   flash("Resetting database: deleting old data and repopulating with dummy data")
   # clear all data from all tables
   meta = db.metadata
   for table in reversed(meta.sorted_tables):
       print('Clear table {}'.format(table))
       db.session.execute(table.delete())
   db.session.commit()

