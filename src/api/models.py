from flask_sqlalchemy import SQLAlchemy
import enum
db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    favourites = db.relationship("Favourite", backref="user")

    def __repr__(self):
        return f'<User {self.username}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "username": self.username
            # do not serialize the password, its a security breach
        }

class Category(enum.Enum):
    characters = "character"
    episodes = "episode"
    locations = "location"
 

class Favourite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    category = db.Column(db.Enum(Category), server_default="characters")
    character_id = db.Column(db.Integer, db.ForeignKey("character.id") , nullable=True)
    location_id = db.Column(db.Integer, db.ForeignKey("location.id") , nullable=True)
    episode_id = db.Column(db.Integer, db.ForeignKey("episode.id") , nullable=True)

  


class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    species = db.Column(db.String(80), nullable=False)
    favourites = db.relationship("Favourite", backref="character")

    def __repr__(self):
        return f'<Character {self.name}>'


class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    type = db.Column(db.String(80))
    favourites = db.relationship("Favourite", backref="location")

    def __repr__(self):
        return f'<Location {self.name}>'


class Episode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    air_date = db.Column(db.String(50))
    favourites = db.relationship("Favourite", backref="episode")

    def __repr__(self):
       return f'<Episode {self.name}>'