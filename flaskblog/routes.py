# ----------------------------------------------------------------------------#
# Imports
# ----------------------------------------------------------------------------#
from flask import render_template, url_for, flash, redirect
from flaskblog.models import User, Post
from flaskblog.forms import PostForm
from flaskblog import app
# Hardcoded posts data
posts = [
    {
        'author': 'Ruchir Sutaria',
        'title': 'Blog Post 1',
        'content': 'first post content',
        'date_posted': 'June 29, 2020'
    },
        {
        'author': 'Ruchir Sutaria',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'June 30, 2020'
    },
]

# ----------------------------------------------------------------------------#
# Flask Controllers.
# ----------------------------------------------------------------------------#

# ----------------------------------------------------------------------------#
#  App route for home page
# ----------------------------------------------------------------------------#
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts)


# ----------------------------------------------------------------------------#
#  App route for about page
# ----------------------------------------------------------------------------#
@app.route("/about")
def about():
    return render_template('about.html', title='About')

# ----------------------------------------------------------------------------#
#  App route for creating a new post
# ----------------------------------------------------------------------------#
@app.route("/post/new", methods=['GET','POST'])
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        flash('Your post has been created!', 'success')
        return redirect(url_for('home'))
    return render_template('create_post.html', title='New Post', form=form)


# ----------------------------------------------------------------------------#
#  App routes for future development
# ----------------------------------------------------------------------------#
@app.route("/login")
def login():
    return render_template('future.html')

@app.route("/register")
def register():
    return render_template('future.html')