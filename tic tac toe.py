import tkinter as tk
from tkinter import messagebox
current_turn="X"
turns=0
def tictactoe(buttonid):
    global current_turn,turns
    buttonid.config(text=current_turn)
    buttonid.config(state="disabled")
    if b1.cget("text")==b2.cget("text")==b3.cget("text")!="":
        messagebox.showinfo("You won","You won "+current_turn)
        win()
    if b1.cget("text")==b2.cget("text")==b3.cget("text")!="":
        messagebox.showinfo("You won","You won "+current_turn)
        win()
    if b7.cget("text")==b8.cget("text")==b9.cget("text")!="":
        messagebox.showinfo("You won","You won "+current_turn)
        win()
    if b1.cget("text")==b5.cget("text")==b9.cget("text")!="":
        messagebox.showinfo("You won","You won "+current_turn)
        win()
    if b3.cget("text")==b5.cget("text")==b7.cget("text")!="":
        messagebox.showinfo("You won","You won "+current_turn)
        win()
    if b1.cget("text")==b4.cget("text")==b7.cget("text")!="":
        messagebox.showinfo("You won","You won "+current_turn)
        win()
    if b2.cget("text")==b5.cget("text")==b8.cget("text")!="":
        messagebox.showinfo("You won","You won "+current_turn)
        win()
    if b3.cget("text")==b6.cget("text")==b9.cget("text")!="":
        messagebox.showinfo("You won","You won "+current_turn)
        win()
    if current_turn=="X":
        current_turn="O"
    else:
        current_turn="X"
    l2.config(text="turn: "+current_turn)
def win():
    b1.config(state="disabled")
    b2.config(state="disabled")
    b3.config(state="disabled")
    b4.config(state="disabled")
    b5.config(state="disabled")
    b6.config(state="disabled")
    b7.config(state="disabled")
    b8.config(state="disabled")
    b9.config(state="disabled")

def restartgame():
    b1.config(state="normal")
    b2.config(state="normal")
    b3.config(state="normal")
    b4.config(state="normal")
    b5.config(state="normal")
    b6.config(state="normal")
    b7.config(state="normal")
    b8.config(state="normal")
    b9.config(state="normal")
    b1.config(text="")
    b2.config(text="")
    b3.config(text="")
    b4.config(text="")
    b5.config(text="")
    b6.config(text="")
    b7.config(text="")
    b8.config(text="")
    b9.config(text="")

mainscreen=tk.Tk()
mainscreen.title("tic tac toe")
mainscreen.geometry("600x600")
mainscreen.configure(bg="white")
l1=tk.Label(text="Welcome to tic tac toe",width=30,height=2,bg="black",fg="blue")
l1.place(x=200,y=50)
b1=tk.Button(width=10,height=5,bg="grey",fg="black",command=lambda: tictactoe(b1))
b1.place(x=100,y=110)
b2=tk.Button(width=10,height=5,bg="grey",fg="black",command=lambda: tictactoe(b2))
b2.place(x=225,y=110)
b3=tk.Button(width=10,height=5,bg="grey",fg="black",command=lambda: tictactoe(b3))
b3.place(x=350,y=110)
b4=tk.Button(width=10,height=5,bg="grey",fg="black",command=lambda: tictactoe(b4))
b4.place(x=100,y=210)
b5=tk.Button(width=10,height=5,bg="grey",fg="black",command=lambda: tictactoe(b5))
b5.place(x=225,y=210)
b6=tk.Button(width=10,height=5,bg="grey",fg="black",command=lambda: tictactoe(b6))
b6.place(x=350,y=210)
b7=tk.Button(width=10,height=5,bg="grey",fg="black",command=lambda: tictactoe(b7))
b7.place(x=100,y=310)
b8=tk.Button(width=10,height=5,bg="grey",fg="black",command=lambda: tictactoe(b8))
b8.place(x=225,y=310)
b9=tk.Button(width=10,height=5,bg="grey",fg="black",command=lambda: tictactoe(b9))
b9.place(x=350,y=310)
b10=tk.Button(text="restart",width=5,height=4,bg="grey",fg="black",command=restartgame)
b10.place(x=250,y=400)
l2=tk.Label(text="turn",width=15,height=3,bg="grey",fg="black")
l2.place(x=250,y=500)










