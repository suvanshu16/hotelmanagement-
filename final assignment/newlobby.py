
from tkinter import *
import tkinter.messagebox
from tkinter import messagebox
from tkinter import ttk
from items_db import *


class lobby_page:
    def __init__(self, window, username):
        self.wn = window
        self.wn.title('Welcome')
        self.wn.geometry('1500x800')
        self.wn.config(bg='#FAEBD7')
        self.wn.resizable(0, 0)

        self.frame0 = Frame(self.wn)
        self.frame0.place(x=50, y=70, width=1400, height=600)

        self.item = Item()
        self.drinks = Drinks()
        self.connect_login = Login()
        self.username = username
        self.connect_customer = Customer()
        self.show_menu()

        self.combo_Name = ttk.Combobox(self.wn, font=('arial', 15, 'bold'))
        self.combo_Name.place(x=1050, y=20)

        self.combobox_data_customer_name()

    def combobox_data_customer_name(self):
        customer_name = []
        data = self.connect_customer.show_customer()
        for i in range(len(data)):
            customer_name.append(data[i][1])
        customer_name.sort()
        self.combo_Name['values'] = customer_name

    def show_menu(self):
        my_menu = Menu(self.wn)
        self.wn.config(menu=my_menu)
        hotel_menu = Menu(my_menu)
        my_menu.add_cascade(label="Room service", command=self.room_serv)

        rest_menu = Menu(my_menu, tearoff=False)
        my_menu.add_cascade(label="Babrage", menu=rest_menu)
        rest_menu.add_cascade(label='Restaurant', command=self.rest_btn)
        rest_menu.add_cascade(label="Bar", command=self.bar_btn)

        bill_menu = Menu(my_menu, tearoff=False)
        my_menu.add_cascade(label='Bill', menu=bill_menu)
        bill_menu.add_cascade(label='Show', command=self.bil_btn)

        exit_menu = Menu(my_menu)
        my_menu.add_cascade(label="Exit", command=self.exit)

        self.close = Button(self.frame0, text='Back', font=('arial', 12, 'bold'), bd=0, command=self.back_btn)
        self.close.place(x=0, y=0)

    def bil_btn(self):
        self.wn.destroy()
        from bill import billing
        billing(self.username)

#----------------------------------restaurant----------------------------

    def rest_btn(self):
        self.frame = Frame(self.wn)
        self.frame.place(x=50, y=100, width=1400, height=600)

        self.lb_text = Label(self.frame, text='Give the Item Name and Item type i.e [buff,veg,chicken......]'
                                              ' that you want to have\n so that the waiter can tell you the rate of'
                                              ' item that you ordered', font=('arial', 10, 'bold'))
        self.lb_text.place(x=450, y=20)

        self.item_name = Label(self.frame, text="Item Name")
        self.item_name.place(x=550, y=90)

        self.entry_name = Entry(self.frame)
        self.entry_name.place(x=650, y=90)

        self.item_type = Label(self.frame, text="Item Type")
        self.item_type.place(x=550, y=130)

        self.entry_type = Entry(self.frame)
        self.entry_type.place(x=650, y=130)

        self.item_rate = Label(self.frame, text="Item Rate")
        self.item_rate.place(x=550, y=170)

        self.entry_rate = Entry(self.frame)
        self.entry_rate.place(x=650, y=170)

        self.item_add = Button(self.frame, text="Add Item", command=self.add_item)
        self.item_add.place(x=450, y=500)

        self.item_update = Button(self.frame, text="Update Item", command=self.update_item)
        self.item_update.place(x=850, y=500)

        self.delete_select = Button(self.frame, text='delete', command=self.delete_item)
        self.delete_select.place(x=675, y=500)

        self.item_tree = ttk.Treeview(self.frame, columns=('name', 'type', 'rate'))
        self.item_tree.place(x=300, y=220)
        self.item_tree['show'] = 'headings'
        self.item_tree.column('name', width=250)
        self.item_tree.column('type', width=250)
        self.item_tree.column('rate', width=250)
        self.item_tree.heading('name', text="Name")
        self.item_tree.heading('type', text="Type")
        self.item_tree.heading('rate', text="Rate")

        self.show_item_tree()


        # =====================FOR ITEM DATABASE======================
    def add_item(self):
        try:
            c_name = self.combo_Name.get()
            print(c_name)
            name = self.entry_name.get()
            type = self.entry_type.get()
            rate = self.entry_rate.get()
            if c_name == "":
                messagebox.showerror("error", "Son of a bitch")
            else:
                c_data = self.connect_customer.search_customer_name(c_name)
                u_id = c_data[0][0]
                print(u_id)
                if self.validate():
                    if self.item.add_item(name, type, rate, u_id):
                        messagebox.showinfo('Item', "Item Added")
                        self.show_item_tree()
                    else:
                        messagebox.showerror("Error", self.item.add_item(name, type, rate, u_id))
        except EXCEPTION:
            messagebox.showerror("Error", "Something weht wrong u asshole")

    def update_item(self):
        try:
            if self.update_index == "":
                messagebox.showerror("Error", "Please select a row first")
            else:
                name = self.entry_name.get()
                type = self.entry_type.get()
                rate = self.entry_rate.get()
                if self.item.update_item(self.update_index, name, type, rate):
                    messagebox.showinfo('Item', "Item Updated")
                    self.show_item_tree()
                    self.update_index = ""
        except AttributeError:
                messagebox.showerror("Error", 'Can not be updated !!!')

    def delete_item(self):
        try:
            if self.update_index == '':
                messagebox.showerror('Error', 'select the item u want to cancel')
            else:
                if self.item.delete_item(self.update_index):
                    messagebox.showinfo('success', 'successfully deleted')
                    self.show_item_tree()
                    self.update_index= ''
        except AttributeError:
            messagebox.showerror('Error', 'double click to select')

    def show_item_tree(self):
        self.item_tree.delete(*self.item_tree.get_children())
        data = self.item.show_item()
        for i in data:
            self.item_tree.insert("", "end", text=i[0], value=(i[1], i[2], i[3]))
        self.item_tree.bind("<Double-1>", self.on_item_select)

    def on_item_select(self, event):
        selected_row = self.item_tree.selection()[0]
        selected_item = self.item_tree.item(selected_row, 'values')
        self.update_index = self.item_tree.item(selected_row, 'text')
        self.entry_name.delete(0, END)
        self.entry_name.insert(0, selected_item[0])
        self.entry_type.delete(0, END)
        self.entry_type.insert(0, selected_item[1])
        self.entry_rate.delete(0, END)
        self.entry_rate.insert(0, selected_item[2])

    def validate(self):
        name = self.entry_name.get()
        type = self.entry_type.get()
        rate = self.entry_rate.get()
        if name == '' or type == '' or rate == '':
            messagebox.showerror('Error', 'Fill all the fields')
            return False
        elif not rate.isdigit():
            messagebox.showerror('Error', 'Invalid value for rate')
            return False
        else:
            return True
