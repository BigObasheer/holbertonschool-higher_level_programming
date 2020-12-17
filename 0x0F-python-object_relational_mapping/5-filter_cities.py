#!/usr/bin/python3
# Filter cities
import MySQLdb
from sys import argv

if __name__ == "__main__":

    user, passwd, database, search = argv[1], argv[2], argv[3], argv[4]
    db = MySQLdb.connect('localhost', user, passwd, database)

    find = db.cursor()

    find.execute("""SELECT cities.name FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name=%s
        ORDER BY 'cities.id' ASC;""", (search,) )

    data = find.fetchall()
    print(", ".join(row[0] for row in data))

    find.close()
    db.close()
