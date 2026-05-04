from tkinter import messagebox
import tkinter as tk
import random
actually_number=random.randint(1,20)
def guess_number():
    global actually_number
    guess_number=int(e1.get())
    if guess_number>actually_number:
        messagebox.showinfo("incorrect guess","Guess lower")
    elif guess_number<actually_number:
        messagebox.showinfo("incorrect guess","Guess higher")
    else:
        messagebox.showinfo("Correct guess","you got it correct")
        
    




mainscreen=tk.Tk()
mainscreen.title("guess the number game")
mainscreen.geometry("800x800")
mainscreen.configure(bg="white")
l1=tk.Label(text="guess the number",width=30,height=2,bg="black",fg="blue")
l1.place(x=200,y=50)
l2=tk.Label(text="Enter the number",width=20,height=2,bg="black",fg="green")
l2.place(x=100,y=100)
e1=tk.Entry(width=20,bg="black",fg="yellow")
e1.place(x=400,y=100)
b1=tk.Button(text="submit",width=10,height=2,bg="black",fg="purple",command=guess_number)
b1.place(x=300,y=150)
