from datetime import datetime

from flask import render_template, flash, request, redirect, url_for
from app import app, db
from flask_wtf import FlaskForm
from app.forms import CreateArtistForm
from app.models import *

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

    a1 = Artist(name="Waterparks", hometown="Houston, TX", description="Waterparks is an American rock band formed in 2011. The group currently consists of lead vocalist and rhythm guitarist Awsten Knight, backing vocalist and lead guitarist Geoff Wigington, and backing vocalist and drummer Otto Wood.")
    a2 = Artist(name="My Chemical Romance", hometown="Newark, NJ", description="My Chemical Romance (commonly abbreviated to MCR or My Chem) is an American rock band formed in 2001. The band's current lineup consists of lead vocalist Gerard Way, lead guitarist Ray Toro, rhythm guitarist Frank Iero, and bassist Mikey Way.")
    a3 = Artist(name="Evanescence", hometown="Little Rock, AR", description="Evanescence is an American rock band founded in 1995 by singer and keyboardist Amy Lee and guitarist Ben Moody. After releasing independent EPs as a duo in the late 90s and a demo CD, Evanescence released their debut studio album, Fallen, on Wind-up Records in 2003")
    a4 = Artist(name="The Rose", hometown="Seoul, SK", description="The Rose (Korean: 더 로즈) is a South Korean indie-rock band under their company Windfall and partnered up with Transparent Arts. The band is composed of four members: Kim Woo-sung (vocals, guitar), Park Do-joon (keyboard), Lee Ha-joon (drums), and Lee Jae-hyeong (bass)")
    a5 = Artist(name="Pierce the Veil", hometown="San Diego, CA", description="Pierce the Veil is an American rock band formed in 2006. Founded by brothers Vic and Mike Fuentes after the disbanding of Before Today. Jaime Preciado and Tony Perry joined the group in 2007, on bass and lead guitar respectively.")
    a6 = Artist(name="WEi", hometown="Seoul, SK", description="WEi (Korean: 위아이; pronounced We-I) is a South Korean boy band formed by Oui Entertainment. The group consists of six members: Daehyeon, Donghan, Yongha, Yohan, Seokhwa, and Junseo. The group made their debut on October 5, 2020, with their extended play Identity: First Sight.")

    db.session.add_all[(a1, a2, a3, a4, a5, a6)]
    db.session.commit()

    v1 = Venue(placename="Pier 17", location="89 South St, New York, NY 10038")
    v2 = Venue(placename="The Armory", location="500 South 6th St, Minneapolis, MN 55415")
    v3 = Venue(placename="Coca-Cola Coliseum", location="45 Manitoba Dr, Toronto, ON M6K 3C3, Canada")
    v4 = Venue(placename="The Theater at Madison Square Garden", location="4 Pennsylvania Plaza, New York, NY 10001")
    v5 = Venue(placename="Arizona Financial Theatre", location="400 W Washington St, Phoenix, AZ 85003")

    db.session.add_all([v1, v2, v3, v4, v5])
    db.session.commit()

    e1 = Events(title="Sneaking Out of Heaven TOUR", date=datetime(2024,3,11,7, 0), venues_id=3)
    e2 = Events(title="Dawn to Dusk TOUR", date=datetime(2023, 10, 18, 8, 30), venues_id=2)
    e3 = Events(title="Dawn to Dusk TOUR", date=datetime(2023, 10, 20, 8), venues_id=3)
    e4 = Events(title="Dawn to Dusk TOUR", date=datetime(2023,10,22,8), venues_id=4)
    e5 = Events(title="The Jaws of Life TOUR", date=datetime(2023, 11, 7, 6, 30), venues_id=5)
    e6 = Events(title="Sneaking Out of Heaven TOUR", date=datetime(2024, 4, 1, 8, 30), venues_id=5)

    db.session.add_all([e1, e2, e3, e4, e5, e6])
    db.session.commit()

    return render_template('index.html')
