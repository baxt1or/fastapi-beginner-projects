from fastapi import FastAPI
from src.books.routes import book_routes


version = "v1"


app = FastAPI(
    title="Book Management System",
    description= "My First REST API with Python FastAPI",
    version=version
)


app.include_router(book_routes, prefix=f"/api/{version}/books")