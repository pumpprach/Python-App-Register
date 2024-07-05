from tkinter import *
from tkinter import ttk

def calculate():
    num1 = entNumber1.get()
    num2 = entNumber2.get()
    if str(v.get()) == "1":
        result = int(num1) + int(num2)
        entTotal.insert(0,(result))
    elif str(v.get()) == "2":
        result = int(num1) - int(num2)
        entTotal.insert(0,(result))
    elif str(v.get()) == "3":
        result = int(num1) * int(num2)
        entTotal.insert(0,(result))
    elif str(v.get()) == "4":
        result = int(num1) / int(num2)
        entTotal.insert(0,(result))

def clearentry():
    entNumber1.delete(0,END)
    entNumber2.delete(0,END)
    entTotal.delete(0,END)


mainFrm = Tk()
mainFrm.title("system register")

# lblFram1
lblFram1 = ttk.LabelFrame(mainFrm, text = "ระบบคำนวณ", labelanchor = "n")
lblFram1.pack(side = "left", padx = 10, pady = 10)

lblNumber1 = ttk.Label(lblFram1, text = "Number 1")
lblNumber2 = ttk.Label(lblFram1, text = "Number 2")
lblTotal = ttk.Label(lblFram1, text = "Total")

lblNumber1.grid(column = 0, row = 2, pady = 5, sticky = "NE")
lblNumber2.grid(column = 0, row = 3, pady = 5, sticky = "NE")
lblTotal.grid(column = 0, row = 4, pady = 5, sticky = "NE")


entNumber1 = ttk.Entry(lblFram1, width=25)
entNumber1.grid(column = 1, row = 2, sticky = "NE")

entNumber2 = ttk.Entry(lblFram1, width=25)
entNumber2.grid(column = 1, row = 3, sticky = "NE")

entTotal = ttk.Entry(lblFram1, width = 25)
entTotal.grid(column = 1, row = 4, sticky = "NE")


btnClick = ttk.Button(lblFram1, text="Cal", width=10,command=calculate)
btnClear = ttk.Button(lblFram1, text="Clear", width=10, command=clearentry)


btnClick.grid(column = 0, row = 5, padx = 10, sticky = "NE")
btnClear.grid(column = 1, row = 5, padx = 10, sticky = "NE")

#lblFram2
lblFram2 = ttk.LabelFrame(mainFrm, text = "คำนวณ", labelanchor = "n")
lblFram2.pack(padx = 10, pady = 10 )

v = StringVar(lblFram2, "1")
values = {
    "บวก" : "1",
    "ลบ" : "2",
    "คูณ" : "3",
    "หาร" : "4"
}

for (text, value) in values.items():
    Radiobutton(lblFram2, text=text, variable=v, value = value).pack(side=TOP, ipady=4)
mainFrm.mainloop()
