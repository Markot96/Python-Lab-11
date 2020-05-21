from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from animalShop.model.Animal import Animal
import os
import json
import copy

from animalShop.model.Animal import Animal

with open('secret.json') as f:
    SECRET = json.load(f)

DB_URI = "mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}".format(
    user=SECRET["user"],
    password=SECRET["password"],
    host=SECRET["host"],
    port=SECRET["port"],
    db=SECRET["db"])

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


class VirtualAnimal(Animal, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=False)
    age_in_months = db.Column(db.Integer, unique=False)
    sex = db.Column(db.String(32), unique=False)
    biological_class = db.Column(db.String(32), unique=False)
    height_in_meters = db.Column(db.Float, unique=False)
    length_in_meters = db.Column(db.Float, unique=False)
    food_per_day_in_kg = db.Column(db.Float, unique=False)
    food_type = db.Column(db.String(64), unique=False)
    price_in_uah = db.Column(db.Float, unique=False)
    creator = db.Column(db.String(32), unique=False)
    memory_require = db.Column(db.Float, unique=False)

    def __init__(self, name=None, age_in_months=None, sex=None, biological_class=None, height_in_meters=None, length_in_meters=None,
                 food_per_day_in_kg=None, food_type=None, price_in_uah=None, creator=None, memory_require=None):
        super().__init__(name, age_in_months, sex, biological_class, height_in_meters, length_in_meters, food_per_day_in_kg, food_type, price_in_uah)
        # new field
        self.creator = creator
        # new field
        self.memory_require = memory_require


class VirtualAnimalSchema(ma.Schema):
    class Meta:
        fields = ('name', 'age_in_months', 'sex', 'biological_class',
                  'height_in_meters', 'length_in_meters', 'food_per_day_in_kg',
                  'food_type', 'price_in_uah', 'creator', 'memory_require')


virtual_animal_schema = VirtualAnimalSchema()
virtual_animals_schema = VirtualAnimalSchema(many=True)


@app.route("/virtual_animal", methods=["POST"])
def add_virtual_animal():
    virtual_animal = VirtualAnimal(request.json['name'],
                                    request.json['age_in_months'],
                                    request.json['sex'],
                                    request.json['biological_class'],
                                    request.json['height_in_meters'],
                                    request.json['length_in_meters'],
                                    request.json['food_per_day_in_kg'],
                                    request.json['food_type'],
                                    request.json['price_in_uah'],
                                    request.json['creator'],
                                    request.json['memory_require'])
    db.session.add(virtual_animal)
    db.session.commit()
    return virtual_animal_schema.jsonify(virtual_animal)


@app.route("/virtual_animal", methods=["GET"])
def get_virtual_animal():
    all_virtual_animal = VirtualAnimal.query.all()
    result = virtual_animals_schema.dump(all_virtual_animal)
    return jsonify({'virtual_animals': result})


@app.route("/virtual_animal/<id>", methods=["GET"])
def virtual_animal_detail(id):
    virtual_animal = VirtualAnimal.query.get(id)
    if not virtual_animal:
        abort(404)
    return virtual_animal_schema.jsonify(virtual_animal)


@app.route("/virtual_animal/<id>", methods=["PUT"])
def virtual_animal_update(id):
    virtual_animal = VirtualAnimal.query.get(id)
    if not virtual_animal:
        abort(404)
    virtual_animal.name = request.json['name']
    virtual_animal.age_in_months = request.json['age_in_months']
    virtual_animal.sex = request.json['sex']
    virtual_animal.biological_class = request.json['biological_class']
    virtual_animal.height_in_meters = request.json['height_in_meters']
    virtual_animal.length_in_meters = request.json['length_in_meters']
    virtual_animal.food_per_day_in_kg = request.json['food_per_day_in_kg']
    virtual_animal.food_type = request.json['food_type']
    virtual_animal.price_in_uah = request.json['price_in_uah']
    virtual_animal.creator = request.json['creator']
    virtual_animal.memory_require = request.json['memory_require']
    db.session.commit()
    return virtual_animal_schema.jsonify(virtual_animal)


@app.route("/virtual_animal/<id>", methods=["DELETE"])
def virtual_animal_delete(id):
    virtual_animal = VirtualAnimal.query.get(id)
    if not virtual_animal:
        abort(404)
    db.session.delete(virtual_animal)
    db.session.commit()
    return virtual_animal_schema.jsonify(virtual_animal)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host='0.0.0.0')
