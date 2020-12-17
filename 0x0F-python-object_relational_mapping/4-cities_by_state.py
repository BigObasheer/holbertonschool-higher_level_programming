#!/usr/bin/python3
# Print all cities
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    find = db.cursor()

    find.execute("SELECT cities.id, cities.name, states.name\
                    FROM cities INNER JOIN states\
                    ON cities.state_id=states.id")

    data = find.fetchall()

    for cities in data:
        print(cities)

    find.close()
    db.close()
