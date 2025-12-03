from fastapi import FastAPI, Body

app=FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author One', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]

@app.get("/books")
def read_all_books(category:str):
    return BOOKS

@app.get("/books/")
def read_category_by_query(category:str):
    book_to_return=[]
    for book in BOOKS:
        if book.get('category').casefold()==category.casefold():
            book_to_return.append(book)
    return book_to_return


#Path parameter
@app.get("/books/{book_title}")
def read_book(book_title:str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book



#Query Parameter
@app.get("/books/byauthor/")
def read_books_by_author_path(author:str):
    book_to_return=[]
    for book in BOOKS:
        if book.get('author').casefold()==author.casefold():
            book_to_return.append(book)
    return book_to_return


@app.get("/books/{book_author}/")
def read_author_category_by_query(book_author:str, category:str):
    book_to_return=[]
    for book in BOOKS:
        if book.get('author').casefold()==book_author.casefold() and book.get('category').casefold()==category.casefold():
            book_to_return.append()
    return book_to_return

#Creating the post method to create a book detail
@app.post("/books/create_book")
def create_book(new_book=Body()):
    BOOKS.append(new_book)

#creating put method to update Book detail
@app.put("/book/update_book")
def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold()==updated_book.get('title').casefold():
            BOOKS[i]=updated_book

#Creating the endpoint using the DELETE Method
#Path Parameter since we want to identify the resource and then delete 
@app.delete("/books/delete_book/{book_title}/") 
def delete_book(book_title:str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold()==book_title.casefold():
            BOOKS.pop(i)
            break


#Create a new API Endpoint that can fetch all books from a specific author using either Path Parameters or Query Parameters

@app.get("/books/assignment/{book_author}")
def fetch_book(book_author):
    book_to_return=[]
    for i in range(len(BOOKS)):
        if BOOKS[i].get('author').casefold()==book_author.casefold():
            book_to_return.append(BOOKS[i])
    return book_to_return

@app.get("/books/assignment/byauthor/")
def fetch_book(author:str):
    book_to_return=[]
    for i in range(len(BOOKS)):
        if BOOKS[i].get("author").casefold()==author.casefold():
            book_to_return.append(BOOKS[i])
    return book_to_return