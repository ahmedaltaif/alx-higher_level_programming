#!/usr/bin/python3

if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    rows = cur.fetchall("SSELECT * FROM states ORDER BY states.id ASC")
    for row in rows:
        print(row)
    cur.close()
    db.close()
