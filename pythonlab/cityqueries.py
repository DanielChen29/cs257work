from cgitb import small
import psycopg2

def northfield():
    conn = psycopg2.connect(
        host="localhost",
        port=5432,   
        database="chend2",
        user="chend2",
        password="plad242books")

    cur = conn.cursor()

    sql = "SELECT Latitude, Longitude FROM Cities WHERE City = 'Northfield'"
    
    cur.execute( sql )

    row = cur.fetchone()

    if row:
        print(f"Coordinates of Northfield are: Latitude {row[0]}, Longitude {row[1]}")
    else:
        print("Error: Northfield not found in the database.")

def max_pop():
    conn = psycopg2.connect(
        host="localhost",
        port=5432,   
        database="chend2",
        user="chend2",
        password="plad242books")

    cur = conn.cursor()

    sql = "SELECT City FROM Cities ORDER BY Population DESC LIMIT 1"
    
    cur.execute( sql )

    row = cur.fetchone()

    print(f"{row[0]} has the largest population in the US")

def smallest_in_MN():
    conn = psycopg2.connect(
        host="localhost",
        port=5432,   
        database="chend2",
        user="chend2",
        password="plad242books")

    cur = conn.cursor()

    sql = "SELECT City FROM Cities WHERE State = 'Minnesota' ORDER BY Population LIMIT 1"
    
    cur.execute( sql )

    row = cur.fetchone()

    print(f"{row[0]} has the smallest population in MN")

def furthest_cardinal():
    conn = psycopg2.connect(
        host="localhost",
        port=5432,   
        database="chend2",
        user="chend2",
        password="plad242books")

    cur = conn.cursor()

    commands = ["SELECT City FROM Cities ORDER BY Latitude LIMIT 1",
                "SELECT City FROM Cities ORDER BY Latitude DESC LIMIT 1",
                "SELECT City FROM Cities ORDER BY Longitude LIMIT 1",
                "SELECT City FROM Cities ORDER BY Longitude DESC LIMIT 1"]
    
    row = []

    for sql in commands:
        cur.execute( sql )
        row.append(cur.fetchone()[0])

    print(f"{row[0]} is the farthest city West in the US")
    print(f"{row[1]} is the farthest city East in the US")
    print(f"{row[2]} is the farthest city South in the US")
    print(f"{row[3]} is the farthest city North in the US")

def user_search():
    state = input("Enter state:")

    conn = psycopg2.connect(
        host="localhost",
        port=5432,   
        database="chend2",
        user="chend2",
        password="plad242books")

    cur = conn.cursor()

    if len(state) == 2:
        sql = f"SELECT State FROM States WHERE Code = '{state}'"

        cur.execute( sql )

        row = cur.fetchone()

        state = row[0]

    sql = f"SELECT Population FROM Cities WHERE Name = '{state}'"

    cur.execute( sql )

    rows = cur.fetchall()

    pop = 0
    for r in rows:
        pop += r[0]

    print(f"the largest cities in {state} have a combined population of {pop}")

if __name__ == '__main__':
    northfield()
    max_pop()
    smallest_in_MN()
    furthest_cardinal()
    user_search()