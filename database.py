import mysql.connector
import db_credentials as cred

def mysql_connect():
    try:
        conn = mysql.connector.connect(
            host = cred.MYSQL_HOST,
            user = cred.MYSQL_USER,
            password = cred.MYSQL_PASSWORD
        )
        return conn
    except:
        return None

def mysql_disconnect(database):
    if database:
        database.close()
    else:
        print("No Database to disconnect!")

def setup_cursor(conn):
    try:
        mycursor = conn.cursor()
        return mycursor
    except:
        print("An unexpected occured!")

def database_connect(mycursor, dbname: str = "pythonDB"): # Setting "pythonDB" as default database for python mysql database usage.
    try:
        mycursor.execute(f"CREATE DATABASE IF NOT EXISTS `{dbname}`")
        return dbname
    except:
        print("An unexpected occured!")
        return None

if __name__ == "__main__":
    connection_name = mysql_connect()
    sql = setup_cursor(connection_name)
    db_name = database_connect(sql)
    mysql_disconnect(connection_name)