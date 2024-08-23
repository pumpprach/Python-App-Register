from tkinter import *
import TeacherForm
import StudentForm

def main():

    def open_form():
        root.withdraw()
        TeacherForm.mainFormTeacher(root)

    root = Tk()
    root.title("Registration system")
    root.geometry("300x350")
    
    Teacherimg = PhotoImage(file="C:\\ummm\\D1\\img\\teacher.png")
    Studentimg = PhotoImage(file="C:\\ummm\\D1\\img\\reading.png")
    Bookimg = PhotoImage(file="C:\\ummm\\D1\\img\\book.png")    
    Clickimg = PhotoImage(file="C:\\ummm\\D1\\img\\click.png")
    Exitimg = PhotoImage(file="C:\\ummm\\D1\\img\\exit.png")

    btn1 = Button(root, text="Teacher", image=Teacherimg, compound="left", width=180, height=35, command=open_form)
    btn2 = Button(root, text="Student", image= Studentimg, compound="left", width=180,height=35, command=open_form)
    btn3 = Button(root, text="Subject", image= Bookimg, compound="left", width=180,height=35)
    btn4 = Button(root, text="Register", image= Clickimg, compound="left",width=180,height=35)
    btn5 = Button(root, text="Exit", image= Exitimg, compound="left", width=180,height=35)

    btn1.pack(pady=10)
    btn2.pack(pady=10)
    btn3.pack(pady=10)
    btn4.pack(pady=10)
    btn5.pack(pady=10)

    
    
    root.mainloop()
    
if __name__ ==  "__main__" :
    main()