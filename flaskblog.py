from flask import Flask, render_template, url_for, flash, redirect
from constants import SecretsManager
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = SecretsManager.SECRET_KEY.value

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
def home():
    return render_template("home.html",posts=posts,title="Flask Blog | Home")

@app.route("/about")
def about():
    return render_template("about.html",title="Flask Blog | About")


@app.route("/register",methods=['GET','POST'])
def register():
    form = RegistrationForm()
    # if form.validate_on_submit():
    #     flash(f'Account created successfully for the user: {form.username.data}',category='success')
    #     return redirect(url_for('home'))
    return render_template("register.html",title="Flask Blog | Register",form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html",title="Flask Blog | Login",form=form)

if __name__ == '__main__':
    app.run(debug=True)
