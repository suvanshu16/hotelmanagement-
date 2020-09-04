from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from items_db import *


class billing:
    def __init__(self, username):
        self.wn = Tk()
        self.wn.title("Bill")
        self.wn.geometry('1700x900')
        self.wn.resizable(0, 0)

        self.username = username
        self.connect_login = Login()
        self.connect_bar = Drinks()
        self.connect_rest = Item()
        self.connect_customer = Customer()
        self.connect_tables = connect_table()

        self.mainframe = LabelFrame(self.wn, width=1700, height=900, bg='#FAEBD7')
        self.mainframe.pack()

        self.frame = Frame(self.mainframe, bg='#FAEBD7')
        self.frame.place(x=150, y=450, width=1350, height=400)

        self.frame1 = Frame(self.mainframe, bg='#FAEBD7')
        self.frame1.place(x=1050, y=30, width=550, height=400)

        self.lb_bill = LabelFrame(self.mainframe, text='Bill', font=('arial', 10, 'italic'), bg='#FAEBD7', height=450,
                                  width=650, bd=7)
        self.lb_bill.place(x=100, y=350)

        lb_c_contact = Label(self.mainframe, text='contact:', font=('arial', 15, 'italic'), bg='#FAEBD7').place(x=300, y=230)
        lb_c_address = Label(self.mainframe, text='address:', font=('arial', 15, 'italic'), bg='#FAEBD7').place(x=300, y=270)
        self.c_contact = Label(self.mainframe, font=('arial', 15, 'italic'), bg='#FAEBD7')
        self.c_contact.place(x=450, y=230)
        self.c_address = Label(self.mainframe, font=('arial', 15, 'italic'), bg='#FAEBD7')
        self.c_address.place(x=450, y=270)

        #---------------------------calculator-----------------------------------

        self.button_1 = Button(self.frame1, text='1', padx=40, pady=20, width=2,
                               font=('arial', 14, 'bold', 'italic'), command=lambda: self.button_click(1), bd=3)
        self.button_1.grid(row=3, column=0)
        self.button_2 = Button(self.frame1, text='2', padx=40, pady=20, width=2,
                               font=('arial', 14, 'bold', 'italic'), command=lambda: self.button_click(2), bd=3)
        self.button_2.grid(row=3, column=1)
        self.button_3 = Button(self.frame1, text='3', padx=40, pady=20, width=2,
                               font=('arial', 14, 'bold', 'italic'), command=lambda: self.button_click(3), bd=3)
        self.button_3.grid(row=3, column=2)
        self.button_4 = Button(self.frame1, text='4', padx=40, pady=20, width=2,
                               font=('arial', 14, 'bold', 'italic'), command=lambda: self.button_click(4), bd=3)
        self.button_4.grid(row=2, column=0)
        self.button_5 = Button(self.frame1, text='5', padx=40, pady=20, width=2,
                               font=('arial', 14, 'bold', 'italic'), command=lambda: self.button_click(5), bd=3)
        self.button_5.grid(row=2, column=1)
        self.button_6 = Button(self.frame1, text='6', padx=40, pady=20, width=2,
                               font=('arial', 14, 'bold', 'italic'), command=lambda: self.button_click(6), bd=3)
        self.button_6.grid(row=2, column=2)
        self.button_7 = Button(self.frame1, text='7', padx=40, pady=20, width=2,
                               font=('arial', 14, 'bold', 'italic'), command=lambda: self.button_click(7), bd=3)
        self.button_7.grid(row=1, column=0)
        self.button_8 = Button(self.frame1, text='8', padx=40, pady=20, width=2,
                               font=('arial', 14, 'bold', 'italic'), command=lambda: self.button_click(8), bd=3)
        self.button_8.grid(row=1, column=1)
        self.button_9 = Button(self.frame1, text='9', padx=40, pady=20, width=2,
                               font=('arial', 14, 'bold', 'italic'), command=lambda: self.button_click(9), bd=3)
        self.button_9.grid(row=1, column=2)
        self.button_0 = Button(self.frame1, text='0', padx=40, pady=20, width=2,
                               font=('arial', 14, 'bold', 'italic'), command=lambda: self.button_click(0), bd=3)
        self.button_0.grid(row=4, column=1)
        self.button_adde = Button(self.frame1, text='+', padx=40, pady=20, width=2,
                                  font=('arial', 14, 'bold', 'italic'), command=self.button_add, bd=3)
        self.button_adde.grid(row=1, column=3)
        self.button_subt = Button(self.frame1, text='-', padx=40, pady=20, width=2,
                                  font=('arial', 14, 'bold', 'italic'), command=self.button_subtract, bd=3)
        self.button_subt.grid(row=2, column=3)
        self.button_multi = Button(self.frame1, text='*', padx=40, pady=20, width=2,
                                   font=('arial', 14, 'bold', 'italic'), command=self.button_multiply, bd=3)
        self.button_multi.grid(row=3, column=3)
        self.button_dvd = Button(self.frame1, text='/', padx=40, pady=20, width=2,
                                 font=('arial', 14, 'bold', 'italic'), command=self.button_devide, bd=3)
        self.button_dvd.grid(row=4, column=2)
        self.button_clean = Button(self.frame1, text='C', padx=40, pady=20, width=2,
                                   font=('arial', 14, 'bold', 'italic'), command=self.button_clear, bd=3)
        self.button_clean.grid(row=4, column=0)
        self.button_equal_to = Button(self.frame1, text='=', padx=40, pady=20, width=2,
                                      font=('arial', 14, 'bold', 'italic'), command=self.button_eqal, bd=3)
        self.button_equal_to.grid(row=4, column=3)
        self.ent_dispaly = Entry(self.frame1, width=34, bd=5, font=('arial', 20, 'bold', 'italic'),
                                 justify=RIGHT)
        self.ent_dispaly.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        self.lb_search = Label(self.mainframe, text='Add customers username', font=('arial', 10, 'bold'), bg='#FAEBD7')
        self.lb_search.place(x=220, y=150)

        # self.ent_customer = Entry(self.mainframe, font=('arial', 10, 'bold'))
        # self.ent_customer.place(x=400, y=150)

        self.search = Button(self.mainframe, text='Search ', font=('arial', 10, 'bold'), bg='#FAEBD7',
                             command=self.search_btn)
        self.search.place(x=650, y=145)

        self.combo_Name = ttk.Combobox(self.wn, font=('arial', 15, 'bold'))
        self.combo_Name.place(x=400, y=150)

        self.combobox_data_customer_name()

        self.tree_v()
        self.wn.mainloop()

    def combobox_data_customer_name(self):
        customer_name = []
        data = self.connect_customer.show_customer()
        for i in range(len(data)):
            customer_name.append(data[i][1])
        customer_name.sort()
        self.combo_Name['values'] = customer_name

    def tree_v(self):
        self.bill_tree = ttk.Treeview(self.lb_bill, columns=('Purchased_item', 'Price'), height=18)
        self.bill_tree.place(x=50, y=10)
        self.bill_tree['show'] = 'headings'
        self.bill_tree.column('Purchased_item', width=250)
        self.bill_tree.column('Price', width=250)
        self.bill_tree.heading('Purchased_item', text="Purchased_item")
        self.bill_tree.heading('Price', text="Price")

    def show_in_tree(self):
        u_name = self.combo_Name.get()
        self.bill_tree.delete(*self.bill_tree.get_children())
        ls_data = []
        u_data = self.connect_customer.search_customer_name(u_name)
        u_id = str(u_data[0][0])
        data_item = self.connect_rest.search_item_uid(u_id)
        data_bar = self.connect_tables.connect_customer_bar(u_name)
        # customer_contact = data_bar[0][6]
        # customer_address = data_bar[0][7]
        # self.c_contact.config(text=customer_contact)
        # self.c_address.config(text=customer_address)
        for i in range(len(data_item)):
            item_name = data_item[i][1]
            item_type = data_item[i][2]
            item_rate = data_item[i][3]
            item = (item_name, item_type)
            ls_data.append((item, item_rate))

        for i in range(len(data_bar)):
            drinks_name = data_bar[i][1]
            drinks_rate = data_bar[i][2]
            ls_data.append((drinks_name, drinks_rate))

        for i in ls_data:
            self.bill_tree.insert('', 'end', text=i[0], value=(i[0], i[1]))

    def search_btn(self):
        self.binary_search()
        self.show_in_tree()

    def button_click(self, number):
        self.current = self.ent_dispaly.get()
        self.ent_dispaly.delete(0, END)
        self.ent_dispaly.insert(0, str(self.current) + str(number))

    def button_clear(self):
        self.current = 0
        self.second_number = 0
        self.ent_dispaly.delete(0, END)

    def button_add(self):
        try:
            first_number = self.ent_dispaly.get()
            global f_num
            global math
            math = "addition"
            f_num = float(first_number)
            self.ent_dispaly.delete(0, END)
        except ValueError:
            messagebox.showerror('Error', 'Incorrect Input')

    def button_subtract(self):
        try:
            first_number = self.ent_dispaly.get()
            global f_num
            global math
            math = "subtraction"
            f_num = float(first_number)
            self.ent_dispaly.delete(0, END)
        except ValueError:
            messagebox.showerror('Error', 'Incorrect Input')

    def button_multiply(self):
        try:
            first_number = self.ent_dispaly.get()
            global f_num
            global math
            math = "multiplication"
            f_num = float(first_number)
            self.ent_dispaly.delete(0, END)
        except ValueError:
            messagebox.showerror('Error', 'Incorrect Input')

    def button_devide(self):
        try:
            first_number = self.ent_dispaly.get()
            global f_num
            global math
            math = "division"
            f_num = float(first_number)
            self.ent_dispaly.delete(0, END)
        except ValueError:
            messagebox.showerror('Error', 'Incorrect Input')

    def button_eqal(self):
        try:
            self.second_number = self.ent_dispaly.get()
            self.ent_dispaly.delete(0, END)
            if math == "addition":
                self.ent_dispaly.insert(0, f_num + float(self.second_number))
            if math == "subtraction":
                self.ent_dispaly.insert(0, f_num - float(self.second_number))
            if math == "multiplication":
                self.ent_dispaly.insert(0, f_num * float(self.second_number))
            if math == "division":
                self.ent_dispaly.insert(0, f_num / float(self.second_number))
        except ValueError:
            messagebox.showerror('Error', 'Incorrect Input')
        except NameError:
            messagebox.showerror('Error', 'Incorrect Input')


    def binary_search(self):
        username = self.combo_Name.get()
        list = self.connect_customer.show_customer_orderby()
        search = list[(self.binary_search_iterative(list, username))]
        contact = search[2]
        address = search[3]
        self.c_contact.config(text=contact)
        self.c_address.config(text=address)

    def binary_search_iterative(self, list, key):
        start = 0
        end = len(list) - 1
        while start <= end:
            mid = (start + end) // 2
            if list[mid][1] == key:
                return mid
            elif list[mid][1] > key:
                end = mid - 1
            else:
                start = mid + 1
        return -1


# billing('')
