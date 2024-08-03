import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  database="register",
  user = "root",
  password = ""
)


mycursor = mydb.cursor()
 
sql = "INSERT INTO tb.teacher(id_teacher, f_name_teacher, l_name_teacher, major, email, tel) VALUES (%d, %s, %s, %s, %s, %s)"
val = ("021481", "Prach", "Choksamritpol","Ce", "puumpprach@gmail.com", "0958090462")


sql = "INSERT INTO tb.student(id_subject, subject_name, credits	, subject_type) VALUES (%s, %s, %s, %s)"
val = ("012345", "Thai", "2","language")
mycursor.execute(sql, val)

mydb.commit()
mydb.close()