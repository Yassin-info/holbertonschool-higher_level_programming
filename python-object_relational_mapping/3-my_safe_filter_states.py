#!/usr/bin/python3
"""
Script that displays all values in states table where name matches argument
Safe from MySQL injection
"""
import MySQLdb
import sys


if __name__ == "__main__":
    """
    Connect to MySQL server and safely retrieve states matching the argument
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name = %s \
ORDER BY id ASC", (sys.argv[4],))
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
