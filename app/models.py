from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Movie(db.Model):
    __tablename__ = 'movies' # Required to name the table "movies" 

    id = db.Column(db.Integer, primary_key=True) # [cite: 110]
    title = db.Column(db.String(255), nullable=False) # [cite: 111]
    description = db.Column(db.Text, nullable=False) # [cite: 112]
    poster = db.Column(db.String(255), nullable=False) # [cite: 113]
    created_at = db.Column(db.DateTime, default=datetime.utcnow) # [cite: 114]

    def __init__(self, title, description, poster):
        self.title = title
        self.description = description
        self.poster = poster