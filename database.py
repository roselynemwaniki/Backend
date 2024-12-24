from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Database URL from an environment variable (or hardcoded for simplicity)
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./movies.sqlite")  # Example for SQLite

# Create an engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})  # For SQLite

# Create a SessionLocal class for database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for declarative models
Base = declarative_base()

# Dependency to get a database session for each request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
