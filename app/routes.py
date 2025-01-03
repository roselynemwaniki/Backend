from fastapi import APIRouter, HTTPException, Depends  
from sqlalchemy.orm import Session  
from .models import User, Movie, Recommendation, SessionLocal  # Import the models and session  
from typing import List
  

router = APIRouter()  

# Dependency to get the database session  
def get_db():  
    db = SessionLocal()  
    try:  
        yield db  
    finally:  
        db.close()  

# User Endpoints  
@router.post("/users/")  
def create_user(username: str, email: str, password: str, db: Session = Depends(get_db)):  
    db_user = User(username=username, email=email, password=password)  
    db.add(db_user)  
    db.commit()  
    db.refresh(db_user)  
    return {"id": db_user.id, "username": db_user.username, "email": db_user.email}  

@router.get("/users/{user_id}")  
def get_user(user_id: int, db: Session = Depends(get_db)):  
    user = db.query(User).filter(User.id == user_id).first()  
    if not user:  
        raise HTTPException(status_code=404, detail="User not found")  
    return {"id": user.id, "username": user.username, "email": user.email}  

@router.delete("/users/{user_id}")  
def delete_user(user_id: int, db: Session = Depends(get_db)):  
    db_user = db.query(User).filter(User.id == user_id).first()  
    if not db_user:  
        raise HTTPException(status_code=404, detail="User not found")  
    db.delete(db_user)  
    db.commit()  
    return {"detail": f"User with ID {user_id} has been deleted"}  

# Movie Endpoints  
@router.post("/movies/")  
def create_movie(title: str, genre: str, release_year: int, description: str, image_url : str, db: Session = Depends(get_db)):  
    db_movie = Movie(title=title, genre=genre, release_year=release_year, description=description, image_url=image_url)  
    db.add(db_movie)  
    db.commit()  
    db.refresh(db_movie)  
    return {"id": db_movie.id, "title": db_movie.title, "genre":db_movie.genre, "release_year": db_movie.release_year, "description": db_movie.description, "image_url": db_movie.image_url}  

@router.get("/movies/", response_model=List[dict])  
def get_movies(db: Session = Depends(get_db)):  
    movies = db.query(Movie).all()  
    return [{"id": movie.id, "title": movie.title, 
             "genre": movie.genre, "release_year": movie.release_year, "description": movie.description
             } for movie in movies]  

@router.get("/movies/{movie_id}")  
def get_movie(movie_id: int, db: Session = Depends(get_db)):  
    movie = db.query(Movie).filter(Movie.id == movie_id).first()  
    if not movie:  
        raise HTTPException(status_code=404, detail="Movie not found")  
    return {"id": movie.id, "title": movie.title, 
            "genre": movie.genre, "release_year": movie.release_year, "description": movie.description
            }  

@router.delete("/movies/{movie_id}")  
def delete_movie(movie_id: int, db: Session = Depends(get_db)):  
    db_movie = db.query(Movie).filter(Movie.id == movie_id).first()  
    if not db_movie:  
        raise HTTPException(status_code=404, detail="Movie not found")  
    db.delete(db_movie)  
    db.commit()  
    return {"detail": f"Movie with ID {movie_id} has been deleted"}  

# Recommendation Endpoints  
@router.post("/recommendations/")  
def create_recommendation(user_id: int, movie_id: int, rating: float, db: Session = Depends(get_db)):  
    db_rec = Recommendation(user_id=user_id, movie_id=movie_id, rating=rating)  
    db.add(db_rec)  
    db.commit()  
    db.refresh(db_rec)  
    return {"id": db_rec.id, "user_id": db_rec.user_id, "movie_id": db_rec.movie_id, "rating": db_rec.rating}  

@router.get("/recommendations/", response_model=List[dict])  
def get_recommendations(db: Session = Depends(get_db)):  
    recommendations = db.query(Recommendation).all()  
    return [{"id": rec.id, "user_id": rec.user_id, "movie_id": rec.movie_id, "rating": rec.rating} for rec in recommendations]  

@router.delete("/recommendations/{rec_id}")  
def delete_recommendation(rec_id: int, db: Session = Depends(get_db)):  
    db_rec = db.query(Recommendation).filter(Recommendation.id == rec_id).first()  
    if not db_rec:  
        raise HTTPException(status_code=404, detail="Recommendation not found")  
    db.delete(db_rec)  
    db.commit()  
    return {"detail": f"Recommendation with ID {rec_id} has been deleted"}
