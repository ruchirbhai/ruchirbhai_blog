from flask import Flask, render_template

app = Flask(__name__)


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
@app.route("/")
def hello():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == "__main__":
    app.run(debug=True)