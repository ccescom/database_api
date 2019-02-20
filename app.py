from database import init, Database, utils
from flask import Flask
from controllers import inserts, selects

init.init_db()
utils.generate_schema(init.db)


app = Flask(__name__)

app.register_blueprint(inserts.insert)
app.register_blueprint(selects.select)

app.run()



