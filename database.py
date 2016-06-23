import sqlite3

conn = sqlite3.connect('crollodb.db')
c = conn.cursor()

conn2 = sqlite3.connect('crollodb.db')
c2 = conn2.cursor()