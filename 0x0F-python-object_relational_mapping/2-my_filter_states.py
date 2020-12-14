#!/usr/bin/python3
""" displays all values in the states table where name matches the argument """
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    find = db.cursor()
    find.execute("SELECT * FROM states\
                    WHERE BINARY name='{}'".format(search))

    data = find.fetchall()
    for state in data:
        print(state)

    find.close()
    db.close()
