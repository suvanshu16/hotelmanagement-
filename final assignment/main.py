from tkinter import *
from tkinter import messagebox
from items_db import Login
from customer_page import user_registration


class user_login:
    def __init__(self, window):
        self.window = window
        self.window.title("Login")

        self.mainframe = LabelFrame(self.window, width=1500, height=800)
        self.mainframe.pack()

        self.Login_user = Login()

        self.title_photo = PhotoImage(file='resep.PNG')
        self.title_photo_lable = Label(self.mainframe, image=self.title_photo, bg="white")
        self.title_photo_lable.image = self.title_photo
        self.title_photo_lable.place(x=-5, y=-5)

        self.frame1 = Frame(self.mainframe)
        self.frame1.place(x=1000, y=100, width=250, height=300)

        self.lbl_top = Label(self.mainframe, bg='#00008b', width=1500, height=2)
        self.lbl_top.place(x=0, y=0)

        self.search = Button(self.frame1, text='search', font=('arial', 10, 'bold'), bd=1, bg='#DCDCDC')
        self.search.place(x=5, y=7)

        self.details = Button(self.frame1, text='click here for\n User details', font=('arial', 10, 'bold'), bd=3
                              , bg='#DCDCDC')
        self.details.place(x=1150, y=500)

        self.lb_text = Label(self.frame1,
                             text='Use Room Number and First Name to \n authenticated the internet access ')
        self.lb_text.place(x=15, y=95)

        self.lb_text1 = Label(self.mainframe, text='Panoramic hotel  offer luxury travel experiences with '
                                                   'personalised services in elegant properties \n each individually '
                                                   'curated to reflect its location ', font=('arial', 15, 'bold'),
                              bg='#000080'
                              , fg='#F5F5F5')
        self.lb_text1.place(x=0, y=180)

        self.lb_text2 = Label(self.mainframe,
                              text='A stay at panoramic  offers  more than  just a holiday -  rather it opens'
                                   'travellers to  opportunities\n and inspiration in diverse part of the '
                                   'world ', font=('arial', 15, 'bold'), bg='#000080', fg='#F5F5F5')
        self.lb_text2.place(x=0, y=233)

        self.lb_text = Label(self.frame1, text='SIGN IN', font=('bold', 13), bg='#000080', fg='#f5f5f5', bd=2)
        self.lb_text.place(x=0, y=5, width=250, height=70)
        self.lb_username = Label(self.frame1, text='User Name', font=('arial', 10, 'bold'), fg='black')
        self.lb_username.place(x=10, y=150)
        self.ent_user = Entry(self.frame1, font=('arial', 10, 'bold'))
        self.ent_user.place(x=90, y=150)

        self.lb_password = Label(self.frame1, text='password', font=('arial', 10, 'bold'), fg='black')
        self.lb_password.place(x=10, y=200)
        self.ent_password = Entry(self.frame1, font=('arial', 10, 'bold'), show='*')
        self.ent_password.place(x=90, y=200)

        self.btn_login = Button(self.frame1, text='Login', width=30, height=1, bg='#FFD700',
                                command=self.btn_login_click)
        self.btn_login.place(x=13, y=250)


    def btn_login_click(self):
        username = self.ent_user.get()
        passwd = self.ent_password.get()

        if username == "" or passwd == "":
            messagebox.showerror('Error', 'Please Fill All Boxes')
        else:
            if self.Login_user.login_user(username, passwd):
                messagebox.showinfo('success', 'Successfully Login')
                self.window.destroy()
                user_registration(username)
            else:
                messagebox.showerror('unsuccessful', 'incorrect details ')


win = Tk()
user_login(win)
win.mainloop()