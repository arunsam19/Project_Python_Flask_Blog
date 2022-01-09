from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')
    
@app.route("/about")
def about():
    return "<h1>About Page</h1>"
   

if __name__ == '__main__':
    #app.run(host='127.0.0.1', port=5001,debug=True)
    app.run(debug=True)
