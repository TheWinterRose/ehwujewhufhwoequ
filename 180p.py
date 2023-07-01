from tkinter import*
from tkinter import ttk
import Translator,LANGUAGES
root=Tk()
root.geometry("470x470")
root.config(bg="moccasin")
l=Label(root,text="LANGUAGE TRANSLATOR",bg="moccasin",font=("Bahnschrift Light",16,"bold"))
l.place(relx=0.5,rely=0.1,anchor=CENTER)
l2=Label(root,text="Enter Text",bg="moccasin",font=("Bahnschrift Light",12,"bold"))
l2.place(relx=0.5,rely=0.7,anchor=W)
t=Text(root,bg="moccasin",font='arial 10',height=11,wrap=WORD,width=60,padx=10,pady=10,bd=0)
t.place(relx=0.5,rely=0.9,anchor=W)
root.mainloop()