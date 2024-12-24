from .models import db, Movie, User, Review
from .__init__ import create_app

app = create_app()

@app.cli.command('init-db')
def init_db():
    """Initialize the database."""
    with app.app_context():
        db.drop_all()
        db.create_all()
        print("Database initialized!")

@app.cli.command('seed-data')
def seed_data():
    """Seed the database with sample data."""
    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()

        # Create sample movies
        movie1 = Movie(title="Inception", genre="Sci-Fi", description="A thief steals secrets using dream-sharing.")
        movie2 = Movie(title="The Dark Knight", genre="Action", description="Batman faces the Joker.")
        
        # Create sample users
        user1 = User(username="john_doe", email="john@example.com")
        user2 = User(username="jane_smith", email="jane@example.com")

        # Create sample reviews
        review1 = Review(movie=movie1, user=user1, rating=5, comment="Mind-blowing experience!")
        review2 = Review(movie=movie2, user=user2, rating=4, comment="Great action and storytelling.")
        review3 = Review(movie=movie1, user=user2, rating=4, comment="A complex but rewarding film.")

        # Add all to the session
        db.session.add_all([movie1, movie2, user1, user2, review1, review2, review3])
        db.session.commit()
        print("Sample data added!")
