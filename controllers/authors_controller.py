from flask import Flask, render_template, redirect, request
from flask import Blueprint

from models.book import Book
from models.author import Author
import repositories.book_repository as book_repository  # why do we give them this alias?
import repositories.author_repository as author_repository

authors_blueprint = Blueprint("authors", __name__)

# New author route:
@authors_blueprint.route("/authors/new")
def new_author():
    return render_template("authors/new.html")

# Add an author:
@authors_blueprint.route("/authors", methods = ['POST'])
def create_author():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    new_author = Author(first_name, last_name)
    author_repository.save(new_author)
    
    return redirect("/books/new")