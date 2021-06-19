from datetime import datetime
from connection import get_sql_conn

def insert_order(connection,orders):
        cursor = connection.cursor()
        query = ("Insert into orders""(cust_name , all_total , date_time)""values(%s , %s , %s)")
        data = (orders['cust_name'] ,orders['all_total'], datetime.now())
        cursor.execute(query, data)
        o_id = cursor.lastrowid
        o_details_query = ("Insert into order_details""(o_id , p_id , quantity , total )""values(%s ,%s , %s , %s)")
        o_details_data=[ ]
        for order_details_record in orders['order_details']:
            o_details_data.append([
                o_id, 
                int (order_details_record['p_id']),
                float (order_details_record['quantity']),
                float (order_details_record['total'])
            ])
        cursor.executemany(o_details_query , o_details_data)
        connection.commit()
        return o_id

def get_order_details(connection,o_id):
    cursor= connection.cursor()
    query = ("select * from order_details where o_id = %s")
    query = ("select order_details.o_id , order_details.quantity ,order_details.p_id, order_details.total,  product.p_name, product.price_pu from order_details left join product on order_details.p_id = product.p_id where order_details.o_id = %s")
    data = (o_id,)
    cursor.execute(query, data)
    record=[]
    for(o_id,quantity,p_id,total,p_name,price_pu)in cursor:
         record.append({
            'o_id':o_id ,
            'quantity':quantity,
            'p_id':p_id , 
            'total':total,
            'p_name':p_name,
            'price_pu':price_pu
         })
    cursor.close()
    return record

def get_order(connection):
    cursor = connection.cursor()
    query = ("select order_details.o_id , order_details.quantity ,order_details.total ,orders.cust_name , orders.date_time from order_details inner join orders on order_details.o_id = orders.o_id;")
    cursor.execute(query)
    response = []
    for (o_id , quantity , total , cust_name , date , ) in cursor:
        response.append({'o_id':o_id , 'quantity':quantity , 'total':total , 'cust_name':cust_name , 'date': date})
    return response

if __name__ == '__main__':
    connection = get_sql_conn()
    #print(get_order(connection))
    #print(get_order_details(connection,10))
    '''print(insert_order(connection,{
         
                            
                'cust_name':'abhi',
                'all_total': '500',
                
                  'order_details': [
                                      {
                                          'p_id': 4,
                                          'quantity': 1,
                                           'total': 500
                                       },
                                     
                                   ]
                        
                         }))'''
                         