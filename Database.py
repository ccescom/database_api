import sqlite3
import json

class Database :

    def __init__(self, db_fname = 'default.db'):

        self.db_name = db_fname
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

    def create_tables(self) :

        #I have specified all create statements inside tables.json
        statements = json.load(open('tables.json'))['statements']

        for statement in statements :
            self.cursor.execute(statement)
        
        self.connection.commit()
    
    def test_tables(self):

        result = self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

        tables = result.fetchall()

        for table in tables :
            table = table[0]
            print("TABLE : "+table)
            print([desc[0] for desc in self.connection.execute("select * from "+table).description])
    
    def dummy_insert(self):

        pass 


db = Database()

db.test_tables()
