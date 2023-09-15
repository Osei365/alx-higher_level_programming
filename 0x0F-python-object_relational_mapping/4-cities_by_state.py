#!/usr/bin/python3
"""
gets cities from databases.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=db
    )
    cur = db.cursor()
    cur.execute("""
                SELECT cities.id, cities.name, states.name
                FROM cities LEFT JOIN states
                ON cities.state_id = states.id
                ORDER BY cities.id
                """)
    cities = cur.fetchall()

    for city in cities:
        print(city)

    cur.close()
    db.close()
