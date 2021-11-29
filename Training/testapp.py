from tkinter import *
import sys
import mariadb
import tkinter as tk


# Accessing your database portal
try:
	conn=mariadb.connect(
		user='orleans lindsay',
		password='benooriginal',
		host='localhost',
		port=3306,
		database='test')
except mariadb.Error as e:
	print('Error',e)
	sys.exit(1)

cur = conn.cursor()
sqlinsert= "INSERT INTO product(name,description,price,image) VALUES(?,?,?,?)"
cur.execute(sqlinsert,("cup","For drinking water",20,"image"))
conn.commit()
conn.close()