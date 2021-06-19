def get_uom(connection):
    cursor = connection.cursor()
    query = ("select * from uom;")
    cursor.execute(query)
    response = []
    for (uom_id , uom_name) in cursor:
        response.append({'uom_id':uom_id , 'uom_name':uom_name})
    return response
if __name__ == "__main__":
    from connection import get_sql_conn
    connection = get_sql_conn()
    print(get_uom(connection)) 