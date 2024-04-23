import psycopg2

def create_tables():
    """ Create tables in the PostgreSQL database"""
    commands = (
        """
        DROP TABLE IF EXISTS cities
        """,
        """
        DROP TABLE IF EXISTS states
        """,
        """
        CREATE TABLE cities (
            City text,
            State text,
            Population real,
            Latitude real,
            Longitude real
        )
        """,
        """ 
        CREATE TABLE states (
                Code text,
                State text,
                Population real
        )
        """)

    conn = psycopg2.connect(
        host="localhost",
        port=5432,   
        database="chend2",
        user="chend2",
        password="plad242books")

    cur = conn.cursor()

    for command in commands:
        cur.execute(command)

    conn.commit()

if __name__ == '__main__':
    create_tables()