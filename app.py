from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm


app = Flask(__name__)


app.config['SECRET_KEY'] = '2de0f2fae3ba5cb551f79fc00862927e'



posts = [
    {
        'author': 'RAyner Rodriguez',
        'title': "Blog post 1",
        'content': 'First post content',
        'date_posted': 'Febrero 23. 2022'
    },
    {
        'author': 'Alexander Valera',
        'title': "Blog post 2",
        'content': 'second post content',
        'date_posted': 'Febrero 24. 2022'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home')) # (name) the functions
    return render_template('register.html', title='Register', form=form)



@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You jave been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)



if __name__ == '__main__':
    app.run(debug=True)