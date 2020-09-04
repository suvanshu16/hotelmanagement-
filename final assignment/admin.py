
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from items_db import Register


class admin_page:
    def __init__(self, window):
        self.window = window

        self.mainframe = LabelFrame(self.window, width=1500, height=800, bg='#FAEBD7')
        self.mainframe.pack()

        self.frame = Frame(self.mainframe, bg='#FAEBD7')
        self.frame.place(x=300, y=250, width=1200, height=400)

        self.Password_value = StringVar()
        self.password = 'assignment'

        self.connction = Register()

        self.lb_password = Label(self.mainframe, text='password', font=('arial', 10, 'bold'), bg='#FAEBD7')
        self.lb_password.place(x=30, y=120)

        self.lb_admin = Label(self.mainframe, text='Admin', font=('arial', 25, 'bold'), bg='#FAEBD7')
        self.lb_admin.place(x=140, y=30)

        self.confirm = Button(self.mainframe, text='Verify', font=('arial', 10, 'bold', 'underline'), bd=1, bg='#FAEBD7'
                              , command=self.verify_btn)
        self.confirm.place(x=170, y=200)

        self.btn_back = Button(self.mainframe, text='Back', font=('bold', 13), bg='#00008b', fg='#FAEBD7', bd=2,
                               command=self.back_btn)
        self.btn_back.place(x=0, y=2)



        self.show_password()
        self.hide_password()

    def tree_v(self):
        self.item_tree = ttk.Treeview(self.frame, columns=('user_id', 'username', 'password', 'phone_no', 'email'),
                                      height=16)
        self.item_tree.place(x=20, y=0)
        self.item_tree['show'] = 'headings'
        self.item_tree.column('user_id', width=150)
        self.item_tree.column('username', width=150)
        self.item_tree.column('password', width=150)
        self.item_tree.column('phone_no', width=150)
        self.item_tree.column('email', width=250)
        self.item_tree.heading('user_id', text="user_id")
        self.item_tree.heading('username', text="username")
        self.item_tree.heading('password', text="Password")
        self.item_tree.heading('phone_no', text="Phone_no")
        self.item_tree.heading('email', text="email")

    def show_password(self):

        self.ent_show = Entry(self.mainframe, font=('arial', 10, 'bold'), textvariable=self.Password_value)
        self.ent_show.place(x=120, y=120)

        self.hide = Button(self.mainframe, text='Hide', font=('arial', 10, 'bold'), command=self.hide_password, bd=0,
                           width=5, bg='#FAEBD7')
        self.hide.place(x=280, y=120)

    def hide_password(self):

        self.ent_password = Entry(self.mainframe, font=('arial', 10, 'bold'), textvariable=self.Password_value,
                                  show="x")
        self.ent_password.place(x=120, y=120)

        self.Login = Button(self.mainframe, text='Show', font=('arial', 10, 'bold'), command=self.show_password,
                            bd=0, width=5,
                            bg='#FAEBD7')
        self.Login.place(x=280, y=120)

    def verify_btn(self):

        passwd1 = self.ent_show.get()
        passwd2 = self.ent_password.get()
        self.passwd = passwd2
        self.passwd = passwd1

        if self.password == passwd1 or self.password == passwd2:
            messagebox.showinfo('success', 'you may look the details')
            self.btn_click_verify()
            self.btn_regis = Button(self.mainframe, text='click here \nFor new registration', font=('bold', 13),
                                    bg='#FAEBD7',
                                    fg='black', bd=1, command=self.registration_btn)
            self.btn_regis.place(x=120, y=250)
        elif self.passwd == '':
            messagebox.showerror('Error', 'Password is required')

    def back_btn(self):
        self.mainframe.pack_forget()
        self.mainframe.destroy()

    def btn_click_verify(self):

        self.frame1 = Frame(self.mainframe, bg='#FAEBD7')
        self.frame1.place(x=0, y=0, width=1500, height=800)

        self.lb_search = Label(self.frame1, text='Search by username', font=('arial', 10, 'bold'), bg='#FAEBD7')
        self.lb_search.place(x=950, y=20)

        self.ent_blank = Entry(self.frame1, font=('arial', 10, 'bold'))
        self.ent_blank.place(x=1100, y=20)

        self.search = Button(self.frame1, text='Search ', font=('arial', 10, 'bold'), bg='#FAEBD7',
                             command=self.search_btn)
        self.search.place(x=1250, y=18)

        self.item_tree = ttk.Treeview(self.frame1, columns=('user_id', 'username', 'password', 'phone_no', 'email'),
                                      height=16)
        self.item_tree.place(x=400, y=250)
        self.item_tree['show'] = 'headings'
        self.item_tree.column('user_id', width=150)
        self.item_tree.column('username', width=150)
        self.item_tree.column('password', width=150)
        self.item_tree.column('phone_no', width=150)
        self.item_tree.column('email', width=250)
        self.item_tree.heading('user_id', text="user_id")
        self.item_tree.heading('username', text="username")
        self.item_tree.heading('password', text="Password")
        self.item_tree.heading('phone_no', text="Phone_no")
        self.item_tree.heading('email', text="email")

        self.btn_back = Button(self.frame1, text='Back', font=('bold', 13), bg='#FAEBD7', bd=1,
                               command=self.out_btn)
        self.btn_back.place(x=0, y=2)


    def registration_btn(self):
        import register

    def out_btn(self):
        self.frame1.destroy()

    def search_btn(self):
        u_data = []
        u_name = self.ent_blank.get()
        u_data = self.connction.extract_user_data(u_name)
        self.item_tree.delete(*self.item_tree.get_children())
        for i in u_data:
            self.item_tree.insert("", "end", text=i[0], value=(i[0], i[1], i[2], i[3], i[4]))

    # def binary_search_iterative(self, list, key):
    #     start = 0
    #     end = len(list) - 1
    #     while start <= end:
    #         mid = (start + end) // 2
    #         if list[mid][3] == key:
    #             return mid
    #         elif list[mid][3] > key:
    #             end = mid - 1
    #         else:
    #             start = mid + 1
    #     return -1
    #
    #     print(list[(binary_search_iterative(list, 'mandip1'))])



# wn = Tk()
# admin_page(wn)
# wn.mainloop()