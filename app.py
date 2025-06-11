from flask import Flask
from flask_migrate import Migrate
from  models import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school.db'



migrate = Migrate(app, db)
db.init_app(app)

@app.route('/')
def index():
    return "Hello World!"

@app.route('/about')
def about():
    return "This is about us page"

@app.route('/<username>')
def username(username):
    return f'Hello {username}'

if __name__ == '__main__':
    app.run(debug=True, port=4000)
