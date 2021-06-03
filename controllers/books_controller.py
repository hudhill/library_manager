from flask import Flask, render_template, redirect, request
from flask import Blueprint

from models.book import Book
from models.author import Author
import repositories.book_repository as book_repository  # why do we give them this alias?
import repositories.author_repository as author_repository

books_blueprint = Blueprint("books", __name__)

# List all books:
@books_blueprint.route("/books")
def books():
    books = book_repository.select_all()
    return render_template("books/index.html", books = books)

# New book route:
@books_blueprint.route("/books/new")
def new_book():
    authors = author_repository.select_all()
    return render_template("books/new.html", authors = authors)

# Add a book:
@books_blueprint.route("/books", methods = ['POST'])
def create_book():
    title = request.form["title"]
    author_id = request.form["author_id"]
    year = request.form["year"]
    author = author_repository.select(author_id)
    new_book = Book(title, author, year)
    book_repository.save(new_book)
    
    return redirect("/books")

# Show single book:
@books_blueprint.route("/books/<id>")
def show_book(id):
    book = book_repository.select(id)
    return render_template("books/show.html", book = book)

# Edit a book:
@books_blueprint.route("/books/<id>/edit")
def edit_book(id):
    book = book_repository.select(id)
    authors = author_repository.select_all()
    return render_template("books/edit.html", book = book, authors = authors)

# Update a book:
@books_blueprint.route("/books/<id>", methods = ["POST"])
def update_book(id):
    title = request.form["title"]
    author_id = request.form['author_id']
    year = request.form['year']
    author = author_repository.select(author_id)
    updated_book = Book(title, author, year, id)
    book_repository.update(updated_book)
    return redirect("/books")

# Delete a book:
@books_blueprint.route("/books/<id>/delete", methods = ['POST'])
def delete_book(id):
    book_repository.delete(id)
    return redirect("/books")