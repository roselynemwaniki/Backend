from flask import Blueprint, jsonify, request
from .models import db, Movie, Review, User

main = Blueprint('main', __name__)

@main.route('/movies', methods=['GET'])
def get_movies():
    movies = Movie.query.all()
    return jsonify([{"id": movie.id, "title": movie.title, "genre": movie.genre, "release_year": movie.release_year} for movie in movies])

@main.route('/movies', methods=['POST'])
def add_movie():
    data = request.get_json()
    new_movie = Movie(
        title=data['title'],
        genre=data['genre'],
        release_year=data['release_year'],
        description=data.get('description')
    )
    db.session.add(new_movie)
    db.session.commit()
    return jsonify({"message": f"Movie '{new_movie.title}' added successfully!"}), 201

@main.route('/reviews', methods=['POST'])
def add_review():
    data = request.get_json()
    new_review = Review(
        user_id=data['user_id'],
        movie_id=data['movie_id'],
        review=data['review'],
        rating=data['rating']
    )
    db.session.add(new_review)
    db.session.commit()
    return jsonify({"message": "Review added successfully!"}), 201