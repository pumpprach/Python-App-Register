import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  database="register",
  user = "root",
  password = "021481"
)


mycursor = mydb.cursor()
 
sql = "INSERT INTO tb.teacher(id_teacher, f_name_teacher, l_name_teacher, major, email, tel) VALUES (%d, %s, %s, %s, %s, %s)"
val = ("021481", "This", "is","Ai", "test@gmail.com", "0000000000")
mycursor.execute(sql, val)

mydb.commit()
mydb.close()