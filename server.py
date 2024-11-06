import logging
import os
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import worker # worker module

app = Flask(__name__) # initializes flask app
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.logger.setLevel(logging.ERROR)


@app.route('/', methods=['GET']) # creates routes for the homepage (root URL)
def index():
    return render_template('index.html')

# routes for processing messages 
@app.route('/process-message', methods=['POST'])
def process_message_route():
    user_message = request.json['userMessage'] # Extract the user's message from the request
    print('user message:', user_message)

    bot_response = worker.process_prompt(user_message) # Process the user's message using the worker module

    # return the bot response as json
    return jsonify({
        "botResponse": bot_response
    }), 200

# routes for processing doc
@app.route('/process-document', method=['POST'])
def process_doc_route():
    # check if the file was uploaded 
    if 'file' not in request.file:
        return jsonify({
            'botResponse': "The file was not uploaded, try again. If the problem persists, try with different file."
        }), 400
    file = request.files['file'] # Extract the uploaded file from the request

    file_path = file.filename # Define the path where the file will be saved
    file.save(file_path) # save file

    # process the doc using the worker module 
    worker.process_document(file_path)

    # Return success message with json
    return jsonify({
        "botResponse": "The file has been analyzed. Ask any questions regarding it!"
    }), 200

if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0') # Starts the app in debug mode, providing helpful error messages and auto-restarting on changes.

