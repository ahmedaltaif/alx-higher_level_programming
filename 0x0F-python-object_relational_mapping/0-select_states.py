#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        user=sys.argv[1], passwd=sys.argv[2],
        db=sys.argv[3], host="localhost", port=3306
    )
    cu = db.cursor()
    num = cu.exuecute("SELECT * FROM states ORDER BY states.id")
    for states in cu:
        print(states)
