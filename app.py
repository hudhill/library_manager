from flask import Flask, render_template

from controllers.books_controller import books_blueprint
from controllers.authors_controller import authors_blueprint

app = Flask(__name__)

app.register_blueprint(books_blueprint)
app.register_blueprint(authors_blueprint)

# Home page:
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True)