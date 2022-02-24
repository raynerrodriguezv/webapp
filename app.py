from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author': 'RAyner Rodriguez',
        'title': "Blog post 1",
        'content': 'First post content',
        'date_posted': 'Febrero 23. 2022'
    },
    {
        'author': 'ALEXANDER Valera',
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

if __name__ == '__main__':
    app.run(debug=True)