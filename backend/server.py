from flask import Flask, request, jsonify
from connection import get_sql_conn
import mysql.connector
import json


import products_dao
import orders_dao
import uom_dao

app = Flask(__name__)

connection = get_sql_conn()

@app.route('/get_uom', methods=['GET'])
def get_uom():
    response = uom_dao.get_uom(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/get_products', methods=['GET'])
def get_products():
    response = products_dao.get_all_products(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/insert_product', methods=['POST'])
def insert_product():
    request_payload = json.loads(request.form['data'])
    product_id = products_dao.insert_new_product(connection, request_payload)
    response = jsonify({
        'product_id': product_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/get_all_orders', methods=['GET'])
def get_all_orders():
    response = orders_dao.get_order(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/insert_order', methods=['POST'])
def insert_order():
    request_payload = json.loads(request.form['data'])
    order_id = orders_dao.insert_order(connection, request_payload)
    response = jsonify({
        'o_id': order_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/delete_product', methods=['POST'])
def delete_product():
    return_id = products_dao.delete_product(connection, request.form['p_id'])
    response = jsonify({
        'p_id': return_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Grocery Store Management System")
    app.config['DEBUG']=True
    app.run()

