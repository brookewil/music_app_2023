from app import app, db
from datetime import datetime

class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), index=True, unique=True, nullable=False)
    hometown = db.Column(db.String(100))
    description = db.Column(db.Text(128))
    events = db.relationship('Events', backref='events', lazy='dynamic')

    def __repr__(self):
        return '<Artist: {}, Hometown: {}, Description: {}, Upcoming Events: {}>'.format(self.name, self.hometown, self.description, self.events )

class Events(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200))
    date = db.Column(db.DateTime, index=True)
    venue_id = db.Column(db.Integer, db.ForeignKey('Venues.id'))

    def __repr__(self):
        return '<Upcoming Events: {} featuring {} at {} on {}>'.format(self.title, self.artist_id, self.venue_id, self.datetime)

class Venues(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    placename = db.Column(db.String(200))
    location = db.Column(db.String(200))
    events = db.relationship('Events', backref='events', lazy='dynamic')

    def __repr__(self):
        return '<Venue: {}, Address: {}>'.format(self.placename, self.location)

class ArtistToEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('Artist.id'))
    event_id = db.Column(db.Integer, db.ForeignKey('Events.id'))