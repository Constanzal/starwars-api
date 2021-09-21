import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from models import db, User, Character, Planet, Starship
from flask_migrate import Migrate

BASEDIR = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(BASEDIR, "test.db") 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['ENV'] = 'development'
app.config['DEBUG'] = True

db.init_app(app)
Migrate(app, db)

@app.route("/")
def Home():
  return jsonify("Hola Mundo")

@app.route("/user", methods = ["POST", "GET"])
def user():
    if request.method == "GET":
        users = User.query.all()
        users = list(map(lambda user: user.serialize(), users))
        return jsonify(users)
    else:
        user = User()
        user.name = request.json.get("name")
        user.password = request.json.get("password")
        user.email = request.json.get("email")
        user.isActive = request.json.get("isActive")

        db.session.add(user)
        db.session.commit()

        return jsonify(user.serialize()), 200


@app.route("/character", methods = ["POST", "GET"])
def character():
    if request.method == "GET":
        characters = Character.query.all()
        characters = list(map(lambda character: character.serialize(), characters))
        return jsonify(characters)
    else:
        character = Character()
        character.name = request.json.get("name")
        character.height = request.json.get("height")
        character.mass = request.json.get("mass")
        character.hair_color = request.json.get("hair_color")
        character.skin_color = request.json.get("skin_color")
        character.eye_color = request.json.get("eye_color")
        character.birth_year = request.json.get("birth_year")
        character.gender = request.json.get("gender")
        character.homeworld = request.json.get("homeworld")
        character.films = request.json.get("films")
        character.species = request.json.get("species")
        character.vehicles = request.json.get("vehicles")
        character.starships = request.json.get("starships")

        db.session.add(character)
        db.session.commit()

        return jsonify(character.serialize()), 200


@app.route("/planet", methods = ["POST", "GET"])
def planet():
    if request.method == "GET":
        planets = Planet.query.all()
        planets = list(map(lambda planet: planet.serialize(), planets))
        return jsonify(planets)
    else:
        planet = Planet()
        planet.name = request.json.get("name")
        planet.rotation_period = request.json.get("rotation_period")
        planet.orbital_period = request.json.get("orbital_period")
        planet.diameter = request.json.get("diameter")
        planet.climate = request.json.get("climate")
        planet.gravity = request.json.get("gravity")
        planet.terrain = request.json.get("terrain")
        planet.surface_water = request.json.get("surface_water")
        planet.population = request.json.get("population")
        planet.residents = request.json.get("residents")
        planet.films = request.json.get("films")

        db.session.add(planet)
        db.session.commit()

        return jsonify(planet.serialize()), 200


@app.route("/starship", methods = ["POST", "GET"])
def starship():
    if request.method == "GET":
        starships = Starship.query.all()
        starships = list(map(lambda starship: starship.serialize(), starships))
        return jsonify(starships)
    else:
        starship = Starship()
        starship.name = request.json.get("name")
        starship.model = request.json.get("model")
        starship.manufacturer = request.json.get("manufacturer")
        starship.cost_in_credits = request.json.get("cost_in_credits")
        starship.length = request.json.get("length")
        starship.max_atmosphering_speed = request.json.get("max_atmosphering_speed")
        starship.crew = request.json.get("crew")
        starship.passengers = request.json.get("passengers")
        starship.cargo_capacity = request.json.get("cargo_capacity")
        starship.consumables = request.json.get("consumables")
        starship.hyperdrive_rating = request.json.get("hyperdrive_rating")
        starship.MGLT = request.json.get("MGLT")
        starship.starship_class = request.json.get("starship_class")
        starship.pilots= request.json.get("pilots")
        starship.films = request.json.get("films")

        db.session.add(starship)
        db.session.commit()
    
        return jsonify(starship.serialize()), 200


if __name__ == "__main__":
    app.run(host ="localhost", port = 8080)