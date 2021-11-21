import tkinter
from tkinter import*
from tkinter import messagebox
import pymysql


def main_menu():
 global screen
 screen=Tk()
 screen.geometry("300x380")
 screen.title("Welcome")
 screen.iconbitmap("user_icon.ico")

 #image= PhotoImage(file="user_icon.gif")
 #image=image.subsample (2,2)
 #label=Label(image=image)
 #label.pack()
 
 Label(text="Access to the system", bg="sea green", fg="white", width="300", height="3", font=("Calibri", 15)).pack()
 Label(text="").pack()

 Button(text="Login", font=("Courier", 10), height="3", width="20", background="dark sea green", cursor="hand2", command=login).pack()
 Label(text="").pack()

 Button(text="Sign Up", font=("Courier", 10), height="3", width="20", background="dark sea green", cursor="hand2", command=signUp).pack()

 screen.mainloop()

def login():
   global screen1
   screen1= Toplevel(screen)
   screen1.geometry("400x250")
   screen1.title("Login")
   screen1.iconbitmap("user_icon.ico")

   Label (screen1, text= "Please enter your username\n and password", bg="sea green", fg="white", width="300", height="3", font=("Calibri", 15)).pack()
   Label (screen1, text="").pack()

   global username_verify
   global userpassword_verify

   username_verify=StringVar()
   userpassword_verify=StringVar()

   global username_entry
   global userpassword_entry

   Label (screen1, text="User").pack()
   username_entry = Entry(screen1, textvariable=username_verify)
   username_entry.pack()
   Label (screen1).pack()

   Label (screen1, text="Password").pack()
   userpassword_entry = Entry(screen1, show="*", textvariable=userpassword_verify)
   userpassword_entry.pack()
   Label (screen1).pack()

   Button (screen1, text="Login", height="10", width="15", background="dark sea green", cursor="hand2", command=data_validation).pack()





def signUp():
   global screen2
   screen2= Toplevel(screen)
   screen2.geometry("400x250")
   screen2.title("Sign Up")
   screen2.iconbitmap("user_icon.ico")

   global username_entry
   global userpassword_entry

   username_entry=StringVar()
   userpassword_entry=StringVar()

   Label (screen2, text= "Please enter username and\n password of your choice", bg="sea green", fg="white", width="300", height="3", font=("Calibri", 15)).pack()
   Label (screen2, text="").pack()

   Label (screen2, text="User").pack()
   username_entry = Entry(screen2)
   username_entry.pack()
   Label (screen2).pack()

   Label (screen2, text="Password").pack()
   userpassword_entry = Entry(screen2, show="*",)
   userpassword_entry.pack()
   Label (screen2).pack()

   Button (screen2, text="Sign Up", height="10", width="15", background="dark sea green", cursor="hand2", command=insert_data).pack()



def insert_data():
   bd= pymysql.connect(
   host= "localhost",
   user= "root",
   passwd= "",
   db="pdb")

   fcursor=bd.cursor()

   sql="INSERT INTO login (user, password) VALUES ('{0}', '{1}')".format(username_entry.get(), userpassword_entry.get())

   try:               #Si se realiza la conexión con la db 
      fcursor.execute(sql)
      bd.commit()          
      messagebox.showinfo(message="Registration Success", title="Message")

   except:            #Si falla la conexión con la db 
      bd.rollback() 
      messagebox.showinfo(message="Registration Failed", title="Message")

   bd.close()


def data_validation():
   bd= pymysql.connect(
   host= "localhost",
   user= "root",
   passwd= "",
   db="pdb")

   fcursor=bd.cursor()

   fcursor.execute("SELECT password FROM login WHERE user='"+username_verify.get()+"' and password='"+userpassword_verify.get()+"'")

   if fcursor.fetchall():
      messagebox.showinfo(title="Correct Login", message="Correct user and password")

   else:
      messagebox.showinfo(title="Incorrect Login", message="Incorrect user and password")

   bd.close()




main_menu()