from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User (db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30), nullable = False)
    password = db.Column(db.String(10), nullable = False)
    email = db.Column(db.String(30), nullable = False)
    isActive = db.Column(db.Boolean, default = False)

    def __repr__(self):
        return "<User %r>" % self.id

    def serialize(self): 
        return {
            "id": self.id,
            "name": self.name,
            "password": self.password,
            "email": self.email,
            "isActive": self.isActive
        }

class Character (db.Model):
    __tablename__ = 'character'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30), nullable = False)
    height = db.Column(db.String(10))
    mass = db.Column(db.String(10))
    hair_color = db.Column(db.String(20))
    skin_color = db.Column(db.String(20))
    eye_color = db.Column(db.String(20))
    birth_year = db.Column(db.String(20))
    gender = db.Column(db.String(20))
    homeworld = db.Column(db.String(100))
    films = db.Column(db.String(300))
    species = db.Column(db.String(50))
    vehicles = db.Column(db.String(300))
    starships = db.Column(db.String(300))
   
    def __repr__(self):
        return "<Character %r>" % self.id

    def serialize(self): 
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
            "gender": self.gender,
            "homeworld": self.homeworld,
            "films": self.films,
            "species": self.species,
            "vehicles": self.vehicles,
            "starships": self.starships
        }

class Planet (db.Model):
    __tablename__ = 'planet'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20), nullable = False)
    rotation_period = db.Column(db.String(20))
    orbital_period = db.Column(db.String(20))
    diameter = db.Column(db.String(100))
    climate = db.Column(db.String(100))
    gravity = db.Column(db.String(100))
    terrain = db.Column(db.String(100))
    surface_water = db.Column(db.String(100))
    population = db.Column(db.String(100))
    residents = db.Column(db.String(300))
    films = db.Column(db.String(300))
   
    def __repr__(self):
        return "<Planet %r>" % self.id

    def serialize(self): 
        return {
            "id": self.id,
            "name": self.name,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "diameter": self.diameter,
            "climate": self.climate,
            "gravity": self.gravity,
            "terrain": self.terrain,
            "surface_water": self.surface_water,
            "population": self.population,
            "residents": self.residents,
            "films": self.films
        }

class Starship (db.Model):
    __tablename__ = 'starship'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20), nullable = False)
    model = db.Column(db.String(50))
    manufacturer = db.Column(db.String(100))
    cost_in_credits = db.Column(db.String(100))
    length = db.Column(db.String(50))
    max_atmosphering_speed = db.Column(db.String(50))
    crew = db.Column(db.String(50))
    passengers = db.Column(db.String(20))
    cargo_capacity = db.Column(db.String(20))
    consumables = db.Column(db.String(20))
    hyperdrive_rating = db.Column(db.String(20))
    MGLT = db.Column(db.String(20))
    starship_class = db.Column(db.String(30))
    pilots = db.Column(db.String(50))
    films = db.Column(db.String(300))
   
    def __repr__(self):
        return "<Starship %r>" % self.id

    def serialize(self): 
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "manufacturer": self.manufacturer,
            "cost_in_credits": self.cost_in_credits,
            "length": self.length,
            "max_atmosphering_speed": self.max_atmosphering_speed,
            "crew": self.crew,
            "passengers": self.passengers,
            "cargo_capacity": self.cargo_capacity,
            "consumables": self.consumables,
            "hyperdrive_rating": self.hyperdrive_rating,
            "MGLT": self.MGLT,
            "starship_class": self.starship_class,
            "pilots": self.pilots,
            "films": self.films,
        }