import mysql.connector
__cnx = None
def get_sql_conn():
    print("Opening mysql connection") 
    global __cnx
    if __cnx is None:
        __cnx = mysql.connector.connect(user = 'root', password = 'rootadmin@123', host ='127.0.0.1',database = 'gs')
    return __cnx