#!/usr/bin/python3
"""List all states from the database hbtn_0e_4_usa"""

import sys
import MySQLdb


def main():
    """Set up for throwing query into MySQL"""
    # TIME FOR BOILERPLATE
    user = sys.argv[1]
    passwrd = sys.argv[2]
    database = sys.argv[3]
    #  This will be the state name
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
    cur.execute(
        "SELECT cities.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC",
        (argument,)
    )

    #  MORE BOILERPLATE
    #  This time is a bit different. as we have to do a different loop
    rows = cur.fetchall()
    print(", ".join([row[0] for row in rows]))

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
