#!/usr/bin/python3
#dkljfladjf
import MySQLdb
from sys import argv

def main():
    """Connect to the MySQL database and fetch data from the states table."""
    # Connect to the database
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()

    # Execute SQL query
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()

    # Print the fetched data
    for row in query_rows:
        print(row)

    # Close cursor and connection
    cur.close()
    conn.close()

if __name__ == "__main__":
    main()