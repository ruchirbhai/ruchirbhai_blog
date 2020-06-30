from flaskblog import db
from datetime import datetime

# ----------------------------------------------------------------------------#
# User table Model
# ----------------------------------------------------------------------------#
class User(db.Model):
    # __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), unique=True, nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"

# ----------------------------------------------------------------------------#
# Post table Model
# ----------------------------------------------------------------------------#
class Post(db.Model):
    # __tablename__ = 'Post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, default=1) # this default needs to change once you have user accounts and login created

    def __repr__(self):
        return f"Post('{self.title}','{self.date_posted}')"