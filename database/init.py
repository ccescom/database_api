from . import Database

def init_db() :
    global db 
    db = Database.Database()
