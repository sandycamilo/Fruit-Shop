from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

client = MongoClient()
db = client.TheFruitShop
fruits = db.fruits

app = Flask(__name__)


@app.route('/')
def fruits_index ():
    return render_template('fruits_index.html', fruits = fruits.find())

@app.route('/fruits/selectfruit')
def fruits_selectfruit():
    return render_template('fruits_selectfruit.html')

@app.route('/fruits', methods=['GET'])
def fruits_submit():
    print(request.form.to_dict())
    return redirect(url_for('fruits_index'))


if __name__ == '__main__':
    app.run(debug=True)