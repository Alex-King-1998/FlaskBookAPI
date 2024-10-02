Book API
A simple RESTful API built with Flask to manage a collection of books. This API allows users to retrieve a list of books and add new books, with data stored in a JSON file for persistence across server restarts.

Features
Retrieve all books: Get a list of all books in the collection.
Add a new book: Submit a new book by providing the title and author.
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/bookapi.git
cd bookapi
Install the required dependencies:

bash
Copy code
pip install flask
Run the application:

bash
Copy code
python app.py
Access the API at http://127.0.0.1:5000/.

API Endpoints
GET /books: Retrieve the list of all books.

Example:

bash
Copy code
curl http://127.0.0.1:5000/books
POST /books: Add a new book (requires JSON body with title and author).

Example:

bash
Copy code
curl -X POST -H "Content-Type: application/json" \
     -d '{"title": "Brave New World", "author": "Aldous Huxley"}' \
     http://127.0.0.1:5000/books
     
License
This project is licensed under the MIT License.
