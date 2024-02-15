import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    # Check if a file is in the request
    if 'file' not in request.files:
        # No file part
        return redirect(request.url)
    file = request.files['file']
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == '':
        return redirect(request.url)
    if file:
        # Save the file
        filename = secure_filename(file.filename)
        file.save(os.path.join('path_to_save', filename))
        # You can process the file here or redirect to another route
        return redirect(url_for('index'))

@app.route('/message', methods=['POST'])
def message():
    # Handle chat message
    message = request.form['message']
    # Process or save message
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
