import requests
import json

query = open('sample_query.json', 'r').read()
data = json.loads(query)

def test_insert() :

    resp = requests.post('http://localhost:5000/api/insert', json = data)

    print(resp.text)

def test_select() :

    resp = requests.post('http://localhost:5000/api/select/query', json = json.load(open('sample_select.json')))

    print(resp.text)

def test_insert_supply_line() :
    resp = requests.post('http://localhost:5000/api/insert', json = json.load(open('insert_line.json')))

    print(resp.text)

def test_insert_farmer() :

    resp = requests.post('http://localhost:5000/api/insert', json = json.load(open('insert_farmer.json')))

    print(resp.text)

LOC = "09846ad4-34d7-1098"

def select_line_from_location() :

    resp = requests.post('http://localhost:5000/api/select/supply_lines', json = {
        "location_id" :  "cdc1bc86-34d1-1cdc"
    })

    print(resp.text)

def select_farmer_from_line() :

    resp = requests.post('http://localhost:5000/api/select/farmers', json = {
        "line_id" : "3f7bead2-34d6-137"
    }) 

    print(resp.text)



#test_insert_supply_line()
test_insert_farmer()