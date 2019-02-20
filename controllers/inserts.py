from flask import Flask, Blueprint, jsonify, request
from database import init, utils

insert = Blueprint("insert", __name__)

@insert.route('/api/insert', methods = ['POST'])
def api_insert() :

    data = request.get_json()

    query, pk = utils.json_to_insert(data)

    utils.insert(init.db, query)

    return jsonify({
        "success" : True,
        "insert_id" : str(insert_id),
        "primary_key" : pk
    }) 
