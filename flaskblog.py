from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author': 'Arun S',
        'title': 'Blog Post 1',
        'content': "First post",
        'date_posted': 'January 09, 2022'
    },
    {
        'author': 'Renu A',
        'title': 'Blog Post 2',
        'content': "Second post",
        'date_posted': 'January 10, 2022'
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
