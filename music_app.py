from app import app, db
from app.models import Artist, Events, Venues

with app.app_context():
    db.create_all()