from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import os


host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/fruitshop')
client = MongoClient(host=f'{host}?retryWrites=false')
db = client.FruitShop
fruits = db.fruits

app = Flask(__name__)


@app.route('/')
def fruits_index ():
    return render_template('fruits_index.html', fruits = fruits.find())

@app.route('/fruits/selectfruit')
def fruits_selectfruit():
    return render_template('fruits_selectfruit.html')

@app.route('/fruits', methods=['POST'])
def fruits_submit():
    fruits = {
        'title': request.form.get('title'),
        'description': request.form.get('description')
    }
    fruits.insert_one(fruits)
    return redirect(url_for('fruits_tobasket'))

@app.route('/fruits/tobasket')
def fruits_tobasket():
    return render_template('fruits_tobasket.html')

app.route('/fruits', methods=['POST'])
def fruits_submit():
    fruits = {
        'title': request.form.get('title'),
        'description': request.form.get('description')
    }
    fruits.insert_one(fruits)
    return redirect(url_for('fruits_checkout'))

@app.route('/fruits/checkout')
def fruits_checkout():
    return render_template('fruits_checkout.html')

app.route('/fruits', methods=['POST'])
def fruits_submit():
    fruits = {
        'title': request.form.get('title'),
        'description': request.form.get('description')
    }
    fruits.insert_one(fruits)
    return redirect(url_for('fruits_thankyou'))

@app.route('/fruits/thankyou')
def fruits_thankyou():
    return render_template('fruits_thankyou.html')


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))