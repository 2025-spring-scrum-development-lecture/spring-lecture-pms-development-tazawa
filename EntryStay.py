import customtkinter as ctk

class EntryStay(ctk.CTkFrame):
    def __init__(self, master, name, email):
        super().__init__(master)
        
        self.master = master
        self.name = name
        self.email = email
        
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        master.geometry(f'{screen_width}x{screen_height}')
        master.title('宿泊内容の入力')
        
        ctk.set_appearance_mode("Light")
        ctk.set_default_color_theme("green")
        
        # 部屋数を数える変数
        self.room_cnt = 1
        
        self.create_widget()
        self.check_option()
        
    def create_widget(self):
        self.guest_label = ctk.CTkLabel(self.master, text=f'{self.name}様〖{self.email}〗', font=('Times', 20))
        self.guest_label.place(x=20, y=10)
        
        self.quotation_button = ctk.CTkButton(self.master, text='確定して見積りを出す＞', font=('Times', 20), command=self.confirmed_info)
        self.quotation_button.place(x=1020, y=10)
        
        frame = ctk.CTkFrame(self.master, width=430, height=550)
        frame.place(x=20, y=80)
        
        # 部屋数
        self.room_cnt_label = ctk.CTkLabel(frame, text=f'{self.room_cnt}部屋目', font=('Times', 16))
        self.room_cnt_label.place(x=10, y=10)
        
        
        # 人数(self.numAdult, self.numChild)
        self.numPeople_label = ctk.CTkLabel(frame, text='人数', font=('Times', 20))
        self.numPeople_label.place(x=10, y=40)
        
        self.numAdult_label = ctk.CTkLabel(frame, text='大人', font=('Times', 16))
        self.numAdult_label.place(x=100, y=40)
        numAdult_menu = [1, 2, 3, 4, 5, 6]
        self.numAdult_Entry = ctk.CTkOptionMenu(frame, values=[str(num) for num in numAdult_menu], width=60, height=25, font=('Times', 16))
        self.numAdult_Entry.place(x=150, y=40)
        
        self.numChild_label = ctk.CTkLabel(frame, text='小学生', font=('Times', 16))
        self.numChild_label.place(x=240, y=40)
        numChild_menu = [1, 2, 3, 4, 5, 6]
        self.numChild_Entry = ctk.CTkOptionMenu(frame, values=[str(num) for num in numChild_menu], width=60, height=25, font=('Times', 16))
        self.numChild_Entry.place(x=310, y=40)
        
        
        # 泊数(self.numStay)
        self.numStay_label = ctk.CTkLabel(frame, text='泊数', font=('Times', 20))
        self.numStay_label.place(x=10, y=80)
        self.numStay_Entry = ctk.CTkEntry(frame, width=60, height=25, font=('Times', 16))
        self.numStay_Entry.place(x=100, y=80)
        self.label = ctk.CTkLabel(frame, text='泊', font=('Times', 16))
        self.label.place(x=165, y=80)
        
        
        # 部屋プラン(self.room)
        self.room_label = ctk.CTkLabel(frame, text='お部屋', font=('Times', 20))
        self.room_label.place(x=10, y=120)
        room_menu = ['本館和室7.5畳', '西館洋室(ツイン)', '岩手山側和室', '岩手山側露天風呂付き和室', '西館和室10畳', '檜内風呂付き和洋室', '西館和洋室', '西館和室28畳']
        self.room_Entry = ctk.CTkOptionMenu(frame, values=[room for room in room_menu], font=('Times', 16))
        self.room_Entry.place(x=80, y=120)
        
        
        # 夕食プラン(self.dinner)
        self.dinner_label = ctk.CTkLabel(frame, text='ご夕食', font=('Times', 20))
        self.dinner_label.place(x=10, y=160)
        dinner_menu = ['スタンダード', '岩手県産牛', '前沢牛', '夕食なし(素泊まり)']
        self.dinner_Entry = ctk.CTkOptionMenu(frame, values=[dinner for dinner in dinner_menu], font=('Times', 16))
        self.dinner_Entry.place(x=80, y=160)
        
        
        # オプション(self.checkin_option, bedrockButh_option, peterAdult_option, peterChild_option, parkAdult_option, parkChild_option, tennis_option, hotSpringRental_option, dogone_option, numdog, dogoneSpa)
        self.option_label = ctk.CTkLabel(frame, text='オプション', font=('Times', 20))
        self.option_label.place(x=10, y=200)

        self.option_menu = ['土曜日チェックイン', '岩盤浴', 'パターゴルフ', 'パークゴルフ', 'テニスコート利用', '温泉貸し切り', 'ドッグワン']
        self.option_vars = []

        for i, option in enumerate(self.option_menu):
            var = ctk.StringVar(value="off")
            self.option_vars.append(var)
            checkbox = ctk.CTkCheckBox(frame, text=option, variable=var, onvalue="on", offvalue="off", font=('Times', 16), checkbox_width=15, checkbox_height=15)
            checkbox.place(x=10, y=240 + i * 30)
            
        self.numDog_var = ctk.IntVar()
        self.numDog_var.set(1)
        self.numDog_Entry = ctk.CTkEntry(frame, width=60, height=25, font=('Times', 16), textvariable=self.numDog_var)
        self.numDog_label = ctk.CTkLabel(frame, text='匹', font=('Times', 16))
        self.dogoneSpa_label = ctk.CTkLabel(frame, text='スパ', font=('Times', 16))
        self.radio_vars = ctk.StringVar(value='unuse')
        self.dogoneSpaUse_label = ctk.CTkRadioButton(frame, text='利用する', font=('Times', 16), variable=self.radio_vars, value='use')
        self.dogoneSpaUnUse_label = ctk.CTkRadioButton(frame, text='利用しない', font=('Times', 16), variable=self.radio_vars, value='unuse')
        
    def check_option(self):
        checkin_selected = False
        bedrockButh_selected = False
        petergolf_selected = False
        pardgolf_selected = False
        tennis_selected = False
        hotSpringRental_selected = False
        dogone_selected = False
        
        self.numAdult = int(self.numAdult_Entry.get())
        self.numChild = int(self.numChild_Entry.get())
        
        try:
            self.numStay = self.numStay_Entry.get()
            if self.numStay == '':
                self.numStay = 1
        except Exception as e:
            self.numDog = 1
        
        self.room = self.room_Entry.get()
        self.dinner = self.dinner_Entry.get()
        self.plan = self.calc_price(self.room, self.dinner)
        self.planPrace_Adult = self.plan[0]
        self.planPrace_Child = self.plan[1]
        
        self.numPeople = self.numAdult + self.numChild
        
        for i, var in enumerate(self.option_vars):
            if var.get() == 'on':
                if self.option_menu[i] == '土曜日チェックイン':
                    checkin_selected = True
                elif self.option_menu[i] == '岩盤浴':
                    bedrockButh_selected = True
                elif self.option_menu[i] == 'パターゴルフ':
                    petergolf_selected = True
                elif self.option_menu[i] == 'パークゴルフ':
                    pardgolf_selected = True
                elif self.option_menu[i] == 'テニスコート利用':
                    tennis_selected = True
                elif self.option_menu[i] == '温泉貸し切り':
                    hotSpringRental_selected = True
                elif self.option_menu[i] == 'ドッグワン':
                    dogone_selected = True
                    
        if checkin_selected:
            self.checkin_option = 2200 * self.numPeople
        else:
            self.checkin_option = 0
              
        if bedrockButh_selected:
            self.bedrockButh_option = 1500 * self.numPeople
        else:
            self.bedrockButh_option = 0
            
        if petergolf_selected:
            self.peterAdult_option = 500 * self.numAdult
            self.peterChild_option = 250 * self.numChild
        else:
            self.peterAdult_option = 0
            self.peterChild_option = 0
            
        if pardgolf_selected:
            self.parkAdult_option = 600 * self.numAdult
            self.parkChild_option = 300 * self.numChild
        else:
            self.parkAdult_option = 0
            self.parkChild_option = 0
            
        if tennis_selected:
            self.tennis_option = 1000 * self.numPeople
        else:
            self.tennis_option = 0
            
        if hotSpringRental_selected:
            self.hotSpringRental_option = 2500 * self.numPeople
        else:
            self.hotSpringRental_option = 0
                    
        if dogone_selected:
            self.numDog_Entry.place(x=130, y=420)
            self.numDog_label.place(x=195, y=420)
            self.dogoneSpa_label.place(x=130, y=460)
            self.dogoneSpaUse_label.place(x=170, y=460)
            self.dogoneSpaUnUse_label.place(x=170, y=490)
            try:
                self.numDog = self.numDog_var.get()
                if self.numDog == '':
                    self.numDog = 0
            except Exception as e:
                self.numDog = 1
            self.numDog_option = 1000
            if self.radio_vars.get() == 'use':
                self.dogoneSpa_option = 1800
                if self.numDog >= 2:
                    self.dogoneSpa_option += 1000 * (self.numDog - 1)
            else:
                self.dogoneSpa_option = 0
            numDog_option = int(self.numDog_option)
            numDog = int(self.numDog)
            dogoneSpa_option = int(self.dogoneSpa_option)
            self.dogone_option = numDog_option * numDog + dogoneSpa_option
            
        else:
            self.numDog_Entry.place_forget()
            self.numDog_label.place_forget()
            self.dogoneSpa_label.place_forget()
            self.dogoneSpaUse_label.place_forget()
            self.dogoneSpaUnUse_label.place_forget()
            self.dogone_option = 0
                    
        self.master.after(1000, self.check_option)
        
    def calc_price(self, room, dinner):
        self.plan_menu = {('本館和室7.5畳', 'スタンダード'): (12400, 12400),
                ('本館和室7.5畳', '岩手県産牛'): (15400, 15400),
                ('本館和室7.5畳', '前沢牛'): (18400, 18400),
                ('本館和室7.5畳', '素泊まり'): (8500, 8500),
                
                ('西館洋室(ツイン)', 'スタンダード'): (12400, 12400),
                ('西館洋室(ツイン)', '岩手県産牛'): (15400, 15400),
                ('西館洋室(ツイン)', '前沢牛'): (18400, 18400),
                ('西館洋室(ツイン)', '素泊まり'): (8500, 8500),
                
                ('岩手山側和室', 'スタンダード'): (12400, 7200),
                ('岩手山側和室', '岩手県産牛'): (15400, 7200),
                ('岩手山側和室', '前沢牛'): (18400, 7200),
                ('岩手山側和室', '素泊まり'): (8500, 8500),
                
                ('岩手山側露天風呂付き和室', 'スタンダード'): (14400, 7200),
                ('岩手山側露天風呂付き和室', '岩手県産牛'): (17400, 7200),
                ('岩手山側露天風呂付き和室', '前沢牛'): (20400, 7200),
                ('岩手山側露天風呂付き和室', '素泊まり'): (8500, 8500),
                
                ('西館和室10畳', 'スタンダード'): (12400, 7200),
                ('西館和室10畳', '岩手県産牛'): (15400, 7200),
                ('西館和室10畳', '前沢牛'): (21400, 7200),
                ('西館和室10畳', '素泊まり'): (8500, 8500),
                
                ('檜内風呂付き和洋室', 'スタンダード'): (15400, 7200),
                ('檜内風呂付き和洋室', '岩手県産牛'): (18400, 7200),
                ('檜内風呂付き和洋室', '前沢牛'): (21400, 7200),
                ('檜内風呂付き和洋室', '素泊まり'): (8500, 8500),
                
                ('西館和洋室', 'スタンダード'): (12400, 7200),
                ('西館和洋室', '岩手県産牛'): (15400, 7200),
                ('西館和洋室', '前沢牛'): (21400, 7200),
                ('西館和洋室', '素泊まり'): (8500, 8500),
                
                ('西館和室28畳', 'スタンダード'): (12400, 7200),
                ('西館和室28畳', '岩手県産牛'): (15400, 7200),
                ('西館和室28畳', '前沢牛'): (21400, 7200),
                ('西館和室28畳', '素泊まり'): (8500, 8500)}
        self.plan = self.plan_menu.get((room, dinner))
        return self.plan
        
    def confirmed_info(self):
        # self.numAdult = self.numAdult_Entry.get()
        # self.numChild = self.numChild_Entry.get()
        # self.numStay = self.numStay_Entry.get()
        # self.dinner = self.dinner_Entry.get()
        print(self.numAdult)
        print(self.numChild)
        print(self.numStay)
        print(self.planPrace_Adult)
        print(self.planPrace_Child)
        print(self.checkin_option)
        print(self.bedrockButh_option)
        print(self.peterAdult_option)
        print(self.peterChild_option)
        print(self.parkAdult_option)
        print(self.parkChild_option)
        print(self.tennis_option)
        print(self.hotSpringRental_option)
        print(self.dogone_option)
        
        from auth import pagemove_entrystay_quotationstay
        self.destroy()
        pagemove_entrystay_quotationstay(self.master, self.numAdult, self.numChild, self.numStay, self.dinner, self.checkin_option, self.bedrockButh_option, self.peterAdult_option, self.peterChild_option, self.parkAdult_option, self.parkChild_option, self.tennis_option, self.hotSpringRental_option, self.dogone_option)

if __name__ == '__main__':
    root = ctk.CTk()
    app = EntryStay(root, name='aaa', email='aaa')
    root.mainloop()