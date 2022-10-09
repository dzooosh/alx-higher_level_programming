#!/usr/bin/python3
"""
    Lists all the cities table of hbtn_0e_4_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    rows = cur.execute(""" SELECT c.id, c.name, s.name
                       FROM cities c JOIN states s
                       ON c.state_id=s.id
                       ORDER BY c.id""")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
