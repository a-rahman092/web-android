from flask import Flask, render_template, request, flash, redirect
from flask_mail import Mail, Message
import smtplib
 
app = Flask(__name__)

app.secret_key = '12345'

mail= Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'abdulrahman209875@gmail.com'
app.config['MAIL_PASSWORD'] = 'Rahman@123'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/', methods =['GET', 'POST'])

def index():
    return render_template("index.html")

@app.route('/service-worker.js')
def sw():
    return app.send_static_file('service-worker.js')


@app.errorhandler(404)
def invalid_route(e):
   return render_template('404.html')

if __name__ == '__main__':
    app.run()
