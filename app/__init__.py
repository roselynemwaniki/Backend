from fastapi import FastAPI
from .routes import router as movie_recommendation_router
from .models import Base, engine

def create_app():
    # Create the FastAPI app instance
    app = FastAPI()

    # Include the router for movie recommendations
    app.include_router(movie_recommendation_router)

    # Create the database tables (this could be done in a separate setup script if preferred)
    Base.metadata.create_all(bind=engine)

    return app
