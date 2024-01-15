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
        SELECT cities.name FROM
        cities INNER JOIN states ON states.id=cities.state_id
        WHERE states.name=%s
    '''
    mycursor.execute(sql, (sys.argv[4],))
    cityes = mycursor.fetchall()
    for city in cityes:
        print(city[0], end=', ')
    print()
    mycursor.close()
    connection.close()
