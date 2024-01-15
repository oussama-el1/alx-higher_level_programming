#!/usr/bin/python3
import sys
"""sys module"""
import MySQLdb
"""import mysqldb client for create connection with base"""

connection = MySQLdb.connect(
    host="localhost",
    user=sys.argv[1],
    password=sys.argv[2],
    database=sys.argv[3],
)

mycursor = connection.cursor()
sql = "SELECT * FROM states"
mycursor.execute(sql)
data = mycursor.fetchall()

for row in data:
    print(row)

mycursor.close()
connection.close()
