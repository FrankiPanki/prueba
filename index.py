#!/usr/bin/python
import cgi
import MySQLdb
print "Content-type: text/html"
print

print"""
hola mundo
"""

form=cgi.FieldStorage()
usr=form["user"].value
usr=form["pass"].value

print "<p>User:", form["user"].value
print "<p>Pass:", form["pass"].value

db=MySQLdb.connect(
	host="192.168.77.130",
	user="test",
	passwd="hola123,",
	db="redes",
)
cursor=db.cursor()
cursor.execute("SELECT username FROM login WHERE username= 'admin' and password = 'sup3rs3cretP@ssw0rd' LIMIT 1;")
if cursor.fetchone() is not None:
	print "<p>Bingo!! user and Password OK<\p>"
else:
	print "<p>Error!!! Wrong user or Password <\p>"
db.close()
