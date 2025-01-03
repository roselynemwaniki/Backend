import click  
from sqlalchemy import create_engine  
from sqlalchemy.orm import sessionmaker, declarative_base  
from sqlalchemy.orm import Session  
from sqlalchemy import Column, Integer, String, Float, ForeignKey  
from sqlalchemy.ext.declarative import declarative_base

# Database configuration  
DATABASE_URL = "sqlite:///./test.db"  # Adjust this to your database URL  
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})  
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)  
Base = declarative_base()  

# SQLAlchemy Models  
class User(Base):  
    __tablename__ = 'users'  

    id = Column(Integer, primary_key=True, index=True)  
    username = Column(String, unique=True, index=True)  
    email = Column(String, unique=True, index=True)  
    password = Column(String)  

class Movie(Base):  
    __tablename__ = 'movies'  

    id = Column(Integer, primary_key=True, index=True)  
    title = Column(String)  
    genre = Column(String)  
    release_year = Column(Integer)  
    description = Column(String)
    image_url = Column(String)  

class Recommendation(Base):  
    __tablename__ = 'recommendations'  

    id = Column(Integer, primary_key=True, index=True)  
    user_id = Column(Integer, ForeignKey('users.id'))  
    movie_id = Column(Integer, ForeignKey('movies.id'))  
    rating = Column(Float)  

# Create the database tables  
Base.metadata.create_all(bind=engine)  

# Dependency to get the database session  
def get_db():  
    db = SessionLocal()  
    try:  
        yield db  
    finally:  
        db.close()  

@click.group()  
def cli():  
    """Command line interface for the movie recommendation application."""  
    pass  

@cli.command()  
@click.argument('username')  
@click.argument('email')  
@click.argument('password')  
def create_user(username: str, email: str, password: str):  
    """Create a new user."""  
    db = next(get_db())  
    user = User(username=username, email=email, password=password)  
    db.add(user)  
    db.commit()  
    db.refresh(user)  
    click.echo(f'Created user: {user.username} (ID: {user.id})')  

@cli.command()  
@click.argument('title')  
@click.argument('genre')  
@click.argument('release_year', type=int)  
@click.argument('description') 
@click.argument('image_url')
def create_movie(title: str, genre: str, release_year: int, description: str, image_url: str):  
    """Create a new movie."""  
    db = next(get_db())  
    movie = Movie(title=title, genre=genre, release_year=release_year, description=description, image_url=image_url)  
    db.add(movie)  
    db.commit()  
    db.refresh(movie)  
    click.echo(f'Created movie: {movie.title} (ID: {movie.id})')  

@cli.command()  
@click.argument('user_id', type=int)  
@click.argument('movie_id', type=int)  
@click.argument('rating', type=float)  
def create_recommendation(user_id: int, movie_id: int, rating: float):  
    """Create a new movie recommendation."""  
    db = next(get_db())  
    rec = Recommendation(user_id=user_id, movie_id=movie_id, rating=rating)  
    db.add(rec)  
    db.commit()  
    db.refresh(rec)  
    click.echo(f'Created recommendation: User {rec.user_id} for movie {rec.movie_id} with rating {rec.rating}')  

@cli.command()  
@click.argument('user_id', type=int)  
def delete_user(user_id: int):  
    """Delete a user by ID."""  
    db = next(get_db())  
    db_user = db.query(User).filter(User.id == user_id).first()  
    if not db_user:  
        click.echo(f'User with ID {user_id} not found.')  
        return  
    db.delete(db_user)  
    db.commit()  
    click.echo(f'Deleted user: {user_id}')  

@cli.command()  
@click.argument('movie_id', type=int)  
def delete_movie(movie_id: int):  
    """Delete a movie by ID."""  
    db = next(get_db())  
    db_movie = db.query(Movie).filter(Movie.id == movie_id).first()  
    if not db_movie:  
        click.echo(f'Movie with ID {movie_id} not found.')  
        return  
    db.delete(db_movie)  
    db.commit()  
    click.echo(f'Deleted movie: {movie_id}')  

@cli.command()  
@click.argument('rec_id', type=int)  
def delete_recommendation(rec_id: int):  
    """Delete a recommendation by ID."""  
    db = next(get_db())  
    db_rec = db.query(Recommendation).filter(Recommendation.id == rec_id).first()  
    if not db_rec:  
        click.echo(f'Recommendation with ID {rec_id} not found.')  
        return  
    db.delete(db_rec)  
    db.commit()  
    click.echo(f'Deleted recommendation: {rec_id}')  

if __name__ == '__main__':  
    cli()

