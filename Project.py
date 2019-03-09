from tkinter import *
from turtle import *
import tkinter.messagebox
import sqlite3
from PIL import ImageTk,Image

conn=sqlite3.connect("data2.db")
c=conn.cursor()

class Database:
    def __init__(self,master,*args,**kwargs):
        self.master=master
        #image2 =Image.open('C:\\Users\\adminp\\Desktop\\k.jpg')
        self.heading=Label(master,text="Warehouse System",bd=10,font=("forte 45 bold underline"),fg="steelblue")
        self.heading.place(x=400,y=0)
        # Create labels for the GUI...
        self.Id_l=Label(master,text="Enter Product Id",font=("chiller 18 bold"))
        self.Id_l.place(x=0,y=200)
        self.Category_l=Label(master,text="Enter Product Category",font=("chiller 18 bold"))
        self.Category_l.place(x=10,y=280)
        self.Name_l=Label(master,text="Enter Product Name",font=("chiller 18 bold"))
        self.Name_l.place(x=10,y=360)
        self.Cost_l=Label(master,text="Enter Product Cost",font=("chiller 18 bold"))
        self.Cost_l.place(x=10,y=440)
        self.Quantity_l=Label(master,text="Enter Product Quantity",font=("chiller 18 bold"))
        self.Quantity_l.place(x=10,y=520)
        # Create entries for the GUI...
        self.Id_e=Entry(master,width=30,bd=6,bg="white",font=("arial"))
        self.Id_e.place(x=300,y=200)
        self.Category_e=Entry(master,width=30,bd=6,bg="white",font=("arial"))
        self.Category_e.place(x=300,y=280)
        self.Name_e=Entry(master,width=30,bd=6,bg="white",font=("arial"))
        self.Name_e.place(x=300,y=360)
        self.Cost_e=Entry(master,width=30,bd=6,bg="white",font=("arial"))
        self.Cost_e.place(x=300,y=440)
        self.Quantity_e=Entry(master,width=30,bd=6,bg="white",font=("arial"))
        self.Quantity_e.place(x=300,y=520)
        # create button...
        self.button=Button(master,text="Submit",bd=10,command=self.get_items,width=10,font=("chiller 18 bold"),bg="snow2")
        self.button.place(x=400,y=600)
        self.sort1=Button(master,text="Sort Price",bd=10,command=self.inc_price,width=10,font=("chiller 18 bold"),bg="snow2")
        self.sort1.place(x=785,y=160)
        self.sort2=Button(master,text="Sort Cat.",bd=10,command=self.inc_cat,width=10,font=("chiller 18 bold"),bg="snow2")
        self.sort2.place(x=785,y=260)
        self.sort3=Button(master,text="Sort Qt.",bd=10,command=self.inc_qt,width=10,font=("chiller 18 bold"),bg="snow2")
        self.sort3.place(x=785,y=360)
        self.sort4=Button(master,text="Sort Price",bd=10,command=self.dec_price,width=10,font=("chiller 18 bold"),bg="snow2")
        self.sort4.place(x=785,y=460)
        self.sort5=Button(master,text="Sort Cat.",bd=10,command=self.dec_cat,width=10,font=("chiller 18 bold"),bg="snow2")
        self.sort5.place(x=785,y=560)
        self.sort6=Button(master,text="Sort Qt.",bd=10,command=self.dec_qt,width=10,font=("chiller 18 bold"),bg="snow2")
        self.sort6.place(x=785,y=660)
        # create textbox...
        self.tBox=Text(master,width=30,height=36,bd=10,bg="white",font=("chiller 18 bold"))
        self.tBox.place(x=1005,y=150)

    def get_items(self,*args,**kwargs):
        self.Id=self.Id_e.get()
        self.Category=self.Category_e.get()
        self.Name=self.Name_e.get()
        self.Cost=self.Cost_e.get()
        self.Quantity=self.Quantity_e.get()
        if self.Id=='' or self.Category=='' or self.Name=='' or self.Cost=='' or self.Quantity=='':
            tkinter.messagebox.showinfo("Error","Please Fill all the entries")
        else:

            sql="INSERT INTO inventory (Id,Category,Name,Cost,Quantity) VALUES(?,?,?,?,?)"
            c.execute(sql,(self.Id,self.Category,self.Name,self.Cost,self.Quantity))
            conn.commit()
            tkinter.messagebox.showinfo("Error","Successfully added to Database")
    def inc_price(self,*args,**kwargs):
        c.execute("SELECT * from inventory order by Cost")
        #print("Id","Category","Name","Cost","Quantity",sep="   ")

        self.tBox.delete(1.0,END)

        for row in c:
            for key in row:
                #print(key,end="      ")
                self.tBox.insert(END,key)
                self.tBox.insert(END," ")
            self.tBox.insert(END,"\n")
        self.tBox.insert(END,"\n\n")

    def inc_cat(self,*args,**kwargs):
        c.execute("SELECT * from inventory order by Category")
        #print("Id","Category","Name","Cost","Quantity",sep="   ")
        self.tBox.delete(1.0,END)
        for row in c:
            for key in row:
                #print(key,end="      ")
                self.tBox.insert(END,key)
                self.tBox.insert(END," ")
            self.tBox.insert(END,"\n")
        self.tBox.insert(END,"\n\n")

    def inc_qt(self,*args,**kwargs):
        c.execute("SELECT * from inventory order by Quantity")
    #    print("Id","Category","Name","Cost","Quantity",sep="   ")
        self.tBox.delete(1.0,END)
        for row in c:
            for key in row:
                #print(key,end="      ")
                self.tBox.insert(END,key)
                self.tBox.insert(END," ")
            self.tBox.insert(END,"\n")
        self.tBox.insert(END,"\n\n")
    def dec_price(self,*args,**kwargs):
        c.execute("SELECT * from inventory order by Cost desc")
        self.tBox.delete(1.0,END)
    #    print("Id","Category","Name","Cost","Quantity",sep="   ")
        for row in c:
            for key in row:
                #print(key,end="      ")
                self.tBox.insert(END,key)
                self.tBox.insert(END," ")
            self.tBox.insert(END,"\n")
        self.tBox.insert(END,"\n\n")
    def dec_cat(self,*args,**Kwargs):
        self.tBox.delete(1.0,END)
        c.execute("SELECT * from inventory order by Category desc")
    #    print("Id","Category","Name","Cost","Quantity",sep="   ")
        for row in c:
            for key in row:
                #print(key,end="      ")
                self.tBox.insert(END,key)
                self.tBox.insert(END," ")
            self.tBox.insert(END,"\n")
        self.tBox.insert(END,"\n\n")

    def dec_qt(self,*args,**kwargs):
         self.tBox.delete(1.0,END)
         c.execute("SELECT * from inventory order by Quantity desc")
        # print("Id","Category","Name","Cost","Quantity",sep="   ")
         for row in c:
            for key in row:
                self.tBox.insert(END,key)
                self.tBox.insert(END," ")
            self.tBox.insert(END,"\n")
         self.tBox.insert(END,"\n\n")


root=Tk()
root.title("Warehouse Management System")
#canvas1=Canvas(root,bd=6,bg="black",width=1550,height=792)

image = Image.open('k.jpg')
photo_image = ImageTk.PhotoImage(image)
label = Label(root,image = photo_image)

label.pack()
b=Database(root)


root.mainloop()
