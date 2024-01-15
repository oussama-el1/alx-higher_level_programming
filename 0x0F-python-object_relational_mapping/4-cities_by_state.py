#!/usr/bin/python3
"""the import i need to list all ciies"""
import MySQLdb
import sys

if __name__ == "__main__":
    connection = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3]
    )
    mycursor = connection.cursor()
    sql = '''
    select cities.id, cities.name, states.name
    from cities, states
    where cities.state_id = states.id
    order by cities.id;
    '''
    mycursor.execute(sql)
    data = mycursor.fetchall()

    for row in data:
        print(row)
    mycursor.close()
    connection.close()
