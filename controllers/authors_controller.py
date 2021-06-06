from flask import Flask, render_template, redirect, request
from flask import Blueprint

from models.book import Book
from models.author import Author
import repositories.book_repository as book_repository  # why do we give them this alias?
import repositories.author_repository as author_repository

authors_blueprint = Blueprint("authors", __name__)

# List all authors:
@authors_blueprint.route("/authors")
def authors():
    authors = author_repository.select_all()
    return render_template("authors/index.html", authors = authors)

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
    
    return redirect("/authors")


# New author option for new book:
@authors_blueprint.route("/authors/new_option")
def new_author_option():
    return render_template("authors/new_option.html")
# Return to new book form:
@authors_blueprint.route("/authors/option", methods = ['POST'])
def create_new_option():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    new_author = Author(first_name, last_name)
    author_repository.save(new_author)

    return redirect("/books/new")


# Show single author:
@authors_blueprint.route("/authors/<id>")
def show_author(id):
    author = author_repository.select(id)
    return render_template("authors/show.html", author = author)

# Edit an author:
@authors_blueprint.route("/authors/<id>/edit")
def edit_author(id):
    author = author_repository.select(id)
    return render_template("authors/edit.html", author = author)

# Update an author:
@authors_blueprint.route("/authors/<id>", methods = ["POST"])
def update_author(id):
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    updated_author = Author(first_name, last_name, id)
    author_repository.update(updated_author)
    return redirect("/authors")

# Delete an author:
@authors_blueprint.route("/authors/<id>/delete", methods = ['POST'])
def delete_author(id):
    author_repository.delete(id)
    return redirect("/authors")