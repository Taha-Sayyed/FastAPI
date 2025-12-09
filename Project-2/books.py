from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel,Field
from starlette import status #For Explicit status code Response


app=FastAPI()

class Book:

    #data member
    id:int
    title:str
    author:str
    description:str
    rating:int
    published_date:int

    #constructor
    def __init__(self,id,title,author,description,rating,published_date):
        self.id=id
        self.title=title
        self.author=author
        self.description=description
        self.rating=rating
        self.published_date=published_date

# This class is responsible for Validation using pydantic model by taking BaseModel 
class BookRequest(BaseModel):
    id:int=Field(description="ID is not needed on create",default=None)
    title:str=Field(min_length=3)
    author:str=Field(min_length=3)
    description:str=Field(min_length=3,max_length=50)
    rating:int=Field(gt=0,le=6)
    published_date:int=Field(gt=1999,le=2020)

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "A new book",
                "author": "codingwithroby",
                "description": "A new description of a book",
                "rating": 5,
                'published_date': 2029
            }
        }
    }



BOOKS = [
    Book(1, 'Computer Science Pro', 'codingwithroby', 'A very nice book!', 5, 2030),
    Book(2, 'Be Fast with FastAPI', 'codingwithroby', 'A great book!', 5, 2030),
    Book(3, 'Master Endpoints', 'codingwithroby', 'A awesome book!', 5, 2029),
    Book(4, 'HP1', 'Author 1', 'Book Description', 2, 2028),
    Book(5, 'HP2', 'Author 2', 'Book Description', 3, 2027),
    Book(6, 'HP3', 'Author 3', 'Book Description', 1, 2026)
]

def find_book_id(book:Book):
    if len(BOOKS)>0:
        book.id=BOOKS[-1].id+1
    else:
        book.id=1
    return book


@app.get("/books",status_code=status.HTTP_200_OK)
def get_book():
    return BOOKS

@app.post("/create-book",status_code=status.HTTP_201_CREATED)
def create_book(book_request:BookRequest): #FastAPI will show BookRequest schema (example/model) in the API docs
    new_book=Book(**book_request.model_dump()) # Convert BookRequest model into a Book model
    # **operator pass the key-value pair from the BodyRequest() into the Book() constructor
    BOOKS.append(find_book_id(new_book))
    

#added Path parameter validation
@app.get("/books/{book_id}",status_code=status.HTTP_200_OK)
def get_book_by_id(book_id:int=Path(gt=0)):
    for book in BOOKS:
        if book.id==book_id:
            return book
    raise HTTPException(status_code=404,detail="Item not found")
        

@app.get("/books/{book_rating}")
def get_book_by_rating(book_rating:int):
    for book in BOOKS:
        if book.rating==book_rating:
            return book
        
@app.put("/books/update_book",status_code=status.HTTP_204_NO_CONTENT)
def update_book(book:BookRequest):
    book_changed=False
    for i in range(len(BOOKS)):
        if BOOKS[i].id==book.id:
            BOOKS[i]=book
            book_changed=True
    if not book_changed:
        raise HTTPException(status_code=404,detail="Items not found")
        

@app.delete("/books/{book_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id:int=Path(gt=0)):
    book_retrieve_to_delete=False
    for i in range(len(BOOKS)):
        if BOOKS[i].id==book_id:
            BOOKS.pop(i)
            book_retrieve_to_delete=True
            break
    if not book_retrieve_to_delete:
        return HTTPException(status_code=404,detail="Item not found")

@app.get("/books/publish_date/{published_date}")
def get_book_by_publishDate(published_date:int=Path(gt=0)):
    for i in range(len(BOOKS)):
        if BOOKS[i].published_date==published_date:
            return BOOKS[i]
        
@app.get("/books/publish_date")
def get_book_by_publishDate(published_date:int=Query(gt=0)):
    for i in range(len(BOOKS)):
        if BOOKS[i].published_date==published_date:
            return BOOKS[i]