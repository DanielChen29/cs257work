from flask import Flask, render_template
import psycopg2
import random

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template("cityhome.html")

@app.route('/cityfact/')
def rand():
    conn = psycopg2.connect(
        host="localhost",
        port=5432,   
        database="chend2",
        user="chend2",
        password="plad242books")

    cur = conn.cursor()

    sql = f"SELECT * FROM Cities ORDER BY RANDOM() LIMIT 1"
    
    cur.execute( sql )

    row = cur.fetchone()

    city = row[0]
    state = row[1]
    pop = row[2]

    sql = f"SELECT Population FROM States WHERE state = '{state}'"
    
    cur.execute( sql )

    row = cur.fetchone()

    prop = round(pop/row[0] * 10, 2)
    
    return render_template("cityfact.html", city = city, state = state, pop = pop, prop = prop)

if __name__ == '__main__':
    my_port = 5202
    app.run(host='0.0.0.0', port = my_port) 
