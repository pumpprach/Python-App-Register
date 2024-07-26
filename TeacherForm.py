from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

def con_bd():
   global cs, con
   con = mysql.connector.connect(host = "localhost",user="root", password="",database="register")
   cs = con.cursor()



def mainFormTeacher():
  def clearFrom():
       ent_id_teacher.delete(0,END)
       ent_fname.delete(0,END)
       ent_gmail.delete(0,END)
       ent_lname.delete(0,END)
       ent_major.delete(0,END)
       ent_tel.delete(0,END)


       
  def insert_data():
      try:
        if ent_id_teacher.get() == "" or ent_fname.get() == "" or ent_gmail.get() == "" or ent_lname.get() == "" or ent_major.get() == "" or ent_tel.get() == "" :
            messagebox.showwaring("waring", "Please fill out all fields")
        else:
            con_db()
            cs = con.cursor()
            sql = "INSERT INTO tb_teacher (id_teacher, f_name_teacher, l_name_teacher, major, email, tel) VALUES (%s, %s, %s, %s, %s, %s)"
            val = (
              str(ent_id_teacher.get()),
              str(ent_fname.get()),
              str(ent_lname.get()),
              str(ent_gmail.get()),
              str(ent_major.get()),
              str(ent_tel.get()),
              )
        cs.execute(sql,val)
        con.commit()
        con.close()
        cs.close()
        clearFrom()
        insertDataTreeview()


        messagebox.showwarning("Warning", "Data saved successfully")

      except mysql.connector.Error as err:
         messagebox.showerror("error", f"Error:{err}")

  def selectTreeView(event):

    clearFrom()
    item = view.selection()
    for i in item:
      ent_id_teacher.insert("",view.item(i, "values")[0])
      ent_fname.insert("",view.item(i, "values")[1])
      ent_lname.insert("",view.item(i, "values")[2])
      ent_major.insert("",view.item(i, "values")[3])
      ent_gmail.insert("",view.item(i, "values")[4])
      ent_tel.insert("",view.item(i, "values")[5])

  def update_data():
    if not view.selection():
      messagebox.showinfo("warning", "คุณยังไม่ได้เลือกข้อมูล")
    else:
      con_db()
      cs.execute("UPDATE tb_teacher set id_teacher = %s, f_name_teacher = %s, l_name_teacher, major = %s, email = %s, tel = %s" (str(ent_id_teacher.get()), str(ent_fname.get()), str(ent_lname.get()), str(ent_major.get()), str(ent_email.get()), str(ent_tel.get())))

      msgBox = messagebox.askquestion("Information", "ต้องการเเก้ไขข้อมูลมั้ย")
      if msgBox == "yes":
        con.commit()
      con.close()
      cs.close()
      clearFrom()
      insertDataTreeview()

  def insertDataTreeview():
      for c in view.get.children():
        view.delete(c)
      con_bd()
      cs.execute("SELECT * FROM tb_teacher")
      data = cs.fetchall()
      for d in data:
        view.insert("", "END", values=d)
      con.close()
      cs.close()

    root = Tk()
    root.title("ระบบทะเบียนอาจารย์")
    root.geometry("900x620")
    
    
    lblFrame = ttk.LabelFrame(root, text= "Add/Edit Register Form")
    lblFrame.place(height=300, width=500, x=10, y=10)
    
    lbl_id_teacher = ttk.Label(lblFrame, text="ID", font = 16)
    lbl_id_teacher.place(height=20, width=80, x=20, y=25)    
    
    lbl_fname = ttk.Label(lblFrame, text="Name", font = 16)
    lbl_fname.place(height=20, width=80, x=20, y=67)
    
    lbl_lname = ttk.Label(lblFrame, text="Surname", font = 16)
    lbl_lname.place(height=20, width=80, x=20, y=110)
    
    lbl_major = ttk.Label(lblFrame, text="Major", font = 16)
    lbl_major.place(height=20, width=80, x=20, y=150)

    lbl_gmail = ttk.Label(lblFrame, text="Email", font = 16)
    lbl_gmail.place(height=20, width=80, x=20, y=190)

    lbl_tel = ttk.Label(lblFrame, text="Tel", font = 16)
    lbl_tel.place(height=20, width=80, x=20, y=230)
    
    ent_id_teacher =  ttk.Entry(lblFrame, )      
    ent_id_teacher.place(height=30, width=180, x=120, y=25)      
    ent_fname =  ttk.Entry(lblFrame, )      
    ent_fname.place(height=30, width=180, x=120, y=65)    
    ent_lname =  ttk.Entry(lblFrame, )      
    ent_lname.place(height=30, width=180, x=120, y=105)
    ent_major =  ttk.Entry(lblFrame, )      
    ent_major.place(height=30, width=180, x=120, y=145)        
    ent_gmail =  ttk.Entry(lblFrame, )      
    ent_gmail.place(height=30, width=180, x=120, y=190)    
    ent_tel =  ttk.Entry(lblFrame, )      
    ent_tel.place(height=30, width=180, x=120, y=230)
    
    
    btn_save =ttk.Button(root,text= "Save",command=insert_data)
    btn_save.place(height=50, width=150, x= 600, y= 20)
    btn_edit =ttk.Button(root,text= "Edit", command=update_data)
    btn_edit.place(height=50, width=150, x= 600, y= 75) 
    btn_delete =ttk.Button(root,text= "Delete")
    btn_delete.place(height=50, width=150, x= 600, y= 130)     
    btn_cancel =ttk.Button(root,text= "Cancel")
    btn_cancel.place(height=50, width=150, x= 600, y= 185)     
    btn_exit =ttk.Button(root,text= "Quit", command=quit)
    btn_exit.place(height=50, width=150, x= 600, y= 240)    
     
     
     
     
     
    view = ttk.Treeview(root,columns=("ID", "Name", "Lastname", "Major", "Email", "Tel"), show="headings")
    view.place(height=250, width=820, x=20, y=350)

    scrollBar = ttk.Scrollbar(root, orient="vertical")
    scrollBar.place(height=248, x=822, y=352)

    view.config(yscrollcommand=scrollBar.set)
    view.column("#1", width="80")
    view.column("#2", width="100")
    view.column("#3", width="100")
    view.column("#4", width="120")
    view.column("#5", width="120")
    view.column("#6", width="80")

    view.heading("#1", text="ID")
    view.heading("#2", text="Name")
    view.heading("#3", text="Surname")
    view.heading("#4", text="Major")
    view.heading("#5", text="Email")
    view.heading("#6", text="Tel")     

    view.bind('<ButtonRelease>', selectTreeView)
    insertDataTreeview()

root.mainloop()
if __name__ == "__main__":
  mainFormTeacher()