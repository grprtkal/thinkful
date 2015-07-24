import sqlite3 as lite
import pandas as pd

# connect to database
con = lite.connect("sample_db.db")

# create values for table
cities = (('New York City', 'NY'),
              ('Los Angeles', 'CA'),
              ('Boston', 'MA'))

weather = (('New York City', 2013, 'July', 'December'),
               ('Atlanta', 2011, 'February', 'August'),
               ('Boston', 2010, 'March', 'October'))

with con:
    # create cursor object which goes over records that result from query
    cur = con.cursor()

    # drop table if it already exists
    cur.execute("DROP TABLE IF EXISTS cities")
    cur.execute("DROP TABLE IF EXISTS weather")

    # create cities and weather tables
    cur.execute("CREATE TABLE cities (name text, state text)")
    cur.execute("CREATE TABLE weather (city text, year integer, warm_month text, cold_month text)")

    # insert values into cities and weather tables
    cur.executemany("INSERT INTO cities VALUES (?, ?)", cities)
    cur.executemany("INSERT INTO weather VALUES (?, ?, ?, ?)", weather)

    # join data together
    rows = cur.execute("SELECT * FROM cities INNER JOIN weather ON name = city")

    # retrieve data
    rows = cur.fetchall()

    # load data into a pandas data frame
    df = pd.DataFrame(rows)

    # create variables for data frame values
    city = df[0]
    state = df[1]
    warm_month = df[4]

    # print city and sentence
    for row in rows:
        print "The cities are: {0}, {1} and their warmest months are: {2}".format(city, state, warm_month)







