from connection import get_sql_conn

def get_all_products(connection):
    cursor = connection.cursor()
    query = ("select product.p_id, product.p_name, product.uom_id, product.price_pu, uom.uom_name from product inner join uom on product.uom_id=uom.uom_id")
    cursor.execute(query)
    response = []
    for (p_id, p_name, uom_id, price_pu, uom_name) in cursor:
        response.append({
            'p_id': p_id,
            'p_name': p_name,
            'uom_id': uom_id,
            'price_pu': price_pu,
            'uom_name': uom_name
        })
    return response

def insert_new_product(connection,product):
    cursor = connection.cursor()
    query = ("INSERT INTO product "
             "(p_name, uom_id, price_pu)"
             "VALUES (%s, %s, %s)")
    data = (product['p_name'], product['uom_id'], product['price_pu'])

    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid

def delete_product(connection, p_id):
    cursor = connection.cursor()
    query = ("DELETE FROM product where p_id=" + str(p_id))
    cursor.execute(query)
    connection.commit()

    return cursor.lastrowid

if __name__ == '__main__':
    connection = get_sql_conn()
    #print(get_all_products(connection))
    '''print(insert_new_product(connection,{
        'p_name': 'tomato',
        'uom_id': '2',
        'price_pu': 15
    }))'''
    #print(delete_product(connection,13))