from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
# flask db migrate -m "create  users tabble"
# create tabe = flask db upgrade head
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    middle_name = db.Column(db.String)
    last_name = db.Column(db.String)
    username = db.Column(db.String)

class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    post_title = db.Column(db.String, nullable=False)
    post_content = db.Column(db.String)

    def __repr__(self):
        return f"<Post {self.id}: {self.post_title}>"
