from tkinter import *


class pack_page:
    def __init__(self, window):
        self.win = window

        self.main_frame = LabelFrame(self.win, width=1500, height=800)
        self.main_frame.pack()

        self.frame = Frame(self.main_frame, bg='#DCDCDC', width=1400, height=700, bd=3)
        self.frame.place(x=50, y=45)

        self.frame1 = Frame(self.frame, width=200, height=208, bd=3)
        self.frame1.place(x=350, y=250)

        self.title_photo = PhotoImage(file='1.PNG')
        self.title_photo_lable = Label(self.frame1, image=self.title_photo)
        self.title_photo_lable.image = self.title_photo
        self.title_photo_lable.place(x=-5, y=-5)

        self.frame2 = Frame(self.frame, width=200, height=208, bd=3)
        self.frame2.place(x=850, y=255)

        self.title_photo = PhotoImage(file='2.PNG')
        self.title_photo_lable = Label(self.frame2, image=self.title_photo)
        self.title_photo_lable.image = self.title_photo
        self.title_photo_lable.place(x=-5, y=-5)

        self.lbl_text1 = Label(self.frame, text='Only for you', font=('chiller', 40), bg='#DCDCDC')
        self.lbl_text1.place(x=600, y=5)

        self.lbl_text2 = Label(self.frame, text="Special Offers", font=('arial', 20), bg='#DCDCDC')
        self.lbl_text2.place(x=600, y=100)

        self.hill = Button(self.main_frame, text='Book', font=('arial', 13, 'bold', 'underline'), bd=0,
                           bg='#DCDCDC', command=self.hill_side)
        self.hill.place(x=470, y=520)

        self.lbl_text3 = Label(self.frame, text='Wine testing in Hillside', font=('arial', 13), bg='#DCDCDC')
        self.lbl_text3.place(x=360, y=510)

        self.lbl_text4 = Label(self.frame, text='Happy birthday \nwith us !', font=('arial', 13), bg='#DCDCDC')
        self.lbl_text4.place(x=900, y=510)

        self.bd = Button(self.main_frame, text='Book', font=('arial', 13, 'bold', 'underline'), width=5, bd=0,
                         bg='#DCDCDC',
                         command=self.bd_page)
        self.bd.place(x=980, y=520)

        self.btn_back = Button(self.frame, text='Back', font=('bold', 13), bg='#DCDCDC', command=self.back_btn)
        self.btn_back.place(x=0, y=0)

    def back_btn(self):
        self.main_frame.pack_forget()
        self.main_frame.destroy()

    def hill_side(self):
        import wine_testing
        wine = wine_testing.wine_test(self.main_frame)

    def bd_page(self):
        import birthday
        birth = birthday.birthday_with(self.main_frame)

