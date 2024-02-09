from flask import Flask, url_for, redirect

app = Flask(__name__)

@app.route("/")
def index():

    return redirect(url_for('static',filename='index.html'))

@app.route("/test")
def test():
    return "TEST"

@app.route('/user/<name>')
def user(name):
    return f'This is page for {name}'

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return do_the_login()
#     else:
#         return show_the_login_form()

app.run()