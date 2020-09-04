from tkinter import *
import time


class main_page:
    def __init__(self, username):
        self.wn = Tk()
        self.wn.title("System")
        self.wn.geometry('1500x800')
        self.wn.resizable(0, 0)

        self.username = username

        self.frame = Frame(self.wn, bg='#DCDCDC', width=1400, height=700)
        self.frame.place(x=50, y=45)

        self.adm = Button(self.wn, text='Admin', font=('arial', 13, 'bold', 'underline'), width=17,
                          height=8, bd=4, command=self.login_btn)
        self.adm.place(x=400, y=140)

        self.service = Button(self.wn, text='Service', font=('arial', 13, 'bold', 'underline'),
                              width=17, height=8, bd=4, command=self.service_btn)
        self.service.place(x=900, y=140)

        self.package = Button(self.wn, text='Package', font=('arial', 13, 'bold', 'underline'), width=17, height=8,
                              bd=4, command=self.package_btn)
        self.package.place(x=900, y=380)

        self.lb_text = Label(self.frame, text='Hotel Description', font=('arial', 15, 'bold'), bg='#DCDCDC')
        self.lb_text.place(x=610, y=15)

        self.lb_text2 = Label(self.frame, text='The panoramic Hotel is a modern,elegant 4-\n'
                                               'star hotel overlooking the mountain, perfect for a \n'
                                               'romantic, charming vacation,in the \n'
                                               'enchanting setting of Taormina.',
                              font=('arial', 10), bg='#DCDCDC')
        self.lb_text2.place(x=540, y=150)

        self.lb_text3 = Label(self.frame, text='The room at the Panoramic Hotel are new,\n'
                                               'well-lit and inviting.Our reception staff will be\n'
                                               'happy to help you during you stay in',
                              font=('arial', 10), bg='#DCDCDC')
        self.lb_text3.place(x=550, y=250)

        self.lb_text4 = Label(self.frame, text='At the end of the stairway across from the \n'
                                               'hotel,the white pebbles on the beach of Isola\n'
                                               'Bella await you as well as beach facilities\n'
                                               'with lounge chairs and umbrellas',
                              font=('arial', 10), bg='#DCDCDC')
        self.lb_text4.place(x=555, y=350)

        self.lb_text5 = Label(self.frame, text='Available services include Voip Telephone\n'
                                               'ideal for low-cost international calls-WiFi\n'
                                               'internet connection,breakfast and 24-hour reception',
                              font=('arial', 10), bg='#DCDCDC')
        self.lb_text5.place(x=545, y=450)

        self.lb_text6 = Label(self.frame, text='Panoramic Hotel - PAB Costruzioni S.r.l.',
                              font=('arial', 12), bg='#DCDCDC')
        self.lb_text6.place(x=550, y=620)

        self.lb_text7 = Label(self.frame, text='Tel. +057 512063 '
                                               'Mob. +977 9874536123 Fax +977 0942 620679 | VAT 01238360877 - '
                                               'info@panoramictaormina.it\nPanoramic Hotel © 2000-2020 Hotel '
                                               'Marketing by Atlantic Business |Cookies/Copyright/IP Policy - Privacy',
                              font=('arial', 10), bg='#DCDCDC')
        self.lb_text7.place(x=350, y=650)

        self.frame_log = LabelFrame(self.wn).pack()
        self.frame_admin = LabelFrame(self.wn).pack()
        self.frame_service = LabelFrame(self.wn).pack()

        self.times()
        self.wn.mainloop()

    def login_btn(self):
        import admin
        log = admin.admin_page(self.frame_admin)

    def times(self):
        current_time = time.strftime("%I:%M:%S:%p")
        clock_lbl = Label(self.frame, font=('arial', 25), bg='#DCDCDC', fg='black', text=current_time)
        clock_lbl.after(200, self.times)
        clock_lbl.place(x=1200, y=0)

    def package_btn(self):
        import package
        pack2 = package.pack_page(self.frame_log)

    def service_btn(self):
        self.wn.destroy()
        import newlobby

    def bill_btn(self):
        self.wn.destroy()
        from bill import billing
        billing(self.username)


#main_page()
