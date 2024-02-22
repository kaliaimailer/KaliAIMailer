# pip install Flask Flask-Mail

from flask import Flask, request, render_template_string
from flask_mail import Mail, Message

app = Flask(__name__)

# Configuring Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Use your SMTP server details
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'your-email@example.com'  # Your email
app.config['MAIL_PASSWORD'] = 'your-password'  # Your email account password
app.config['MAIL_DEFAULT_SENDER'] = 'your-email@example.com'  # Default sender

mail = Mail(app)

@app.route('/send_email', methods=['GET', 'POST'])
def send_email():
    if request.method == 'POST':
        subject = request.form.get('subject')
        recipient = request.form.get('recipient')
        message = request.form.get('message')
        
        msg = Message(subject, recipients=[recipient])
        msg.body = message
        
        try:
            mail.send(msg)
            return 'Email sent successfully!'
        except Exception as e:
            return str(e)
    else:
        # A simple form for testing email sending
        return render_template_string('''
            <form method="post">
                Subject: <input type="text" name="subject"><br>
                Recipient: <input type="email" name="recipient"><br>
                Message: <textarea name="message"></textarea><br>
                <input type="submit">
            </form>
        ''')

if __name__ == '__main__':
    app.run(debug=True)
