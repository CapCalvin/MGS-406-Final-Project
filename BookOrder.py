from flask import Flask, url_for, redirect, render_template, request
import sqlite3 as sql
import mysql.connector

app = Flask(__name__)

@app.route("/")
def hello_world():
	return render_template("home.htm")



@app.route("/enternew")
def enternew():
	return render_template("BookOrder.htm")

@app.route("/addrec", methods = ['POST','GET'])
def addrec():
	if request.method == "POST":
		BookID = request.form['BookID']
		BookName = request.form['BookName']
		BookDate = request.form['BookDate']
		BookCategory = request.form['BookCategory']
		BookWriter = request.form['BookWriter']



		with mysql.connector.connect(host = "localhost", user="flask", password="ubuntu", database="BookOrder") as conn:
			cur = conn.cursor()
			cmd = "INSERT INTO Book_Order_Info (BookID,BookName,BookDate,BookCategory,BookWriter) VALUES ('{0}','{1}','{2}','{3}','{4}')".format(BookID,BookName,BookDate,BookCategory,BookWriter)
			cur.execute(cmd)
			conn.commit()
		
			msg = "Record successfully added"
		return render_template("output.htm", msg=msg)

@app.route('/list')
def list():
   con = mysql.connector.connect(host = "localhost", user="flask", password="ubuntu", database="BookOrder")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from Book_Order_Info")
   
   rows = cur.fetchall(); 
   return render_template("list.htm",rows = rows)

if __name__ =="__main__":
	app.run() 
