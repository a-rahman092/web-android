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
    msg = ''
    if request.method == 'POST' and 'name' in request.form and 'email' in request.form and 'description' in request.form :
        name = request.form['name']
        email = request.form['email']
        description = request.form['description']
        try:
            mailmsg = Message('WebAndroid Form Submission', sender = 'abdulrahman209875@gmail.com', recipients = ['abdulrahman92mohd@gmail.com'])
            mailmsg.body = "Hello, \nName: {}\nEmail: {} \nDescription: {}".format(name, email, description)
            mail.send(mailmsg)
            flash("Your Request Successfully Sent")
            return redirect("/")
        except:
            msg = "Oops! Something went wrong."
            return redirect("/")
    return render_template("index.html", msg=msg)

@app.route('/service-worker.js')
def sw():
    return app.send_static_file('service-worker.js')


@app.errorhandler(404)
def invalid_route(e):
   return render_template('404.html')

if __name__ == '__main__':
    app.run()