## Movie Recommendation System - Backend

## Overview
The backend of the Movie Recommendation System serves as the core of the application, handling data storage, retrieval, and processing. It is built using Python and Flask, with a SQLite database to store movie information and reviews.

## Project Structure
The backend folder is organized as follows:

Backend/
├── app/
│   ├── __init__.py          # Initializes the Flask app
│   ├── cli.py               # Custom CLI commands for database management
│   ├── models.py            # Defines database models for movies and reviews
│   ├── routes.py            # Contains API routes for handling HTTP requests
│   ├── database.py          # Handles database connection setup
├── instance/
│   ├── movies.sqlite        # SQLite database for storing data
├── main.py                  # Entry point for running the Flask app
├── movies.sqlite            # Primary database file
├── Pipfile                  # Dependencies for the backend
├── Pipfile.lock             # Dependency lock file
├── test.db                  # Test database for development or testing purposes

## Features
RESTful API Endpoints:

Fetch movie details, reviews, and other related data.

Create, update, and delete movies and reviews.

Database Models:

Movies: Stores information about movies.

Reviews: Stores reviews and ratings for movies.

Custom CLI Commands:

Manage database setup and migrations using cli.py.

Flask Framework:

Lightweight and efficient web framework for building APIs.

## Setup and Installation
Prerequisites
Python 3.8 or later

Pipenv for dependency management

Steps
Clone the repository:

git clone <repository-url>
cd Backend
Set up the virtual environment and install dependencies:

pipenv install
pipenv shell
Run database migrations to set up the SQLite database:

flask db init
flask db migrate
flask db upgrade
Start the Flask development server:

python main.py
The server will be available at http://127.0.0.1:5000.

Running Tests
To run tests, ensure the test.db database is set up and execute the test scripts.

## API Routes
Below are some key API endpoints:

Movies

GET /movies: Fetch all movies.

POST /movies: Add a new movie.

PUT /movies/<id>: Update an existing movie.

DELETE /movies/<id>: Delete a movie.

Reviews

GET /reviews: Fetch all reviews.

POST /reviews: Add a new review.

## Technologies Used
Python: Programming language.

Flask: Web framework for building the backend.

SQLite: Database for storing application data.

Pipenv: Dependency management.

## Future Enhancements
Implement advanced search and filtering for movies.

Add user authentication and authorization.

Integrate recommendation algorithms for personalized suggestions.
