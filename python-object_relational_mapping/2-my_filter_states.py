#!/usr/bin/python3
"""List all states from the database hbtn_0e_usa"""

import sys
import MySQLdb


def main():
    """Get arguments: username, password, database"""
    # TIME FOR BOILERPLATE
    user = sys.argv[1]
    passwrd = sys.argv[2]
    database = sys.argv[3]
    argument = sys.argv[4]

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=user,
        passwd=passwrd,
        db=database
    )

    # make a cursor
    cur = db.cursor()

    # THE ACTUAL THING THAT'S IMPORTANT
    cur.execute(f"SELECT * FROM states "
                f"WHERE name LIKE '{argument}%' "
                f"ORDER BY id ASC")

    # MORE BOILERPLATE
    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
