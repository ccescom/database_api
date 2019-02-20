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

#test_insert()
test_select()