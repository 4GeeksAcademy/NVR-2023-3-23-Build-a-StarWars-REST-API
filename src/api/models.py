from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    favourites = db.relationship("Favourite", backref="user")

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Favourite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    category = db.Column(db.Enum('characters', 'locations', 'episodes'))
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'))
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'))
    episode_id = db.Column(db.Integer, db.ForeignKey('episode.id'))

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    species = db.Column(db.String(80), nullable=False)
    favourites = db.relationship("Favourite", backref="character")

class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    type = db.Column(db.String(80))
    favourites = db.relationship("Favourite", backref="location")

class Episode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    air_date = db.Column(db.String(10))
    favourites = db.relationship("Favourite", backref="episode")