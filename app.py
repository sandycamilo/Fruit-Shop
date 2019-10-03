from flask import Flask, render_template
from pymongo import MongoClient

client = MongoClient()
db = client.FruitShop
fruits = db.fruits

app = Flask(__name__)


@app.route('/')
def fruits_index ():
    return render_template('fruits_index.html', fruits = fruits.find())

if __name__ == '__main__':
    app.run(debug=True)