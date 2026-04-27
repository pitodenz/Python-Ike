import tkinter as tk

def convert():
    kilogram=int(e1.get())
    grams=kilogram*1000
    pounds=kilogram*2.25
    ounces=kilogram*35.27
    l2.config(text=str(grams)+"grams")
    l3.config(text=str(pounds)+"pounds")
    l4.config(text=str(ounces)+"ounces")
    

mainscreen=tk.Tk()
mainscreen.title("my second screen")
mainscreen.configure(bg="red")
mainscreen.geometry("800x800")
l1=tk.Label(text="enter your weight in kg",width=25,height=2,bg="black",fg="red")
l1.place(x=50,y=100)
e1=tk.Entry(width=30,bg="black",fg="blue")
e1.place(x=300,y=100)
l2=tk.Label(text="in grams",width=15,height=2,bg="black",fg="yellow")
l2.place(x=100,y=200)
l3=tk.Label(text="in pounds",width=15,height=2,bg="black",fg="white")
l3.place(x=340,y=200)
l4=tk.Label(text="in ounces",width=25,height=2,bg="black",fg="orange")
l4.place(x=600,y=200)
b1=tk.Button(text="Convert",width=15,height=2,bg="black",fg="purple",command=convert)
b1.place(x=250,y=350)


mainscreen.mainloop()
         
