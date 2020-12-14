#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


def getall_states():
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    a = db.cursor()
    a.execute("""SELECT * FROM states ORDER BY states.id ASC;""")
    data = a.fetchall()
    for state in data:
        print(state)
    a.close()
    db.close()


if __name__ == "__main__":
    getall_states()
