import tkinter as tk
from tkinter import messagebox
def show_message():
    messagebox.showinfo("saved","Your details have been saved")
    

mainscreen=tk.Tk()
mainscreen.title("My first Screen")
mainscreen.configure(bg="blue")
mainscreen.geometry("600x600")
l1=tk.Label(text="Welcome to my screen",width=30,height=2,bg="black",fg="white")
l1.place(x=200,y=20)
l2=tk.Label(text="Enter your name",width=25,height=2,bg="black",fg="yellow")
l2.place(x=50,y=80)
e1=tk.Entry(width=30,bg="white",fg="Black")
e1.place(x=300,y=80)
l3=tk.Label(text="Enter your age",width=25,height=2,bg="black",fg="brown")
l3.place(x=60,y=140)
e2=tk.Entry(width=25,bg="white",fg="Black")
e2.place(x=300,y=140)
b1=tk.Button(text="Submit",width=15,height=1,bg="black",fg="blue",command=show_message)
b1.place(x=250,y=450)
r1=tk.Radiobutton(text="female",value=1)
r1.place(x=100,y=200)
r2=tk.Radiobutton(text="Male",value=2)
r2.place(x=250,y=200)
l4=tk.Label(text="Select your hobbies",width=25,height=2,bg="black",fg="orange")
l4.place(x=60,y=260)
c1=tk.Checkbutton(text="Coding",onvalue=1,offvalue=0)
c1.place(x=300,y=260)
c2=tk.Checkbutton(text="Gaming",onvalue=1,offvalue=0)
c2.place(x=420,y=260)
lb1=tk.Listbox(width=20, height=5,bg="black",fg="cyan")
lb1.place(x=200,y=320)
languages=["French","English","Chinese","Polish","Russian","Hindi"]
n=1
for i in languages:
    lb1.insert(n,i)
    n=n+1
l5=tk.Label(text="How old are you",width=30,height=2,bg="black",fg="purple")
l5.place(x=150,y=380)
e3=tk.Entry(width=30,height=2,bg="black",fg="dark blue")
e3.place(x=200,y=380)
mainscreen.mainloop()
