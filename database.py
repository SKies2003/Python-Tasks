import mysql.connector
import db_credentials as cred

def database_connect():
    try:
        db = mysql.connector.connect(
            host = cred.MYSQL_HOST,
            user = cred.MYSQL_USER,
            password = cred.MYSQL_PASSWORD
        )
        return db
    except:
        return None

def database_disconnect(database):
    if database:
        database.close()
    else:
        print("No Database to disconnect!")

if __name__ == "__main__":
    db = database_connect()
    database_disconnect(db)