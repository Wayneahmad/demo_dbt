import psycopg2


# CREATING A DATABASE CONNECTION

def setup_db_connection():
    return psycopg2.connect(
        host="localhost",
        port=5432,
        user="root",
        password="password")


db = setup_db_connection()
db.set_session(autocommit=True)
cursor = db.cursor()

sql = "CREATE DATABASE dbt IF NOT EXSIST"

cursor.execute(sql)
