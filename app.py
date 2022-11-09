from tkinter import *
from tkinter import ttk
import os
import subprocess
from PIL import *
import PIL.Image
from PIL import ImageTk
import tkinter.messagebox as mbox
import time
# Designing window for registration
 
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")
 
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
 
    Label(register_screen, text="Please enter details below", bg="blue").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command = register_user).pack()
 
 
# Designing window for login 
 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()
 
# Implementing event on register button
 
def register_user():
 
    username_info = username.get()
    password_info = password.get()
 
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
 
    username_entry.delete(0, END)
    password_entry.delete(0, END)
 
    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
 
# Implementing event on login button 
 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
 
        else:
            password_not_recognised()
 
    else:
        user_not_found()
 
# Designing popup for login success
 
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()
 
# Designing popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 
# Deleting popups
 
def delete_login_success():
    main_screen.destroy()
    root = Toplevel()
    root.geometry("500x500")
    root.title("OTESL")
    image1 = PIL.Image.open("HHTCOJ.png")
    resize_image = image1.resize((100, 50))
    new_image= ImageTk.PhotoImage(resize_image)
    label1 = ttk.Label(root,image=new_image)
    label1.image = new_image
    label1.place(x=0, y=0)
    title_1= Label(root,text="OTESL",font=25)
    title_2 = Label(root,text="Name of websites:",font=20)
    title_1.place(x=225,y=0)
    title_2.place(x=0,y=40)
    entry= Entry(root, width= 40)
    entry.focus_set()
    entry.place(x=150,y=60)
    def get_value():
        text= entry.get()
        print(text)
    ttk.Button(root, text= "Xac Nhan",width= 8,command=get_value).place(x=400,y=85)
    title_3 = Label(root,text="Picture of websites:",font=20)
    title_3.place(x=0,y=120)
    entry2= Entry(root, width= 40)
    entry2.focus_set()
    entry2.place(x=150,y=150)
    def get_value():
        text= entry.get()
        print(text)
    ttk.Button(root, text= "Xac Nhan",width= 8,command=get_value).place(x=400,y=180)    
    frame = Frame(root)
    frame.place(x=200,y=250)
    Label(frame, text="Tinh nang:").grid(row=0,padx=0,pady=0)
    var1 = IntVar()
    Checkbutton(frame, text="Cham bai", variable=var1).grid(row=1, sticky=W)
    var2 = IntVar()
    Checkbutton(frame, text="User", variable=var2).grid(row=2, sticky=W)
    var3 = IntVar()
    Checkbutton(frame, text="Toan", variable=var3).grid(row=3, sticky=W)
    var4 = IntVar()
    Checkbutton(frame, text="Tin", variable=var4).grid(row=4, sticky=W)
    btn = Button(frame, text = 'xac nhan',command = root.destroy)
    btn.grid(row=5)
    def mebox():
        root.destroy()
        def ket_noi():
            os.system("gnome-terminal -e 'bash -c \"sudo lsof -i tcp:80; exec bash\"'")
        def ket_noi_2():
            os.system("gnome-terminal -e 'bash -c \"sudo lsof -t -i tcp:80 -s tcp:listen | sudo xargs kill; exec bash\"'")
        def ket_noi_3():
            os.system("gnome-terminal -e 'bash -c \"sudo docker-compose up -d; exec bash\"'")
        def ket_noi_4():
            os.system("gnome-terminal -e 'bash -c \"ifconfig; exec bash\"'")
            root2.destroy()
            root3 = Toplevel()
            root3.geometry("400x400")
            t1 = Label(root3,text="chuc mung ban da thiet lap thanh cong",font=10).grid(row=0)
            t2 = Label(root3,text="dia chi trang web cua ban o dong  Docker 0: inet:___",font=10).grid(row=1) 
            
             

        mbox.askokcancel(title="xac nhan thiet lap websites",message="hay dam bao cac tinh nang da duoc chon!!")
        root2 = Toplevel()
        root2.geometry("400x400")
        title_1= Label(root2,text="Dang thuc thi qua trinh se yeu cau mat khau root cua nguoi dung",font=15).grid(row=0)
        title_2= Label(root2,text="Buoc 1: Xac dinh port 80",font=15).grid(row=1)
        nut_1= Button(root2,text="xac nhan",command=ket_noi).grid(row=2)
        title_2= Label(root2,text="Buoc 2: kill port 80",font=15).grid(row=3)
        nut_2= Button(root2,text="xac nhan",command=ket_noi_2).grid(row=4)
        title_3= Label(root2,text="Buoc 3: truy cap quyen root, Thu muc, Pull Image",font=15).grid(row=5)
        nut_3= Button(root2,text="xac nhan",command=ket_noi_3).grid(row=6)
        title_4= Label(root2,text="Buoc 4: lay dia chi trang website",font=15).grid(row=7)
        nut_4= Button(root2,text="xac nhan",command=ket_noi_4).grid(row=8)
        
    btn2 = Button(root, text = 'thiet lap websites',command = mebox).place(x=350,y=450)
    root.mainloop()
     

 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
 
 
# Designing Main(first) window
 
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command = login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()
 
    main_screen.mainloop()
 
 
main_account_screen()