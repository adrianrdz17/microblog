from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {
        'username': 'Miguel'
    }
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beatiful day in Portland'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'Joker 2 is amazing'
        },
    ]

    # Asi es como se hace referencia a una plantilla
    # ademas se envian las variables indicadas dentro de ella, aqui mismo.
    return render_template('index.html', title='Home', user=user, posts=posts)