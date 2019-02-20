from database import Database, utils, init
from flask import Blueprint, jsonify, request


select = Blueprint("select", __name__)

#this is a query interface that selects one or more rows based on single value
@select.route('/api/select/query', methods = ['POST'])
def db_select():

    data = request.get_json()
    query, parms = utils.json_to_select(data)

    print(query)

    result = utils.select(init.db, query, parms)

    return jsonify({
        'success' : True,
        'result' : result
    })

