from datetime import datetime

from flask import render_template, flash, request, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required
from app import app, db
from flask_wtf import FlaskForm
from urllib.parse import urlsplit
from app.forms import *
from app.models import *

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Ithaca Music')

@app.route('/allArtists', methods=['GET', 'POST'])
def allArtists():
    artists_list = db.session.query(Artist).all()
    return render_template('allArtists.html', title="List of Artists", artists=artists_list)

@app.route('/artist/<name>')
def artist(name):
    artist = db.session.query(Artist).filter_by(name=name).first()
    events = db.session.query(Events).join(Artist, Artist.id == ArtistToEvent.artist_id).join(ArtistToEvent, ArtistToEvent.event_id == Events.id).filter(Artist.name == name).all()

    return render_template('artist.html', title=name, artist=artist, events=events)

@app.route('/newArtist', methods=['GET', 'POST'])
@login_required
def newArtist():
    form = CreateArtistForm()
    if form.is_submitted():
        if db.session.query(Artist).filter_by(name=form.name.data).first():
            flash("Artist Page Already Exists")
            return render_template('newArtist.html', title="Create a New Artist", form=form)

        artist = Artist(name=form.name.data, hometown=form.hometown.data, description=form.description.data)
        db.session.add(artist)
        db.session.commit()
        flash('Page created for {},'.format(form.name.data))
        return redirect(url_for('allArtists'))

    return render_template('newArtist.html', title='Create a New Artist', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or urlsplit(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

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

    db.session.add_all([a1, a2, a3, a4, a5, a6])
    db.session.commit()

    v1 = Venue(placename="Pier 17", location="89 South St, New York, NY 10038")
    v2 = Venue(placename="The Armory", location="500 South 6th St, Minneapolis, MN 55415")
    v3 = Venue(placename="Coca-Cola Coliseum", location="45 Manitoba Dr, Toronto, ON M6K 3C3, Canada")
    v4 = Venue(placename="The Theater at Madison Square Garden", location="4 Pennsylvania Plaza, New York, NY 10001")
    v5 = Venue(placename="Arizona Financial Theatre", location="400 W Washington St, Phoenix, AZ 85003")
    v6 = Venue(placename="Stone Pony Summer Stage", location=" 909 Ocean Ave N, Asbury Park, NJ 07712")

    db.session.add_all([v1, v2, v3, v4, v5, v6])
    db.session.commit()

    e1 = Events(title="Sneaking Out of Heaven TOUR", date=datetime(2024,3,11,19, 0), venues_id=3)
    e2 = Events(title="Dawn to Dusk TOUR", date=datetime(2023, 10, 18, 20, 30), venues_id=2)
    e3 = Events(title="Dawn to Dusk TOUR", date=datetime(2023, 10, 20, 20), venues_id=3)
    e4 = Events(title="Dawn to Dusk TOUR", date=datetime(2023,10,22,19), venues_id=4)
    e5 = Events(title="The Jaws of Life TOUR", date=datetime(2023, 11, 7, 18, 30), venues_id=5)
    e6 = Events(title="Sneaking Out of Heaven TOUR", date=datetime(2024, 4, 1, 20, 30), venues_id=5)
    e7 = Events(title="Sad Summer Festival", date=datetime(2024, 7, 29, 13, 30), venues_id=6)
    e8 = Events(title="Warped Tour", date=datetime(2024, 8, 5, 14, 30), venues_id=6)

    db.session.add_all([e1, e2, e3, e4, e5, e6, e7, e8])
    db.session.commit()

    a2e_list = [
        ArtistToEvent(artist=a1, event=e1),
        ArtistToEvent(artist=a1, event=e6),
        ArtistToEvent(artist=a4, event=e2),
        ArtistToEvent(artist=a4, event=e3),
        ArtistToEvent(artist=a4, event=e4),
        ArtistToEvent(artist=a5, event=e5),
        ArtistToEvent(artist=a1, event=e7),
        ArtistToEvent(artist=a5, event=e7),
        ArtistToEvent(artist=a1, event=e8),
        ArtistToEvent(artist=a2, event=e8),
        ArtistToEvent(artist=a3, event=e8),
        ArtistToEvent(artist=a5, event=e8)]

    db.session.add_all(a2e_list)
    db.session.commit()

    return render_template('index.html')

