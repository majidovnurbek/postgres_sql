import psycopg2

from colorama import Fore

def create_connection():
    try:
        conn= psycopg2.connect(database="lesson", user="postgres", password="1234", host="localhost", port="5432")
        cursor = conn.cursor()
        print(Fore.LIGHTYELLOW_EX + "database connect successful")
        cursor.execute("""CREATE TABLE IF NOT EXISTS admin(
        id SERIAL PRIMARY KEY,
        name varchar(50),
        username varchar(50) not null unique)""")
        conn.commit()
        print(Fore.LIGHTGREEN_EX + "Table created successfully")
    except psycopg2.DatabaseError as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == "__main__":
    create_connection()
