#!/usr/bin/python3
"""
gets cities from databases.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cur = db.cursor()
    cur.execute("""
                SELECT cities.name
                FROM cities LEFT JOIN states
                ON cities.state_id = states.id
                WHERE states.name = %(states name)s
                ORDER BY cities.id
                """, {'states name': sys.argv[4]})
    cities = cur.fetchall()
    cities = [tp[0] for tp in cities]
    print(', '.join(cities))

    cur.close()
    db.close()
