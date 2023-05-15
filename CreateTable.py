import mysql.connector as sql

conn = sql.connect(host="localhost", user="flask", password="ubuntu", database="BookOrder")

cur = conn.cursor()

cmd = "CREATE TABLE Book_Order_Info (\
    sid INT NOT NULL AUTO_INCREMENT PRIMARY KEY, \
    BookID INTEGER(30) NOT NULL, \
    BookName VARCHAR(30) NOT NULL,\
    BookDate DATE, \
    BookCategory VARCHAR(30), \
    BookWriter VARCHAR(30))"

cur.execute(cmd)

conn.close()