#--------------------------bar-------------------------

    def bar_btn(self):
        self.frame2 = Frame(self.wn)
        self.frame2.place(x=50, y=70, width=1400, height=600)

        self.drink_name = Label(self.frame2, text="Drink's Name")
        self.drink_name.place(x=540, y=120)

        self.entry_name = Entry(self.frame2)
        self.entry_name.place(x=650, y=120)

        self.item_rate = Label(self.frame2, text="Drink's Rate")
        self.item_rate.place(x=540, y=180)

        self.entry_rate = Entry(self.frame2)
        self.entry_rate.place(x=650, y=180)

        self.item_add = Button(self.frame2, text="Add Item", command=self.add_drinks)
        self.item_add.place(x=550, y=500)

        self.item_update = Button(self.frame2, text="Update Item", command=self.update_drinks)
        self.item_update.place(x=800, y=500)

        self.item_delete = Button(self.frame2, text='delete', command=self.delete_entry)
        self.item_delete.place(x=675, y=500)

        self.drinks_tree = ttk.Treeview(self.frame2, columns=('name', 'rate'))
        self.drinks_tree.place(x=510, y=240)
        self.drinks_tree['show'] = 'headings'
        self.drinks_tree.column('name', width=200)
        self.drinks_tree.column('rate', width=200)
        self.drinks_tree.heading('name', text="Name")
        self.drinks_tree.heading('rate', text="Rate")

        self.show_drinks_tree()

    def add_drinks(self):
        c_name = self.combo_Name.get()
        name = self.entry_name.get()
        rate = self.entry_rate.get()
        if c_name == "":
            messagebox.showerror("error", "fuck off")
        u_data = self.connect_customer.search_customer_name(c_name)
        u_id = u_data[0][0]
        if self.validate_drinks():
            if self.drinks.add_drinks(name, rate, u_id):
                messagebox.showinfo('Drinks', "Drinks Added")
                self.show_drinks_tree()
            else:
                messagebox.showerror("Error", self.drinks.add_drinks(name, rate, u_id))

    def update_drinks(self):
        try:
            if self.update_index == "":
                messagebox.showerror("Error", "Please select a row first")
            else:
                name = self.entry_name.get()
                rate = self.entry_rate.get()
                if self.drinks.update_drinks(self.update_index, name, rate):
                    messagebox.showinfo('Drinks', "Drinks Updated")
                    self.show_drinks_tree()
                    self.update_index= ""

        except AttributeError:
            messagebox.showerror("Error", 'Can not be updated !!! plz double tap to to select row')

    def delete_entry(self):
        try:
            if self.update_index == '':
                messagebox.showerror('Error', 'select the item u want to cancel')
            else:
                if self.drinks.delete_drinks(self.update_index):
                    messagebox.showinfo('success', 'successfully deleted')
                    self.show_drinks_tree()
                    self.update_index= ''
        except AttributeError:
            messagebox.showerror('Error', 'double click to select')

    def show_drinks_tree(self):
        self.drinks_tree.delete(*self.drinks_tree.get_children())
        data = self.drinks.show_drinks()
        for i in data:
            self.drinks_tree.insert("", "end", text=i[0], value=(i[1], i[2]))
        self.drinks_tree.bind("<Double-1>", self.on_drinks_select)

    def on_drinks_select(self, event):
        selected_row = self.drinks_tree.selection()[0]
        selected_drinks = self.drinks_tree.item(selected_row, 'values')
        self.update_index = self.drinks_tree.item(selected_row, 'text')
        self.entry_name.delete(0, END)
        self.entry_name.insert(0, selected_drinks[0])
        self.entry_rate.delete(0, END)
        self.entry_rate.insert(0, selected_drinks[1])

    def validate_drinks(self):
        name = self.entry_name.get()
        rate = self.entry_rate.get()
        if name == '' or rate == '':
            messagebox.showerror('Error', 'Fill all the fields')
            return False
        elif not rate.isdigit():
            messagebox.showerror('Error', 'Invalid value for rate')
            return False
        else:
            return True
