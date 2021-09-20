import mysql.connector
import json
from flask import Flask, render_template, request
from simple_text import to_upper



app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
  variavel = "SMF"
  if request.method == "GET":
    return render_template("index.html", variavel=variavel)
  else:

    palpite = request.form.get("name")
    novo_texto = to_upper(palpite)
    inse(novo_texto)
    return novo_texto

@app.route('/widgets')
def get_widgets() :
  mydb = mysql.connector.connect(
    host="mysqldb",
    user="root",
    password="p@ssw0rd1",
    database="inventory"
  )
  cursor = mydb.cursor()


  cursor.execute("SELECT * FROM widgets")

  row_headers=[x[0] for x in cursor.description] #this will extract row headers

  results = cursor.fetchall()
  json_data=[]
  for result in results:
    json_data.append(dict(zip(row_headers,result)))

  cursor.close()

  return json.dumps(json_data)

@app.before_first_request
def db_init():
  mydb = mysql.connector.connect(
    host="mysqldb",
    user="root",
    password="p@ssw0rd1"
  )
  cursor = mydb.cursor()

  cursor.execute("DROP DATABASE IF EXISTS inventory")
  cursor.execute("CREATE DATABASE inventory")
  cursor.close()

  mydb = mysql.connector.connect(
    host="mysqldb",
    user="root",
    password="p@ssw0rd1",
    database="inventory"
  )
  cursor = mydb.cursor()

  cursor.execute("DROP TABLE IF EXISTS widgets")
  cursor.execute("CREATE TABLE widgets (name VARCHAR(255), description VARCHAR(255))")
  cursor.close()

#@app.route('/initdb')
#def db_init():
#  mydb = mysql.connector.connect(
#    host="mysqldb",
#    user="root",
#    password="p@ssw0rd1"
#  )
#  cursor = mydb.cursor()
#
#  cursor.execute("DROP DATABASE IF EXISTS inventory")
#  cursor.execute("CREATE DATABASE inventory")
#  cursor.close()
#
#  mydb = mysql.connector.connect(
#    host="mysqldb",
#    user="root",
#    password="p@ssw0rd1",
#    database="inventory"
#  )
#  cursor = mydb.cursor()

#  cursor.execute("DROP TABLE IF EXISTS widgets")
#  cursor.execute("CREATE TABLE widgets (name VARCHAR(255), description VARCHAR(255))")
#  cursor.close()

#  return 'init database'

#@app.route('/fw') # Como que eu chamo as funções que estão em outro lugar?
#def pega_valor():
#  fancywallet get price


def inse(valor):
  mydb = mysql.connector.connect(
    host="mysqldb",
    user="root",
    password="p@ssw0rd1",
    database="inventory"
  )
  cursor = mydb.cursor()
  sql = "INSERT INTO widgets (name , description) VALUES (%s, %s)"
  val = (valor , '1')
  cursor.execute(sql,val)
  mydb.commit()
  cursor.close()


if __name__ == "__main__":
  app.run(host ='0.0.0.0')