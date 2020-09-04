from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from items_db import Customer
from dashboard import *


class user_registration:
    def __init__(self, username):
        self.wn = Tk()
        self.wn.geometry('1500x800')
        self.wn.resizable(0, 0)

        self.connect_db_customer = Customer()
        self.username = username

        self.lb_heading = Label(self.wn, text='Customer Registraton', font=('arial', 20, 'bold'))
        self.lb_heading.place(x=490, y=10)

        self.frame1 = Frame(self.wn)
        self.frame1.place(x=100, y=100, height=400, width=500)

        self.lb_username = Label(self.frame1, text='User Name', font=('arial', 10, 'bold'))
        self.lb_username.grid(row=0, column=1, padx=10, pady=10)
        self.ent_username = Entry(self.frame1, font=('arial', 10, 'bold'))
        self.ent_username.grid(row=0, column=2, padx=10, pady=10)

        self.lb_phone = Label(self.frame1, text='Phone.No', font=('arial', 10, 'bold'))
        self.lb_phone.grid(row=2, column=1, padx=10, pady=10)
        self.ent_pn = Entry(self.frame1, font=('arial', 10, 'bold'))
        self.ent_pn.grid(row=2, column=2, padx=10, pady=10)

        self.lb_address = Label(self.frame1, text='Address', font=('arial', 10, 'bold'))
        self.lb_address.grid(row=3, column=1, padx=10, pady=10)
        self.ent_address = Entry(self.frame1, font=('arial', 10, 'bold'))
        self.ent_address.grid(row=3, column=2, padx=10, pady=10)

        self.btn_registration = Button(self.wn, text='Register', font=('arial', 10, 'bold'), fg='black')
        self.btn_registration.place(x=400, y=480)

        self.customer_tree = ttk.Treeview(self.wn, columns=('username', 'phone_no', 'address'), height=16)
        self.customer_tree.place(x=300, y=300)
        self.customer_tree['show'] = 'headings'
        self.customer_tree.column('username', width=150)
        self.customer_tree.column('phone_no', width=150)
        self.customer_tree.column('address', width=250)
        self.customer_tree.heading('username', text="username")
        self.customer_tree.heading('phone_no', text="Phone_no")
        self.customer_tree.heading('address', text="address")

        self.add_cust = Button(self.wn, text="customer check in", command=self.add_user)
        self.add_cust.place(x=150, y=250)

        self.cust_update = Button(self.wn, text="Update customer", command=self.update_user)
        self.cust_update.place(x=450, y=670)

        self.cust_delete = Button(self.wn, text='customer check out', command=self.delete_user)
        self.cust_delete.place(x=675, y=670)

        self.dashboard = Button(self.wn, text='Dashboard', command=self.dashboard_page)
        self.dashboard.place(x=800, y=250)

        self.show_customer_tree()
        self.wn.mainloop()

    def add_user(self):
        name = self.ent_username.get()
        contact = self.ent_pn.get()
        address = self.ent_address.get()
        if self.validate():
            if self.connect_db_customer.add_customer(name, contact, address):
                messagebox.showinfo('user', "customer Added")
                self.show_customer_tree()
            else:
                messagebox.showerror("Error", self.connect_db_customer.add_customer(name, contact, address))

    def update_user(self):
        try:
            if self.update_index == "":
                messagebox.showerror("Error", "Please select a row first")
            else:
                name = self.ent_username.get()
                contact = self.ent_pn.get()
                address = self.ent_address.get()
                if self.connect_db_customer.update_customer(self.update_index, name, contact, address):
                    messagebox.showinfo('user', "information  Updated")
                    self.show_customer_tree()
                    self.update_index = ""
                    self.ent_username.delete(0, END)
                    self.ent_pn.delete(0, END)
                    self.ent_address.delete(0, END)

        except AttributeError:
                messagebox.showerror("Error", 'Can not be updated !!!')

    def delete_user(self):
        try:
            if self.update_index == '':
                messagebox.showerror('Error', 'select the item u want to cancel')
            else:
                if self.connect_db_customer.delete_customer(self.update_index):
                    messagebox.showinfo('success', 'successfully deleted')
                    self.show_customer_tree()
                    self.update_index= ''
        except AttributeError:
            messagebox.showerror('Error', 'double click to select')

    def validate(self):
        name = self.ent_username.get()
        contact = self.ent_pn.get()
        address = self.ent_address.get()
        if name == '' or contact == '' or address == '':
            messagebox.showerror('Error', 'Fill all the fields')
            return False
        elif not contact.isdigit():
            messagebox.showerror('Error', 'Invalid value for rate')
            return False
        else:
            return True

    def show_customer_tree(self):
        self.customer_tree.delete(*self.customer_tree.get_children())
        data = self.connect_db_customer.show_customer()
        for i in data:
            self.customer_tree.insert('', 'end', text=i[0], values=(i[1], i[2], i[3]))
        self.customer_tree.bind("<Double-1>", self.on_item_select)

    def on_item_select(self, event):
        selected_row = self.customer_tree.selection()[0]
        selected_item = self.customer_tree.item(selected_row, 'values')
        self.update_index = self.customer_tree.item(selected_row, 'text')
        self.ent_username.delete(0, END)
        self.ent_username.insert(0, selected_item[0])
        self.ent_pn.delete(0, END)
        self.ent_pn.insert(0, selected_item[1])
        self.ent_address.delete(0, END)
        self.ent_address.insert(0, selected_item[2])

    def dashboard_page(self):
        self.wn.destroy()
        from dashboard import main_page
        main_page(self.username)


# user_registration('text')