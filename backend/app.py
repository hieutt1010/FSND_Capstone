from flask import Flask, request, jsonify, abort
from models import db, Movie, Actor

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///casting_agency.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/actors', methods=['GET'])
def get_actors():
    actors = Actor.query.all()
    return jsonify({'success': True, 'actors': [actor.name for actor in actors]})

@app.route('/movies', methods=['GET'])
def get_movies():
    movies = Movie.query.all()
    return jsonify({'success': True, 'movies': [movie.title for movie in movies]})

@app.route('/actors', methods=['POST'])
def add_actor():
    data = request.get_json()
    actor = Actor(name=data['name'], age=data['age'], gender=data['gender'])
    db.session.add(actor)
    db.session.commit()
    return jsonify({'success': True, 'actor': actor.name}), 201

@app.route('/actors/<int:id>', methods=['PATCH'])
def update_actor(id):
    actor = Actor.query.get(id)
    if not actor:
        abort(404)
    data = request.get_json()
    if 'name' in data:
        actor.name = data['name']
    if 'age' in data:
        actor.age = data['age']
    db.session.commit()
    return jsonify({'success': True, 'actor': actor.name})

@app.route('/actors/<int:id>', methods=['DELETE'])
def delete_actor(id):
    actor = Actor.query.get(id)
    if not actor:
        abort(404)
    db.session.delete(actor)
    db.session.commit()
    return jsonify({'success': True, 'deleted': id})
