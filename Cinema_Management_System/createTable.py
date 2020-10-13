import sqlite3

conn = sqlite3.connect('cms.db')

c= conn.cursor()

#only one time
'''
c.execute(""" CREATE TABLE movies(    
    name text,
    desc text,
    language text,
    subtitle text,
    price integer,
    time text,
    date text,
    tickets integer,
    cover blob
    )""")
    
c.execute(""" CREATE TABLE Audience(
    
    username text,
    name text,
    email text,
    pNumber integer,
    password text,
    approved text
    )""")

c.execute(""" CREATE TABLE management(
    
    username text,
    name text,
    email text,
    pNumber integer,
    password text,
    role text
    )""")

c.execute("""INSERT INTO management(username, name, email, pNumber, password, role)
            VALUES('Admin', 'Administrator', 'admin@mail.com', 3207062783,'adminPass123', 'admin')""")


c.execute(""" CREATE TABLE bookings(
    userId integer,
    movieId integer,
    userName text,
    movieName text,
    bookBy text,
    price integer,
    time text,
    date text,
    seats integer
    )""")
'''
#Viewing All users in Debugging Mode
c.execute("Select oid,* FROM Audience")
records=c.fetchall()
print(records)

conn.commit()
conn.close()
