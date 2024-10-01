from flask import Flask, jsonify, request, render_template
import json
import os

app = Flask(__name__)
data_file = 'books.json'

# Load existing books from the JSON file
def load_books():
    if os.path.exists(data_file):
        with open(data_file, 'r') as f:
            return json.load(f)
    return []

# Save books to the JSON file
def save_books(books):
    with open(data_file, 'w') as f:
        json.dump(books, f, indent=4)

# Load books when the app starts
books = load_books()

@app.route('/')
def index():
    return render_template('index.html')

# API routes
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.get_json()
    new_book['id'] = len(books) + 1
    books.append(new_book)
    save_books(books)  # Save to JSON file
    return jsonify(new_book), 201

if __name__ == '__main__':
    app.run(debug=True)

