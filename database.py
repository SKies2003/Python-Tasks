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

def mysql_disconnect(connection):
    if connection:
        connection.close()
    else:
        print("No Connection to disconnect!")

def setup_cursor(conn):
    try:
        mycursor = conn.cursor()
        print("Setup complete!")
        return mycursor
    except:
        print("An unexpected occured!")

def database_connect(mycursor, dbname: str = "pythonDB"): # Setting "pythonDB" as default database for python mysql database usage.
    try:
        mycursor.execute(f"CREATE DATABASE IF NOT EXISTS `{dbname}`")
        print("Database connected!")
        return dbname
    except:
        print("An unexpected occured!")
        return None

if __name__ == "__main__":
    connection_name = mysql_connect()
    sql = setup_cursor(connection_name)
    db_name = database_connect(sql)
    # sql.execute(f"USE {db_name}")
    # sql.execute("CREATE TABLE IF NOT EXISTS users (name VARCHAR(100), password VARCHAR(50))")
    # sql.execute("INSERT INTO users VALUES ('Gagan', 'hbdshvhjv666jdbvdhf')")
    # sql.execute("SELECT * FROM users")
    # result = sql.fetchall()
    # for x in result:
    #     print(x)
    mysql_disconnect(connection_name)