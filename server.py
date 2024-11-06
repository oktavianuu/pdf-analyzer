import worker
from flask import Flask

app = Flask(__name__) # initializes flask app

@app.route('/', methods=['GET']) # creates routes for the homepage (root URL)
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True) # Starts the app in debug mode, providing helpful error messages and auto-restarting on changes.

