# import the necessary packages
import flask
import json
import mariadb
# from config_bd import CONFIG


app = flask.Flask(__name__)
app.config["DEBUG"] = True

CONFIG = {
    'host': '172.18.0.3',
    'port': 3306,
    'user': 'root',
    'password': 'rootpassword',
    'database': 'mydatabase'
}

# route to return all people
@app.route('/api/people', methods=['GET'])
def index():
   # connection for MariaDB
   conn = mariadb.connect(**CONFIG)
   # create a connection cursor
   cur = conn.cursor()
   # execute a SQL statement
   cur.execute("select * from people")

   # serialize results into JSON
   row_headers=[x[0] for x in cur.description]
   rv = cur.fetchall()
   json_data=[]
   for result in rv:
        json_data.append(dict(zip(row_headers,result)))

   # return the results!
   return json.dumps(json_data)

app.run()