from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import os

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/fruitshop')
client = MongoClient(host=f'{host}?retryWrites=false')
db = client.get_default_database()
fruits_collection = db.fruits


app = Flask(__name__)


@app.route('/')
def fruits_index ():
    """Homepage"""
    return render_template('fruits_index.html', fruits = fruits_collection.find())

@app.route('/fruits/selectfruit')
def fruits_selectfruit():
    """Selection of fruits."""
    return render_template('fruits_selectfruit.html', title="Fruit")

@app.route('/fruits', methods=['POST'])
def fruits_submitbasket():
    """Select fruit and submit to basket."""
    fruits = {
        'title': request.form.get('title'),
        'description': request.form.get('description')
    }
    fruits = fruits_collection.insert_one(fruits)
    return redirect(url_for('fruits_tobasket'))

@app.route('/fruits/tobasket')
def fruits_tobasket():
    """Shows everything listed in fruit basket."""
    return render_template('fruits_tobasket.html')

app.route('/fruits', methods=['POST'])
def fruits_submitcheckout():
    """Fruit basket with items to checkout."""
    fruits = {
        'title': request.form.get('title'),
        'description': request.form.get('description')
    }
    fruits = fruits_collection.insert_one(fruits)
    return redirect(url_for('fruits_checkout'))

@app.route('/fruits/checkout')
def fruits_checkout():
    """Input payment information."""
    return render_template('fruits_checkout.html')

app.route('/fruits/thankyou', methods=['POST'])
def fruits_submitthankyou():
    """Submit payment information."""
    fruits = {
        'title': request.form.get('title'),
        'description': request.form.get('description')
    }
    fruits = fruits_collection.insert_one(fruits)
    return redirect(url_for('fruits_thankyou'))

@app.route('/fruits/thankyou')
def fruits_thankyou():
    """Thank you."""
    return render_template('fruits_thankyou.html')


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))