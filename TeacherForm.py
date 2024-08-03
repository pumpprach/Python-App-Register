from tkinter import*
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
def con_db():
    global cs, con
    con = mysql.connector.connect(host = "localhost",user="root",password= "",database = "register")
    cs = con.cursor()


def mainFormTeacher():
    def clearFrom():
        ent_id_teacher.delete(0,END)
        ent_fname.delete(0,END)
        ent_lname.delete(0,END)
        ent_majors.delete(0,END)
        ent_email.delete(0,END)
        ent_tel.delete(0,END)
        
    def insert_data():
        try:  
            if ent_id_teacher.get() == "" or ent_fname.get() == "" or ent_lname.get() == "" or ent_majors.get() == "" or ent_email.get() ==""or ent_tel.get() == "":   
                messagebox.showwarning("warning", "Please fill in all information.")
            else:
                con_db()
                cs = con.cursor()
                sql = "INSERT INTO tb_teacher (id_teacher,f_name,l_name,majors,email,tel) VALUES (%s,%s,%s,%s,%s,%s)"
                val = (
                    str(ent_id_teacher.get()),
                    str(ent_fname.get()),  
                    str(ent_lname.get()),
                    str(ent_majors.get()),
                    str(ent_email.get()),
                    str(ent_tel.get())
                    )
                cs.execute(sql,val) 
                con.commit()  
                con.close()
                cs.close()
                clearFrom()
                #insertDataTreeview()
                
                messagebox.showwarning("warning", "Recording Successful")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error:{err}")
    
    def selectTreeView(event):
        clearFrom()
        item = viewTrc.selection()
        for i in item:
            ent_id_teacher.insert("",viewTrc.item(i, "values")[0])
            ent_fname.insert("",viewTrc.item(i, "values")[1])
            ent_lname.insert("",viewTrc.item(i, "values")[2])
            ent_majors.insert("",viewTrc.item(i, "values")[3])
            ent_email.insert("",viewTrc.item(i, "values")[4])
            ent_tel.insert("",viewTrc.item(i, "values")[5])
    def update_data():
        if not viewTrc.selection():
            messagebox.showinfo("warning", "You have not selected any data yet.")  
        else:
            con_db()
            cs.execute("UPDATE tb_teacher set id_teacher = %s, f_name = %s, l_name= %s, majors = %s,email=%s,tel =%s WHERE id_teacher = %s",(str(ent_id_teacher.get()),str(ent_fname.get()),str(ent_lname.get()),str(ent_majors.get()),str(ent_email.get()),str(ent_tel.get()),str(ent_id_teacher.get())))
            msgBox = messagebox.askquestion("Information", "Do you want to edit your information?",icon = "warning")
            if msgBox == "yes":
                con.commit()
            con.close()
            cs.close()
            clearFrom()
            insertDataTreeview()   
            
    def insertDataTreeview():
        for c in viewTrc.get_children():
            viewTrc.delete(c)
        con_db()
        cs.execute("select * from tb_teacher")
        data = cs.fetchall()
        
        for d in data:
            viewTrc.insert("","end", values=d)  
        con.close()
        cs.close()
    def delete_data():
        if not viewTrc.selection():
            messagebox.showinfo("information","You haven't selected the data you want to delete.")
        else:
            item = viewTrc.selection()
            for i in item:
                    con_db()
                    cs.execute("DELETE FROM tb_teacher WHERE id_teacher = %s" % viewTrc.item(i,"values")[0])
                    msgBox = messagebox.askquestion("warning", "Do you want to delete your data?")
                    
                    if msgBox == "yes":
                        con.commit()
            con.close()
            cs.close()            
            clearFrom()
            insertDataTreeview()
            
    
    
    root = Tk()
    root.title("Teacher Registration System")
    root.geometry("900x620")
    #การสร้าง labelFrame
    lblFrame = ttk.LabelFrame(root,text="Add/edit historical data register", labelanchor="nw")
    lblFrame.place(height=300, width= 500, x=10, y=10)
    
    lbl_id_teacher = ttk.Label(lblFrame, text= "Teacher ID",font= 16)
    lbl_id_teacher.place(height=20, width=80,x= 20, y=20)
    
    lbl_fname = ttk.Label(lblFrame, text= "Name",font= 16)
    lbl_fname.place(height=20, width=80,x= 20, y=75)
    
    lbl_lname = ttk.Label(lblFrame, text= "Surname",font= 16)
    lbl_lname.place(height=20, width=80,x= 20, y=110)
    lbl_majors = ttk.Label(lblFrame, text= "Major",font= 16)
    lbl_majors.place(height=20, width=80,x= 20, y=150)
    lbl_email = ttk.Label(lblFrame, text= "E-mail",font= 16)
    lbl_email.place(height=20, width=80,x= 20, y=190)
    lbl_tel = ttk.Label(lblFrame, text= "Tel",font= 16)
    lbl_tel.place(height=20, width=80,x= 20, y=230)
    
    ent_id_teacher = ttk.Entry(lblFrame,)
    ent_id_teacher.place(height=30, width=180, x=120, y=25)
    ent_fname = ttk.Entry(lblFrame,)
    ent_fname.place(height=30, width=180, x=120, y=65)
    ent_lname = ttk.Entry(lblFrame,)
    ent_lname.place(height=30, width=180, x=120, y=105)
    ent_majors = ttk.Entry(lblFrame,)
    ent_majors.place(height=30, width=180, x=120, y=145)
    ent_email = ttk.Entry(lblFrame,)
    ent_email.place(height=30, width=180, x=120, y=190)
    ent_tel = ttk.Entry(lblFrame,)
    ent_tel.place(height=30, width=180, x=120, y=230)
    
    btn_save = ttk.Button(root,text= "record",command=insert_data)
    btn_save.place(height=50, width=150,x=600,y=20)
    btn_edit = ttk.Button(root,text= "Edit", command=update_data)
    btn_edit.place(height=50, width=150,x=600,y=75)
    btn_delete = ttk.Button(root,text= "Delete",command=delete_data)
    btn_delete.place(height=50, width=150,x=600,y=130)
    btn_cancel = ttk.Button(root,text= "Cancel",command=clearFrom)
    btn_cancel.place(height=50, width=150,x=600,y=185)
    btn_exit = ttk.Button(root,text= "Exit",command=quit)
    btn_exit.place(height=50, width=150,x=600,y=240)
    
    viewTrc = ttk.Treeview(root,columns=("id","fName","lName","Majors","Email","Tel"),show="headings")
    viewTrc.place(height=250,width=820,x=20,y=350)
    
    sc = ttk.Scrollbar(root, orient="vertical",command=viewTrc.yview)
    sc.place(height=248,x=823,y=352)
    
    viewTrc.config(yscrollcommand=sc.set)
    viewTrc.column("#1" , width=80)
    viewTrc.column("#2" , width=100)
    viewTrc.column("#3" , width=100)
    viewTrc.column("#4" , width=120)
    viewTrc.column("#5" , width=120)
    viewTrc.column("#6" , width=80)
    
    viewTrc.heading("#1",text="ID")
    viewTrc.heading("#2",text="F_name")
    viewTrc.heading("#3",text="L_name")
    viewTrc.heading("#4",text="Majors")
    viewTrc.heading("#5",text="Email")
    viewTrc.heading("#6",text="Tel")
    
    viewTrc.bind('<ButtonRelease>', selectTreeView)
    insertDataTreeview()
    
    root.mainloop()
if __name__ == "__main__":
    mainFormTeacher()
    