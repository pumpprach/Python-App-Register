from tkinter import *
import TeacherForm

def main():
    root = Tk()
    root.title("ระบบลงทะเบียน")
    root.geometry("300x350")
    
    Teacherimg = PhotoImage(file="C:\\Users\\User\\Pictures\\python App\\img\\teacher.png")
    Studentimg = PhotoImage(file=  "C:\\Users\\User\\Pictures\\python App\\img\\reading.png")
    Bookimg = PhotoImage(file=  "C:\\Users\\User\\Pictures\\python App\\img\\book.png")    
    Clickimg = PhotoImage(file= "C:\\Users\\User\\Pictures\\python App\\img\\click.png")
    Exitimg = PhotoImage(file= "C:\\Users\\User\\Pictures\\python App\\img\\exit.png")

    btn1 = Button(root, text="Teacher", image=Teacherimg, compound="left", width=180, height=35, command=TeacherForm.mainFormTeacher)
    btn2 = Button(root, text="Student", image= Studentimg, compound="left", width=180,height=35)
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
