from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Tomko'}
    posts = [
        {
            'author': {'username': 'Dezider'},
            'body': 'Skuska'
        },
        {
            'author': {'username': 'Jolanda'},
            'body': 'Dalsia skuska'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)