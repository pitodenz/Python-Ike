import tkinter as tk
import datetime

def show_time():
    x=datetime.datetime.now()
    a=x.strftime("%H:%M:%S")
    l2.config(text=a)
    l2.after(1000,show_time)
    
def show_date():
    x=datetime.datetime.now()
    a=x.strftime("%d/%b/%Y")
    l3.config(text=a)
    
    
    


mainscreen=tk.Tk()
mainscreen.title("digital clock")
mainscreen.configure(bg="white")
mainscreen.geometry("600x600")
l1=tk.Label(text="digital clock",width=15,height=2,bg="black",fg="blue")
l1.place(x=200,y=50)
b1=tk.Button(text="show time",width=15,height=2,bg="black",fg="yellow",command=show_time)
b1.place(x=200,y=150)
l2=tk.Label(text="",width=20,height=2,bg="black",fg="red")
l2.place(x=200,y=200)
b2=tk.Button(text="show date",width=15,height=2,bg="black",fg="green",command=show_date)
b2.place(x=200,y=250)
l3=tk.Label(text="",width=15,height=2,bg="black",fg="orange")
l3.place(x=200,y=300)


                 
