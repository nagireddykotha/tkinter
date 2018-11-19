

from tkinter import *
from tkinter import ttk
root = Tk()
Title1 = " APPLICATION FORM FOR THE EXAM "
Title2 = " (Last date for applying is on 31-09-2017, 23:59 hours.)\n(Applicationspost the above time will not be accepted)"
Label(root,
      text = Title1,
      fg = "Black",
      bg = "Light grey",
      font = "Arial 16 bold").grid(row=0,column=2)
Label(root,
      text = Title2,
      fg = "Black",
      font = "verdana 10 italic").grid(row=1,column=2)
var1 = StringVar()
var2 = StringVar()
Label(root,text = "Applicant's Name").grid(row=2,column=0,sticky=W)
Label(root,text = "Surname").grid(row=3,column=0,sticky=W)
Label(root,text = "Sex").grid(row=4,column=0,sticky=W)
Label(root,text = "center of exam").grid(row=5,column=0,sticky=W)
e1=Entry(root,width=100,textvariable = var1)
e2=Entry(root,width=100,textvariable = var2)
e1.grid(row=2,column=2)
e2.grid(row=3,column=2)
var3 = StringVar()
R1 = Radiobutton(root,text = "Male", variable = var3,value=1).grid(row = 4,column = 1)
R2 = Radiobutton(root,text = "Female",variable = var3,value=2).grid(row = 4,column = 2)
var4 = StringVar()
    
Test_Center = ttk.Combobox(root, textvariable = var4, state = 'readonly')
Test_Center['values'] = ['Delhi','Mumbai','Kolkata','Chennai','Bangalore','Hyderabad']
Test_Center.grid(row=5,column=1)
var = StringVar(root)
def drop_place():
    chosen_option = var.get()
    label_chosen_variable = Label(root,text = chosen_option)
    label_chosen_variable.grid(row=5,column=1)
drop_menu = OptionMenu(root,var,"Delhi","Mumbai","Kolkata","Chennai","Bengaluru","Hyderabdad",command = drop_place)
drop_menu.grid(row=5,column=1)
#def print_details():
 #   print("First Name:",var1.get())
  #  print("Surname:",var2.get())
   # print("Sex:",var3.get())
    #print("Test Center:",var4.get())
def on_exit():
    """When you click to exit, this function is called"""
    if messagebox.askyesno("Exit", "Do you want to quit the application?"):
        root.destroy()
Button(root,text="Print",command=print_details).grid(row=6,column=0)
Button(root,text="Cancel",command=on_exit).grid(row=6,column=1)
    
root.mainloop()

