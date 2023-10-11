from app import app, db


class Artist(db.Model):
    __tablename__ = 'Artist'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True, nullable=False)
    hometown = db.Column(db.String(100))
    description = db.Column(db.Text(128))
    events = db.relationship('Events', backref='events', lazy='dynamic')

    def __repr__(self):
        return '<Artist: {}, Hometown: {}, Description: {}, Upcoming Events: {}>'.format(self.name, self.hometown, self.description, self.events )

class Events(db.Model):
    __tablename__ = 'Events'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    datetime = db.Column(db.String(140))
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'))
    venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'))

    def __repr__(self):
        return '<Upcoming Events: {} featuring {} at {} on {}>'.format(self.title, self.artist_id, self.venue_id, self.datetime)

class Venues(db.Model):
    __tablename__ = 'Venues'
    id = db.Column(db.Integer, primary_key=True)
    placename = db.Column(db.String(200))
    location = db.Column(db.String(200))
    events = db.relationship('Events', backref='events', lazy='dynamic')

    def __repr__(self):
        return '<Venue: {}, Address: {}>'.format(self.placename, self.location)