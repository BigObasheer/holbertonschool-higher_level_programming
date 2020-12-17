#!/usr/bin/python3
""" displays all values in the states table of hbtn_0e_0_usa """
from sys import argv
import MySQLdb


if __name__ == "__main__":
    user, passwd, database, search = argv[1], argv[2], argv[3], argv[4]
    db = MySQLdb.connect('localhost', user, passwd, database)

    find = db.cursor()

    find.execute("SELECT * FROM states\
                    WHERE name=%s\
                    ORDER BY states.id ASC;", (search,))

    data = find.fetchall()
    for state in data:
        print(state)

    find.close()
    db.close()
