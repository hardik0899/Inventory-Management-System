dic = [['Shirt',123,456,3],['Jeans',90,3456,2],['Jacket',890,678,1]]

import tkinter as tk

root = tk.Tk()

frame = tk.Frame(root)
frame.pack()
root.configure(background='black')
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.overrideredirect(1)
root.geometry("%dx%d+0+0"%(w,h))
root.focus_set()
root.bind("<Escape>",lambda e: e.widget.quit())
l1=tk.Label(frame,text="Warehouse and Inventory Management System")
l1.pack()

def press():
    arr = sorted(dic,key=lambda dic:dic[1])
    ans = 'Product_name    Quantity    Price   Category \n'
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            ans+="      "+str(arr[i][j])+"          "
        ans+='\n'
    print(ans)
    l1.config(text=ans)

def press1():
    arr = sorted(dic,key=lambda dic:dic[2])
    ans = '   Product_name     Quantity     Price       Category \n'
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            ans+="     "+str(arr[i][j])+"       "
        ans+='\n'
    print(ans)
    l1.config(text=ans)

def press2():
    arr = sorted(dic,key=lambda dic:dic[3])
    ans = '   Product_name     Quantity     Price       Category \n'
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            ans+="        "+str(arr[i][j])+"       "
        ans+='\n'
    print(ans)
    l1.config(text=ans)
def press3():
    arr = sorted(dic,key=lambda dic:dic[1],reverse=True)
    ans = '   Product_name     Quantity     Price       Category \n'
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            ans+="  "+str(arr[i][j])+"       "
        ans+='\n'
    print(ans)
    l1.config(text=ans)

def press4():
    arr = sorted(dic,key=lambda dic:dic[2],reverse=True)
    ans = '   Product_name     Quantity     Price       Category \n'
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            ans+="     "+str(arr[i][j])+"       "
        ans+='\n'
    print(ans)
    l1.config(text=ans)

def press5():
    arr = sorted(dic,key=lambda dic:dic[3],reverse=True)
    ans = '   Product_name     Quantity     Price       Category \n'
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            ans+="        "+str(arr[i][j])+"       "
        ans+='\n'
    print(ans)
    l1.config(text=ans)


button = tk.Button(frame,text="Quit",fg="red",bg="yellow",command=quit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,text="Quantity-ASC",fg="red",command=press)
slogan.pack(side=tk.LEFT)

slogan1 = tk.Button(frame,text="Price-ASC",fg="red",command=press1)
slogan1.pack(side=tk.LEFT)

slogan2 = tk.Button(frame,text="Category-ASC",fg="red",command=press2)
slogan2.pack(side=tk.LEFT)

slogan3 = tk.Button(frame,text="Quantity-DSC",fg="red",command=press3)
slogan3.pack(side=tk.LEFT)

slogan4 = tk.Button(frame,text="Price DSC",fg="red",command=press4)
slogan4.pack(side=tk.LEFT)

slogan5 = tk.Button(frame,text="Category DSC",fg="red",command=press5)
slogan5.pack(side=tk.LEFT)
root.mainloop()