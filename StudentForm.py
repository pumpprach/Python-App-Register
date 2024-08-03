from tkinter import*
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
def con_db():
    global cs, con
    con = mysql.connector.connect(host = "localhost",user="root",password= "",database = "register")
    cs = con.cursor()


def mainFormStudent():
    def clearFrom():
        ent_id_subject.delete(0,END)
        ent_subject_name.delete(0,END)
        ent_credits.delete(0,END)
        ent_subject_type.delete(0,END)
        
    def insert_data():
        try:  
            if ent_id_subject.get() == "" or ent_subject_name.get() == "" or ent_credits.get() == "" or ent_subject_type.get() == "" :   
                messagebox.showwarning("warning", "Please fill in all information.")
            else:
                con_db()
                cs = con.cursor()
                sql = "INSERT INTO tb_subject (id_subject,subject_name,credits,subject_type) VALUES (%s,%s,%s,%s)"
                val = (
                    str(ent_id_subject.get()),
                    str(ent_subject_name.get()),  
                    str(ent_credits.get()),
                    str(ent_subject_type.get())
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
            ent_id_subject.insert("",viewTrc.item(i, "values")[0])
            ent_subject_name.insert("",viewTrc.item(i, "values")[1])
            ent_credits.insert("",viewTrc.item(i, "values")[2])
            ent_subject_type.insert("",viewTrc.item(i, "values")[3])

    def update_data():
        if not viewTrc.selection():
            messagebox.showinfo("warning", "You have not selected any data yet.")  
        else:
            con_db()
            cs.execute("UPDATE tb_subject set id_subject = %s, subject_name = %s, credits= %s, subject_type = %s WHERE id_subject = %s",(str(ent_id_subject.get()),str(ent_subject_name.get()),str(ent_credits.get()),str(ent_subject_type.get()),str(ent_id_subject.get())))
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
        cs.execute("select * from tb_subject")
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
                    cs.execute("DELETE FROM tb_subject WHERE id_subject = %s" % viewTrc.item(i,"values")[0])
                    msgBox = messagebox.askquestion("warning", "Do you want to delete your data?")
                    
                    if msgBox == "yes":
                        con.commit()
            con.close()
            cs.close()            
            clearFrom()
            insertDataTreeview()
            
    
    
    root = Tk()
    root.title("Subject Information System")
    root.geometry("900x620")
    #การสร้าง labelFrame
    lblFrame = ttk.LabelFrame(root,text="Add/edit Subject Imformation", labelanchor="nw")
    lblFrame.place(height=300, width= 500, x=10, y=10)
    
    lbl_id_subject = ttk.Label(lblFrame, text= "Subject ID : ",font= 16)
    lbl_id_subject.place(height=20, width=120,x= 20, y=20)
    lbl_subject_name = ttk.Label(lblFrame, text= "Subject Name : ",font= 16)
    lbl_subject_name.place(height=20, width=120,x= 20, y=75)
    lbl_credits = ttk.Label(lblFrame, text= "Credits : ",font= 16)
    lbl_credits.place(height=20, width=120,x= 20, y=110)
    lbl_subject_type = ttk.Label(lblFrame, text= "Subject Type : ",font= 16)
    lbl_subject_type.place(height=20, width=120,x= 20, y=150)
    
    ent_id_subject = ttk.Entry(lblFrame,)
    ent_id_subject.place(height=30, width=180, x=150, y=25)
    ent_subject_name = ttk.Entry(lblFrame,)
    ent_subject_name.place(height=30, width=180, x=150, y=65)
    ent_credits = ttk.Entry(lblFrame,)
    ent_credits.place(height=30, width=180, x=150, y=105)
    ent_subject_type = ttk.Entry(lblFrame,)
    ent_subject_type.place(height=30, width=180, x=150, y=145)
    
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
    
    viewTrc = ttk.Treeview(root,columns=("ID_Subject","Subject_Name","Credits","Subject_Type"),show="headings")
    viewTrc.place(height=250,width=820,x=20,y=350)
    
    sc = ttk.Scrollbar(root, orient="vertical",command=viewTrc.yview)
    sc.place(height=248,x=823,y=352)
    
    viewTrc.config(yscrollcommand=sc.set)
    viewTrc.column("#1" , width=80)
    viewTrc.column("#2" , width=100)
    viewTrc.column("#3" , width=100)
    viewTrc.column("#4" , width=120)
    
    viewTrc.heading("#1",text="ID_Subject")
    viewTrc.heading("#2",text="Subject Name")
    viewTrc.heading("#3",text="Credits")
    viewTrc.heading("#4",text="Subject Type")

    
    viewTrc.bind('<ButtonRelease>', selectTreeView)
    insertDataTreeview()
    
    root.mainloop()
if __name__ == "__main__":
    mainFormStudent()
    