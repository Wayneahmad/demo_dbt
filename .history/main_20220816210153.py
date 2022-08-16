import psycopg2


# CREATING A DATABASE CONNECTION

def setup_db_connection():
    return psycopg2.connect(
        host="localhost",
        port=5439,
        user="root",
        password="password")


db = setup_db_connection()
db.set_session(autocommit=True)
cursor = db.cursor()
