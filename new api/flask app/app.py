from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.form['message']
    # Here you would implement your logic to generate a response
    # For now, let's just echo the message back to the user
    response_message = "You said: " + message
    return jsonify({'response': response_message})

if __name__ == '__main__':
    app.run(debug=True)
