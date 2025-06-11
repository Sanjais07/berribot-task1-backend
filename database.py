import psycopg2

conn = psycopg2.connect(
    dbname="NewDB",
    user="postgres",
    password="sanjai",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()
