from tkinter import * 
root=Tk()
root.geometry("655x333")
f2 = Frame(root,borderwidth=8,bg="grey")
f2.pack(side=TOP,fill="x")
f1=Frame(root,bg="grey",borderwidth=6)

f1.pack(side=LEFT,fill="y")

l=Label(f1,text="Projet Tkinter- sample")
l.pack(pady=42)
l=Label(f2,text="welcome to text",font= "Helvetica 16 bold",fg="red")
l.pack()

root.mainloop()