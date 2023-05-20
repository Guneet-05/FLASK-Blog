from flask import Flask, render_template, url_for
app = Flask(__name__)


posts = [
    {
        'author': 'Guneet Malhotra',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'May 20, 2023'
    },
    {
        'author': 'Rahul Maurya',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'May 20, 2023'
    }
]

@app.route("/")
@app.route("/home")
def hello_world():
    return render_template("home.html",posts=posts,title="Flask Blog | Home")

@app.route("/about")
def about():
    return render_template("about.html",title="Flask Blog | About")

if __name__ == '__main__':
    app.run(debug=True)