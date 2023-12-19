from models.movie import Movie as MovieModel
from schemas.movie import Movie
from fastapi.responses import JSONResponse
class MovieService():
    
    def __init__(self, db) -> None:
        self.db = db

    def get_movies(self):
        result = self.db.query(MovieModel).all()
        return result

    def get_movie(self, id):
        result = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        return result
    def get_movies_by_category(self, category):
        result = self.db.query(MovieModel).where(MovieModel.category == category).all()
        return result
    def create_movie(self, movie: Movie):
        new_movie = MovieModel(**movie.dict())
        self.db.add(new_movie)
        self.db.commit()
    def update_movie(self, movie: Movie):
        result = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        if not result:
            return JSONResponse(status_code=404, content={"message":"No encontrado"})
     
        result.title = movie.title
        result.overview = movie.overview
        result.year = movie.year
        result.rating = movie.rating
        result.category = movie.category
        self.db.commit()
        return JSONResponse(status_code=200, content={"message": "Se ha modificado la película"})

    def delete_movie(self, id):
        result = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        if not result:
            return JSONResponse(status_code=404, content={"message":"No encontrado"})
        
        self.db.delete(result)
        self.db.commit()
        return JSONResponse(status_code=200, content={"message": "Se ha eliminado la película"})