from tkinter import *
import sys
import mariadb
import tkinter as tk


# Accessing your database portal
try:
	conn=mariadb.connect(
		user='root',
		password='benooriginal',
		host='localhost',
		port=3306,
		database='dealership')
except mariadb.Error as e:
	print('Error',e)
	sys.exit(1)

carname= input("Please enter the name of the car: ")
modelname= input("Please enter the model of the car: ")
year=input("Enter the year: ")
chassisnumber=input("Enter your chassis number: ")
brandname=input("Enter the brand of the car: ")

# representing as a tuple
def getData(car_name,m_number,y,cha,brnd):
	return (car_name,m_number,y,cha,brnd)

# Get connection cursor and insert data tp database after close connection
def saveData():
	cur =conn.cursor()
	sqlinsert="INSERT INTO car(name,model,year,chassis,brand) VALUES(?,?,?,?,?)"
	mydata = getData(carname,modelname,year,chassisnumber,brandname)
	cur.execute(sqlinsert,mydata)
	conn.commit()
	conn.close()

saveData()