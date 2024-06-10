import psycopg2

conn = psycopg2.connect(database="lesson",
                        user="postgres",
                        password=1234,
                        host="localhost",
                        port=5432)

cursor = conn.cursor()  # creating a cursor

cursor.execute("""SELECT * FROM user_web;""")
for row in cursor.fetchall():
    print(f"{row[0]} # {row[1]} # {row[2]} # {row[3]}")
conn.commit()
conn.close()