#!/usr/bin/python3
"""
Module to list all states from a MySQL database.
"""
import sys
import MySQLdb


def show_states():
    """
    List all states.
    """
    connection = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3],
    )

    mycursor = connection.cursor()
    sql = "SELECT * FROM states ORDER BY id"
    mycursor.execute(sql)
    data = mycursor.fetchall()

    for row in data:
        print(row)

    mycursor.close()
    connection.close()


if __name__ == "__main__":
    show_states()
