from app import app, db
from datetime import datetime

class Artist(db.Model):
    __tablename__="Artist"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), index=True, unique=True, nullable=False)
    hometown = db.Column(db.String(100))
    description = db.Column(db.Text(350))

    def __repr__(self):
        return '<Artist: {},>'.format(self.name)

class Events(db.Model):
    __tablename__="Events"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200))
    date = db.Column(db.DateTime, index=True)
    venues_id = db.Column(db.Integer, db.ForeignKey('Venue.id'))

    def __repr__(self):
        return '<Upcoming Events: {}>'.format(self.title)
        #return '<Upcoming Events: {} featuring {} at {} on {}>'.format(self.title, self.artist_id, self.venue_id, self.datetime)

class Venue(db.Model):
    __tablename__="Venue"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    placename = db.Column(db.String(200))
    location = db.Column(db.String(200))
    events = db.relationship("Events", backref="venue")

    def __repr__(self):
        return '<Venue: {}>'.format(self.placename)

