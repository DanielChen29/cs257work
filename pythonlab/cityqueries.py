import psycopg2

def queries():

    # You will need to change the Port and the Password to use this code
    
    conn = psycopg2.connect(
        host="localhost",
        port=5432,   
        database="chend2",
        user="chend2",
        password="plad242books")

    cur = conn.cursor()

    sql = "SELECT Latitude, Longitude FROM Cities WHERE City = 'Northfield'"
    
    cur.execute( sql )

    # fetchone() returns one row that matches your quer
    row = cur.fetchone()

    if row:
        print(f"Coordinates of Northfield are: Latitude {row[0]}, Longitude {row[1]}")
    else:
        print("Error: Northfield not found in the database.")

    conn.commit()

if __name__ == '__main__':
    queries()