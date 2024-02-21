from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['SECRET_KEY'] = 'qpgx glzv krlg fuzc'  # Replace with your secret key

# Configure mail settings
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'jskassociates92@gmail.com'
app.config['MAIL_PASSWORD'] = 'xmhf eevr utfm xcuv'
app.config['MAIL_DEFAULT_SENDER'] = 'jskassociates92@gmail.com'

mail = Mail(app)

@app.route('/')
def contact():
    return render_template('contact.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone_no']
        email = request.form['email']
        message = request.form['message']

        msg = Message('New Contact Form Submission',
                      sender='jskassociates92@gmail.com',
                      recipients=['jskassociates92@gmail.com'])  # Replace with your recipient email

        msg.body = f"Name: {name}\nPhone: {phone}\nEmail: {email}\nMessage: {message}"

        try:
            mail.send(msg)
            flash('Message sent successfully!', 'success')
        except Exception as e:
            print(str(e))
            flash('An error occurred. Please try again later.', 'error')

        return redirect(url_for('contact'))  # Redirect to the contact form page
    else:
        return redirect(url_for('contact'))

if __name__ == '__main__':
    app.run(debug=True)
