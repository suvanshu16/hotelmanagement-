from tkinter import *
from tkinter import messagebox


class birthday_with:
    def __init__(self, window):
        self.wn = window

        self.birthday_frame = LabelFrame(window, width=1500, height=800)
        self.birthday_frame.pack()

        self.frame = Frame(self.birthday_frame, bg='#DCDCDC', width=1400, height=700)
        self.frame.place(x=50, y=45)

        self.title_photo =PhotoImage(file='2.PNG')
        self.title_photo_lable = Label(self.frame, image=self.title_photo)
        self.title_photo_lable.place(x=800, y=90)

        self.lb_text1 = Label(self.frame, text='Happy Birthday with us !', font=('arial', 14), bg='#DCDCDC')
        self.lb_text1.place(x=10, y=55)

        self.lb_text = Label(self.frame, text='Your birthday is approaching? Do you want to celebrate it ina a special'
                                              '\n way? Book it now at the Panoramic Hotel in Hillside',
                             font=('arial', 12), bg='#DCDCDC')
        self.lb_text.place(x=10, y=105)

        self.lb_text8 = Label(self.frame, text='We Will customize a cake of your choice. You will bw able to choose\n'
                                               'among wonderful flavours along with a delicious bottle of Prosecco!',
                              font=('arial', 12), bg='#DCDCDC')
        self.lb_text8.place(x=10, y=150)

        self.lb_text1 = Label(self.frame, text='The offers includes:', font=('arial', 13, 'bold'), bg='#DCDCDC')
        self.lb_text1.place(x=10, y=225)

        self.lb_text2 = Label(self.frame, text='-Lovely room with private balcony overlooking the beautiful scene'
                              , font=('arial', 12), bg='#DCDCDC')
        self.lb_text2.place(x=10, y=270)

        self.lb_text3 = Label(self.frame, text='-Buffet breakfast served in our Terrace & ', font=('arial', 12),
                              bg='#DCDCDC')
        self.lb_text3.place(x=10, y=310)

        self.lb_text4 = Label(self.frame, text='-Your special birthday cake prepared and backed exclusively for you',
                              font=('arial', 12), bg='#DCDCDC')
        self.lb_text4.place(x=10, y=350)

        self.lb_text5 = Label(self.frame, text='-Complimentary WiFi connection for the entire duration of  your stay',
                              font=('arial', 12), bg='#DCDCDC')
        self.lb_text5.place(x=10, y=390)

        self.lb_text9 = Label(self.frame, text='-A delicious bottle of Khukuri Rum',
                              font=('arial', 12), bg='#DCDCDC')
        self.lb_text9.place(x=10, y=430)

        self.lb_text6 = Label(self.frame, text='This offer is not combined with other promotions.\n'
                                               'offer available by booking 2 days prior to arrival date ',
                              font=('arial', 12), bg='#DCDCDC')
        self.lb_text6.place(x=10, y=480)

        self.lb_text7 = Label(self.frame, text='the unit cost of this package is 25,000 , once you \n'
                                               'book this package the price is non-refundable',
                              font=('arial', 13), bg='#DCDCDC')
        self.lb_text7.place(x=730, y=350)

        self.book = Button(self.frame, text='Book Now', font=('arial', 13, 'bold'), bg='#DCDCDC', command=self.book_btn)
        self.book.place(x=860, y=312)

        self.exit = Button(self.birthday_frame, text='Back ', font=('arial', 13, 'bold'), bg='#DCDCDC', command=self.back_dtn)
        self.exit.place(x=0, y=0)

    def back_dtn(self):
        self.birthday_frame.pack_forget()
        self.birthday_frame.destroy()

    def book_btn(self):
        messagebox.showinfo('sucess', 'successfully booked enjoy your package')
        self.birthday_frame.destroy()
        self.back_dtn()



