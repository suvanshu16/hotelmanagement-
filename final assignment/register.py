from tkinter import *
from tkinter import messagebox
from items_db import Register


class user_registration:
    def __init__(self):
        self.wn = Tk()
        self.wn.title("registration")
        self.wn.geometry('800x700')
        self.wn.resizable(0, 0)

        self.reg = Register()

        self.lb_heading = Label(self.wn, text='Sign UP', font=('arial', 20, 'bold'))
        self.lb_heading.place(x=390, y=10)

        self.frame1 = Frame(self.wn)
        self.frame1.place(x=240, y=250, height=400, width=500)

        self.lb_username = Label(self.frame1, text='User Name', font=('arial', 10, 'bold'))
        self.lb_username.grid(row=0, column=1, padx=10, pady=10)
        self.ent_username = Entry(self.frame1, font=('arial', 10, 'bold'))
        self.ent_username.grid(row=0, column=2, padx=10, pady=10)

        self.lb_password = Label(self.frame1, text='password', font=('arial', 10, 'bold'))
        self.lb_password.grid(row=1, column=1, padx=10, pady=10)
        self.ent_pass = Entry(self.frame1, font=('arial', 10, 'bold'), show='*')
        self.ent_pass.grid(row=1, column=2, padx=10, pady=10)

        self.lb_phone = Label(self.frame1, text='Phone.No', font=('arial', 10, 'bold'))
        self.lb_phone.grid(row=2, column=1, padx=10, pady=10)
        self.ent_pn = Entry(self.frame1, font=('arial', 10, 'bold'))
        self.ent_pn.grid(row=2, column=2, padx=10, pady=10)

        self.lb_Email = Label(self.frame1, text='Email address', font=('arial', 10, 'bold'))
        self.lb_Email.grid(row=3, column=1, padx=10, pady=10)
        self.ent_email = Entry(self.frame1, font=('arial', 10, 'bold'))
        self.ent_email.grid(row=3, column=2, padx=10, pady=10)

        self.btn_registration = Button(self.wn, text='Register', font=('arial', 10, 'bold'), fg='black',
                                       command=self.btn_register_click)
        self.btn_registration.place(x=400, y=480)

        self.lb_text0 = Label(self.frame1, text='eg:-  ........@gmail.com ', font=('arial', 10, 'bold'))
        self.lb_text0.place(x=290, y=138)

        self.wn.mainloop()

    def btn_register_click(self):
        user_name = self.ent_username.get()
        password = self.ent_pass.get()
        phone_no = self.ent_pn.get()
        email = self.ent_email.get()

        if user_name == '' or password == '' or phone_no == '' or email == '':
            messagebox.showerror('Error', 'Fill all the blanks')
        elif not phone_no.isdigit():
            messagebox.showerror('Error', 'Invalid value for phone number')
        else:
            if self.reg.add_user(user_name, password, phone_no, email):

                messagebox.showinfo('Sucess', 'Successfully registered')
                self.wn.destroy()
            else:
                messagebox.showerror('Error', 'sry ')


user_registration()