from flask import request, Response, jsonify

from app import app
from app.controllers import Shopify, Woocommerce
from mock_data.db import db

@app.route('/')
def home():
    return Response('Welcome, to test the api use "/stores/{store_id}/products". Currently only store ID 1 or 2 can be used(mock data)')

@app.route('/stores/<int:storeID>/products', methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def products(storeID):
    if request.method == 'GET':
        platform = db.get(storeID)
        products = None
        if platform == 'shopify':
            shopify = Shopify()
            products = shopify.get_products()
        elif platform == 'woocommerce':
            woo = Woocommerce()
            products = woo.get_products()
        return jsonify({'success': True, 'data': products})
        # return Response('True', status=200)
    elif request.method == 'POST':
        # Logic for creating a new product in the db
        pass
    elif request.method == 'PUT':
        # Logic for updating an entire product in the db
        pass
    elif request.method == 'PATCH':
        # Logic for updating a property of a product in the db
        pass
    elif request.method == 'DELETE':
        # Logic for removing a product from the db
        pass
    else:
        response = jsonify(success=False)
        return Response(response, status=500)