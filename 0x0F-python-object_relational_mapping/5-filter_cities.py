#!/usr/bin/env python3

import MySQLdb
import sys

def main():
    if len(sys.argv) !=  5:
        print("Usage: python script.py <mysql_username> <mysql_password> <database_name> <state_name>")
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username, passwd=mysql_password, db=database_name)
    cursor = db.cursor()

    query = """
    SELECT cities.name
    FROM cities
    INNER JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """

    cursor.execute(query, (state_name,))
    results = cursor.fetchall()

    if results:
        for row in results:
            print(row[0])
    else:
        print("No cities found for the state '{}'.".format(state_name))

    cursor.close()
    db.close()

if __name__ == "__main__":
    main()
