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

@select.route('/api/select/supply_lines', methods = ['POST'])
def select_supply_lines() :

    location_id = request.get_json()['location_id']
    query = "select * from SUPPLY_LINES where location_id =:location_id"

    result = utils.select(init.db, query, parms = {'location_id' : location_id})

    return jsonify({
        "success" : True, 
        "result" : result
    })

@select.route('/api/select/farmers', methods = ['POST'])
def select_farmers() :

    line_id = request.get_json()['line_id']
    query = "select * from FARMER where line_id=:line_id"

    result = utils.select(init.db, query, parms = {'line_id' : line_id})

    return jsonify({
        "success" : True,
        "result" : result
    })

@select.route('/api/select/farmers_loc_id', methods = ['POST'])
def select_farmers_id() :

    location_id = request.get_json()['location_id']

    query = "select * from FARMER f, SUPPLY_LINES s where f.line_id = s.line_id and s.location_id=:location_id"

    result = utils.select(init.db, query, parms = {"location_id" : location_id})

    return jsonify({
        "success" : True,
        "result" : result
    })