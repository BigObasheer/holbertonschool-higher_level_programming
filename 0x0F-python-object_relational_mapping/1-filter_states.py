#!/usr/bin/python3
"""lists all states with a name starting with N"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    user, passwd, database = argv[1], argv[2], argv[3]
    db = MySQLdb.connect('localhost', user, passwd, database)

    find = db.cursor()
    find.execute("SELECT * FROM states ORDER BY states.id ASC;")

    data = find.fetchall()
    for row in data:
        state = row[1]
        if state[0] == "N":
            print(row)

    find.close()
    db.close()
