#!/usr/bin/python3
"""
    Lists all the cities based on state name in hbtn_0e_4_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    state_name = sys.argv[4]
    cur.execute("""SELECT cities.name FROM cities JOIN states
                ON cities.state_id=states.id
                WHERE states.name = %s""", (state_name,))
    rows = cur.fetchall()
    lst = [row[0] for row in rows]
    print(*set(lst), sep=", ")
    cur.close()
    db.close()
