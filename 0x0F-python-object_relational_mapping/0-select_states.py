#!/usr/bin/python3
"""
Module to list all states from a MySQL database.
"""
import sys
import MySQLdb


if __name__ == "__main__":
    connection = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3],
        port=3306
    )

    mycursor = connection.cursor()
    mycursor.execute("SELECT * FROM states")
    data = mycursor.fetchall()
    for row in data:
        print(row)
    mycursor.close()
    connection.close()
