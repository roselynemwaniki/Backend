from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from sqlalchemy.ext.declarative import declarative_base

# Database configuration
DATABASE_URL = "sqlite:///./test.db"  # Use your actual database URL

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create a new sessionmaker instance
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for your models
Base = declarative_base()

# User Model
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    recommendations = relationship("Recommendation", back_populates="user")

# Movie Model
class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    genre = Column(String)
    release_year = Column(Integer)
    description = Column(String)
    image_url = Column(String)

    recommendations = relationship("Recommendation", back_populates="movie")

# Recommendation Model
class Recommendation(Base):
    __tablename__ = 'recommendations'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    movie_id = Column(Integer, ForeignKey('movies.id'))
    rating = Column(Float)

    user = relationship("User", back_populates="recommendations")
    movie = relationship("Movie", back_populates="recommendations")

# Create the database tables
Base.metadata.create_all(bind=engine)
