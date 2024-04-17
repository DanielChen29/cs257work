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

    conn.commit()

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

    conn.commit()

if __name__ == '__main__':
    northfield()
    max_pop()