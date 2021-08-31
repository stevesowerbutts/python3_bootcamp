# Python + SQL

Demo with SQLITE3 (General concepts should work with any SQL db.)
Preinstalled on mac
https://www.sqlite.org/index.html

## SQL Syntax

Open with `sqlite3` command (opens terminal).
`.help` - list of commands

* Storage Classes and Datatypes
Each value stored in an SQLite database (or manipulated by the database engine) has one of the following storage classes:

`NULL.` The value is a NULL value.
`INTEGER.` The value is a signed integer, stored in 1, 2, 3, 4, 6, or 8 bytes depending on the magnitude of the value.
`REAL.` The value is a floating point value, stored as an 8-byte IEEE floating point number.
`TEXT.` The value is a text string, stored using the database encoding (UTF-8, UTF-16BE or UTF-16LE).
`BLOB.` The value is a blob of data, stored exactly as it was input.

* Creating a table via cli (can also create via script see basics.sql)
```
Connected to a transient in-memory database.
Use ".open FILENAME" to reopen on a persistent database.

sqlite> .open dog_db.db
sqlite> CREATE TABLE dogs (name TEXT, breed TEXT, age INTEGER);
sqlite> .tables
dogs

sqlite> INSERT INTO dogs (name,breed,age) VALUES ("Blue", "Scottish Fold", 3);
sqlite> select * from dogs;
Blue|Scottish Fold|3
```

Can run sql scripts (basics.sql) to create tables or insert data using the below:
`sqlite> .read basics.sql`

* Selecting data
`select * from dogs` - select all columns from dogs table
`select name from dogs` - select the name column from dogs

```
sqlite> SELECT * FROM dogs WHERE name IS "Piggy";
Piggy|Lab|7

sqlite> SELECT * FROM dogs WHERE breed IS NOT "Husky" AND breed IS NOT "Lab";
BLue|Scottish Fold|3
Blue|Scottish Fold|3

sqlite> SELECT * FROM dogs WHERE age > 3;
Piggy|Lab|7
```

## Connecting to a db with python
sqlite3 comes built in with python3 so just need to import and set up the connection to db:
```
import sqlite3
conn = sqlite3.connect('dogs_db.db')
```

See friends.py
- need a cursor object - basically an in memory workspace on the database
- execute some sql
- commit changes

Insert data into the database:
```
data = ("Steve", "Irwin", 9)
query = "INSERT INTO friends VALUES (?,?,?)"
c.execute(query, data)
```

Bulk inserts (see bulk_inserts.py)

Can use c.executemany() to insert all at once:
```
# Insert all at once
c.executemany("INSERT INTO friends VALUES (?,?,?)", people)
```

If you need to insert data and do something with the values, it would be better to use a loop:
```
average = 0
for person in people:
	c.execute("INSERT INTO friends VALUES (?,?,?)", person)
	average += person[2]
print(average/len(people))
```
