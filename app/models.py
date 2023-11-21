from app import db
from datetime import datetime

class Artist(db.Model):
    __tablename__="Artist"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), index=True, unique=True, nullable=False)
    hometown = db.Column(db.String(100))
    description = db.Column(db.Text(350))
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
