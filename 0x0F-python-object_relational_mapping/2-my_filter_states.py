#!/usr/bin/python3
"""
gets states from databases.
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
                SELECT *
                FROM states
                WHERE name = '{}'
                ORDER BY id ASC
                """.format(sys.argv[4]))
    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    db.close()
