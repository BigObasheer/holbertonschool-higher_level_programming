#!/usr/bin/python3
# Print all cities
import MySQLdb
from sys import argv

if __name__ == "__main__":

    user, passwd, database, search = argv[1], argv[2], argv[3], argv[4]
    db = MySQLdb.connect('localhost', user, passwd, database)

    find = db.cursor()

    find.execute("SELECT cities.id, cities.name, states.name\
                    FROM cities INNER JOIN states\
                    ON cities.state_id=states.id")

    data = find.fetchall()

    for cities in data:
        print(cities)

    find.close()
    db.close()
