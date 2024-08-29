from fastapi import APIRouter, status, HTTPException
from typing import List
from src.books.schema import Book
from src.books.book_data import books


book_routes = APIRouter()




@book_routes.get("/", response_model=List[Book])
async def get_all_books():
    return books


@book_routes.get("/{id}")
async def get_book(id:int) -> dict:
    for book in books:
        if book["id"] == id:
            return book
    raise HTTPException(status.HTTP_404_NOT_FOUND)

@book_routes.post("/", status_code=status.HTTP_201_CREATED)
async def create_book(book:Book) -> dict:
    created_book = book.model_dump()
    books.append(created_book)
    return created_book


@book_routes.patch("/{id}", response_model=Book)
async def update_book(id: int, updated_book:Book) -> dict:
    for book in books:
        if book["id"] == id:
            book["title"] = updated_book.title
            book["author"] = updated_book.author
            book["page"] = updated_book.page
            book["language"] = updated_book.language
            book["published_year"] = updated_book.published_year

            return book
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@book_routes.delete("/{id}")
async def delete_book(id :int) -> dict:
    for index, book in enumerate(books):
        if book["id"] == id:
            deleted_book = books.pop(index)

            return deleted_book
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)




