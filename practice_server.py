import logging
import os
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import worker  # Import the worker module

# Initialize Flask app and CORS
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.logger.setLevel(logging.ERROR)

# Define the route for the index page
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')  # Render the index.html template


@app.route('/process-document', methods=['POST'])
def process_document_data():
    # TODO: Implement this function
    pass


@app.route('/process-message', methods=['POST'])
def process_prompt_route():
    # TODO: Implement this function
    pass


#if __name__ == "__main__":
app.run(debug=True, port=8000, host='0.0.0.0')