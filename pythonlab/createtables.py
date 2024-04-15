import psycopg2

def create_tables():
    """ Create tables in the PostgreSQL database"""
    commands = (
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
        CREATE TABLE States (
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

if __name__ == '__main__':
    create_tables()