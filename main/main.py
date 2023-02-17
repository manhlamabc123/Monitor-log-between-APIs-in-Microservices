from flask import Flask, jsonify, abort, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint
from dataclasses import dataclass
import requests
import json
import time
from producer import publish, publish_log

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:20194616@database/main'
CORS(app)

db = SQLAlchemy(app)

correlation_id = ''


@app.before_request
def before_request():
    global correlation_id
    correlation_id = request.headers.get('X-My-Correlation-Id')
    headers = dict(request.headers)
    if correlation_id is None:
        correlation_id = "main-" + str(int(time.time()))
    body = bytes(request.data).replace(b"'", b'"')
    if body.decode('utf-8') == '':
        body = '{}'
    req = {
        'header': headers,
        'body': json.loads(body),
        'path': request.path,
        'method': request.method,
        'correlation_id': correlation_id,
    }
    publish_log('product_liked', req)


@dataclass
class Product(db.Model):
    id: int
    title: str
    image: str

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(256))
    image = db.Column(db.String(256))


@dataclass
class ProductUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)

    UniqueConstraint('user_id', 'product_id', name='user_product_unique')


@app.route('/api/products')
def index():
    return jsonify(Product.query.all())


@app.route('/api/products/<int:id>/like', methods=['POST'])
def like(id):
    req = requests.get(
        'http://172.17.0.1:8000/api/user',
        headers={
            'X-My-Correlation-Id': correlation_id
        }
    )
    json = req.json()
    try:
        productUser = ProductUser(user_id=json['id'], product_id=id)
        db.session.add(productUser)
        db.session.commit()

        publish('product_liked', id)

    except:
        abort(400, 'You already liked this product')

    return jsonify({
        "message": "success"
    })


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
