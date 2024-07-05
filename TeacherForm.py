from tkinter import *
from tkinter import ttk

def mainFormTeacher():
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
    
    
    btn_save =ttk.Button(root,text= "Save")
    btn_save.place(height=50, width=150, x= 600, y= 20)
    btn_edit =ttk.Button(root,text= "Edit")
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
    root.mainloop()
    
if __name__ == "__main__":
  mainFormTeacher()