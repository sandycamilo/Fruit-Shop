from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import os

# my_app_db

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/fruitshop')
client = MongoClient(host=f'{host}?retryWrites=false')
db = client.get_default_database()
fruits = db.fruits
comments = db.comments

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

app.route('/fruits/thankyou', methods=['POST'])
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

@app.route('/fruits/comments', methods=['POST'])
def comments_new():
    comment = {
        'title': request.form.get('title'),
        'content': request.form.get('content'),
        'fruit_id': ObjectId(request.form.get('fruit_id'))
    }
    print(comment)
    comment_id = comments.insert_one(comment).inserted_id
    return redirect(url_for('fruits_show', fruit_id=request.form.get('fruit_id')))
    return 'Leave a review'

@app.route('/fruits/<fruit_id>')
def fruits_show(fruit_id):
    fruit = fruits.find_one({'_id': ObjectId(fruit_id)})
    fruit_comments = comments.find({'fruit_id': ObjectId(fruit_id)})
    return render_template('fruits_show.html', fruit=fruit, comments=fruit_comments)

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))