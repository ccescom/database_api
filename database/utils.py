import json
from . import init
import uuid

def generate_schema(db) :

    global schema
    
    result = db.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

    tables = result.fetchall()

    schema = {}

    for table in tables :
        schema[table[0]] = [desc[0] for desc in db.connection.execute("select * from "+table[0]).description]


def generate_primary_key(col_name):

    return (col_name, str(uuid.uuid1())[0:10] + str(uuid.uuid1())[10:15]+ str(uuid.uuid1())[0:3])

    
def json_to_insert(json_data):

    #early return if no TABLE is not in schema
    if json_data['TABLE'] not in schema.keys() :
        return None
    
    #convert json_data to SQL insert statement : 

    #process primary keys:
    pk = None
    if 'PRIMARY_KEY' in json_data.keys() :
        col, pk = generate_primary_key(json_data['PRIMARY_KEY'])
        json_data['data'][col] = pk

    
    print(json_data['data'])

    query = "insert into "+json_data['TABLE'] + '' + str(tuple(json_data['data'].keys()))+' values'

    values = ()
    for key in json_data['data'].keys() :

        if key not in schema[json_data['TABLE']] :
            return None
        values = values + (json_data['data'][key],)

    query += str(values)

    return (query , pk)


def json_to_select(json_data):

    if json_data['TABLE'] not in schema.keys() :
        return None
    
    query = "select "

    for col in json_data['COLS'] :

        query = query + col +" "
    
    query = query + "from "+ json_data['TABLE']

    if "FILTERS" in json_data.keys() :

        query = query + " where "

        for k, v in json_data['FILTERS'].items() :

            query = query +""+k+"=:"+k + " and "

        query = query[:-4]

    return (query , json_data['FILTERS'])



def insert(db, sql) :
    result = db.cursor.execute(sql)
    db.connection.commit()

def select(db,sql, parms) :
    
    result = db.cursor.execute(sql, parms)
    res = []
    for row in result : 
        d = {}
        for idx, col in enumerate(db.cursor.description):
           d[col[0]] = row[idx]  
        res.append(d)
    
    return res
    



    

