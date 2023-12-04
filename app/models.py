from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Artist(db.Model):
    __tablename__="Artist"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), index=True, unique=True, nullable=False)
    hometown = db.Column(db.String(100))
    description = db.Column(db.Text)
    a2e = db.relationship("ArtistToEvent", backref="artist")

    def __repr__(self):
        return '<Artist: {},>'.format(self.name)

class Events(db.Model):
    __tablename__="Events"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200))
    date = db.Column(db.DateTime, index=True)
    venues_id = db.Column(db.Integer, db.ForeignKey('Venue.id'))
    a2e = db.relationship("ArtistToEvent", backref="event")

    def __repr__(self):
        return '<Upcoming Events: {}>'.format(self.title)

class Venue(db.Model):
    __tablename__="Venue"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    placename = db.Column(db.String(200))
    location = db.Column(db.String(200))
    events = db.relationship("Events", backref="venue")

    def __repr__(self):
        return '<Venue: {}>'.format(self.placename)

class ArtistToEvent(db.Model):
    __tablename__ = "ArtistToEvent"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('Artist.id'))
    event_id = db.Column(db.Integer, db.ForeignKey('Events.id'))

    def __repr__(self):
        return '<ArtistToEvent {}>'.format(self.id)

class User(UserMixin, db.Model):
    __tablename__ = "User"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @login.user_loader
    def load_user(id):
        return db.session.get(User, int(id))

    def __repr__(self):
        return '<User {}>'.format(self.username)
