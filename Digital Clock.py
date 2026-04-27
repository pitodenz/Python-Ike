import tkinter as tk
import datetime
def showtime():
    x=datetime.datetime.now()
    a=x.strftime("%H:%M:%S")
    l2.config(text=a)
    l2.after(1000,showtime)
mainscreen=tk.Tk()
mainscreen.title("Digital Clock")
mainscreen.configure(bg="red")
mainscreen.geometry("600x600")
l1=tk.Label(text="digital clock",width=15,height=2,bg="white",fg="black")
l1.place(x=200,y=50)
b1=tk.Button(text="Show time",width=15,height=2,bg="white",fg="black",command=showtime)
b1.place(x=200,y=100)
l2=tk.Label(text="",width=20,height=2,bg="white",fg="black")
l2.place(x=200,y=200)
mainscreen.mainloop()
