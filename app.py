from flask import Flask 

app = Flask(__name__)

@app.route('/')
def index():
    """Homepage"""
    return render_template('home.html', msg= "Hi, welcome to the Fruit Shop!")

if __name__ == '__main__':
    app.run(debug=True)