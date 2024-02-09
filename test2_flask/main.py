from flask import (Flask, redirect, url_for, render_template)


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',title = 'Main Page')

@app.route('/about')
def about():
    return render_template('about.html', title='About')
@app.route('/contact')
def contact():
    return render_template('contact.html', title='contact')
    

if __name__ == '__main__':
    app.run(debug=True)