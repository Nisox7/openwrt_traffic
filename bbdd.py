#"MYSQL ON 192.168.0.166"

"CREATE TABLE TRAFFIC (ID int PRIMARY KEY AUTO_INCREMENT, TX VARCHAR(50), RX VARCHAR(50), ACTUAL_TX VARCHAR(50), ACTUAL_RX VARCHAR(50), TS TIMESTAMP DEFAULT current_timestamp);"
"DROP TABLE TRAFFIC;"
import pymysql
from env import database_host, database_user, database_password, database_table, database_name

def connect():
    try:
        connection = pymysql.connect(host=database_host,
                                user=database_user,
                                password=database_password,
                                db=database_name)
        #print("Conexión correcta")
        cursor = connection.cursor()
        
        return connection, cursor

    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrió un error al conectar: ", e)

    

#--------------------------

def write_db(tx,rx,actual_tx,actual_rx):
    
    ddbb = connect()
    connection=ddbb[0]
    cursor=ddbb[1]

    try:
        cursor.execute(f"INSERT INTO {database_table} VALUES (NULL,{tx},{rx},{actual_tx},{actual_rx},DEFAULT)")
        connection.commit()
        #print("db written correctly")
        connection.close()
    except Exception as e:
        print(f"error writing db:\n{e}")

#--------------------------

def read_db(args):

    ddbb = connect()
    connection=ddbb[0]
    cursor=ddbb[1]


    cursor.execute(f"SELECT {args} FROM {database_table}")
    read = cursor.fetchall()

    connection.close()

    return read
#--------------------------

def get_last_value():
    ddbb = connect()
    connection=ddbb[0]
    cursor=ddbb[1]


    cursor.execute(f"SELECT * FROM {database_table} ORDER BY ID DESC LIMIT 1")
    read = cursor.fetchall()

    connection.close()

    return read
