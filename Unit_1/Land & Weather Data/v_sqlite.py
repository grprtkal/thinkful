import sqlite3 as lite
import pandas as pd

#connect to database
con = lite.connect("sample_db.db")

with con:
    # create cursor object which goes over records that result from query
    cur = con.cursor()

    # call cursor object's execute method; this is where you select, create tables
    cur.execute("SELECT * FROM weather")

    # fetch all data from cursor object
    rows = cur.fetchall()

    # get column names; cur.description has 7 tuples: name, type_code, display_size, internal_size, precision, scale,
    # null_okay; desc[0] = name
    cols = [desc[0] for desc in cur.description]

    df = pd.DataFrame(rows, columns=cols)

    print df







