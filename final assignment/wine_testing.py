from tkinter import *
from tkinter import messagebox


class wine_test:
    def __init__(self, window):
        self.wn = window

        self.wine_frame = LabelFrame(self.wn, width=1500, height=800)
        self.wine_frame.pack()

        self.frame = Frame(self.wine_frame, bg='#DCDCDC', width=1400, height=700)
        self.frame.place(x=50, y=45)

        self.title_photo = PhotoImage(file='1.PNG')
        self.title_photo_lable = Label(self.frame, image=self.title_photo)
        self.title_photo_lable.place(x=800, y=90)

        self.lb_text = Label(self.frame, text='Wine tasting in Hillside', font=('arial', 15), bg='#DCDCDC')
        self.lb_text.place(x=10, y=55)

        self.lb_text = Label(self.frame, text='Sicily has a long tradition in wine making experience and nowadays\n'
                                              'wine bars are a melting port of culture and history. Panoramic Hotel\n'
                                              'gives you the opportunity to experience the emotion right in the      \n'
                                              'historical center of Hillside with the support of experts           ',
                             font=('arial', 12), bg='#DCDCDC')
        self.lb_text.place(x=10, y=105)

        self.lb_text1 = Label(self.frame, text='The offers includes:', font=('arial', 13, 'bold'), bg='#DCDCDC')
        self.lb_text1.place(x=10, y=225)

        self.lb_text2 = Label(self.frame, text='-minimum stay of 3 nights, in a beautiful room with private terrace'
                              , font=('arial', 12), bg='#DCDCDC')
        self.lb_text2.place(x=10, y=270)

        self.lb_text3 = Label(self.frame, text='-Buffet breakfast served in our Terrace & '
                                               'sicilian Wine-tasting', font=('arial', 12), bg='#DCDCDC')
        self.lb_text3.place(x=10, y=310)

        self.lb_text4 = Label(self.frame, text='-A delicious bottle of Duca of Salaparuta in room upon arrival',
                              font=('arial', 12), bg='#DCDCDC')
        self.lb_text4.place(x=10, y=350)

        self.lb_text5 = Label(self.frame, text='-Complimentary WiFi connection for the entire duration of  your stay',
                              font=('arial', 12), bg='#DCDCDC')
        self.lb_text5.place(x=10, y=390)

        self.lb_text6 = Label(self.frame, text='This offer is not combined with other promotions.\n'
                                               'offer available by booking 3 days prior to arrival date ',
                              font=('arial', 12), bg='#DCDCDC')
        self.lb_text6.place(x=10, y=450)

        self.lb_text7 = Label(self.frame, text='the unit cost of this package is 25,000 , once you \n'
                                               'book this package the price is non-refundable',
                              font=('arial', 13), bg='#DCDCDC')
        self.lb_text7.place(x=730, y=360)

        self.book = Button(self.frame, text='Book Now', font=('arial', 13, 'bold'), bg='#DCDCDC', command=self.book_btn)
        self.book.place(x=860, y=312)

        self.exit = Button(self.wine_frame, text='Back ', font=('arial', 13, 'bold'), bg='#DCDCDC', command=self.back_dtn)
        self.exit.place(x=0, y=0)

    def back_dtn(self):
        self.wine_frame.pack_forget()
        self.wine_frame.destroy()

    def book_btn(self):
        messagebox.showinfo('sucess', 'successfully booked enjoy your package')
        self.wine_frame.destroy()
        self.back_dtn()


