from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Tomko'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Skuska'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'Dalsia Skuska'
        }
    ]
    return render_template('index.html', title='Home', user=user)