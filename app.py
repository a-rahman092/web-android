from flask import Flask, render_template, request, flash, redirect

 
app = Flask(__name__)

app.secret_key = '12345'

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