#---------------------------- room service---------------------------
    def room_serv(self):
        self.frame1 = Frame(self.wn)
        self.frame1.place(x=50, y=70, width=1400, height=600)

        self.title_photo = PhotoImage(file='room.PNG')
        self.title_photo_lable = Label(self.frame1, image=self.title_photo)
        self.title_photo_lable.image = self.title_photo
        self.title_photo_lable.place(x=100, y=150)

        self.title_photo = PhotoImage(file='jym.PNG')
        self.title_photo_lable = Label(self.frame1, image=self.title_photo)
        self.title_photo_lable.image = self.title_photo
        self.title_photo_lable.place(x=550, y=120)

        self.title_photo =PhotoImage(file='travel.PNG')
        self.title_photo_lable = Label(self.frame1, image=self.title_photo)
        self.title_photo_lable.image = self.title_photo
        self.title_photo_lable.place(x=1050, y=120)

        self.lb_text = Label(self.frame1, text='Room Service', font=('arial', 10, 'bold'))
        self.lb_text.place(x=200, y=60)

        self.lb_text = Label(self.frame1, text='Room delivery,Laundry,Housekeeping', font=('arial', 10, 'bold'))
        self.lb_text.place(x=110, y=350)

        self.lb_text = Label(self.frame1, text='Gym', font=('arial', 10, 'bold'))
        self.lb_text.place(x=630, y=70)

        self.lb_text = Label(self.frame1, text='All equipments+Cardio ', font=('arial', 10, 'bold'))
        self.lb_text.place(x=570, y=350)

        self.lb_text = Label(self.frame1, text='Travel', font=('arial', 10, 'bold'))
        self.lb_text.place(x=1150, y=70)

        self.lb_text = Label(self.frame1, text='Travel Guide and Vehicles', font=('arial', 10, 'bold'))
        self.lb_text.place(x=1100, y=350)

        self.btn_book = Button(self.frame1, text='Book', bd=2, font=('arial', 13, 'bold'),
                               command=self.ok_1)
        self.btn_book.place(x=650, y=500)

        self.radio_button1 = IntVar()
        self.radio_button2 = IntVar()
        self.radio_button3 = IntVar()

        btn_1 = Radiobutton(self.frame1, text='book', value=1500, variable=self.radio_button1,
                            command=self.radiovalue1)
        btn_1.place(x=180, y=400)

        btn_2 = Radiobutton(self.frame1, text='book', value=500, variable=self.radio_button2,
                            command=self.radiovalue2)
        btn_2.place(x=610, y=400)

        btn_3 = Radiobutton(self.frame1, text='book', value=250, variable=self.radio_button3,
                            command=self.radiovalue3)
        btn_3.place(x=1150, y=400)

        self.wn.mainloop()

    def radiovalue1(self):
        print(self.radio_button1.get())

    def radiovalue2(self):
        print(self.radio_button2.get())

    def radiovalue3(self):
        print(self.radio_button3.get())


    def ok_1(self):
        book1 = self.radio_button1.get()
        book2 = self.radio_button2.get()
        book3 = self.radio_button3.get()

        if book1 == 0 or book2 == 0 or book3 == 0:
            messagebox.showerror('Error', 'please select the service')
        else:
            messagebox.showinfo('success', 'successfully booked')

    def back_btn(self):
        self.wn.destroy()
        import dashboard

    def exit(self):
        ask = tkinter.messagebox.askyesno('Exit', 'Do you want to exit?')
        if ask == 1:
            exit()
        else:
            pass


wn = Tk()
lobby_page(wn, 'suvanshu')
wn.mainloop()