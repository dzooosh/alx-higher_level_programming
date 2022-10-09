#!/usr/bin/python3
"""
    Displays all values in the states table of hbtn_0e_0_usa
    based on state name searched
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    data = sys.argv[4]
    cur.execute("SELECT * FROM states "
                "WHERE name LIKE BINARY '{}'".format(data))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
