import customtkinter as ctk

class EntryStay(ctk.CTkFrame):
    def __init__(self, master, name, email):
        super().__init__(master)
        self.master = master
        self.name = name
        self.email = email
        # 画面サイズ調整
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        master.geometry(f'{screen_width}x{screen_height}')
        master.title('宿泊内容の入力')
        # 画面モード設定
        ctk.set_appearance_mode("Light")
        ctk.set_default_color_theme("green")
        # 部屋数を数える変数
        self.room_cnt = 1
        self.frame_line_x = 5
        self.frame_line_y = 0
        # 入力値を部屋ごとに管理するリスト
        self.numAdult_list = []
        self.numChild_list = []
        self.numStay_list = []
        self.room_list = []
        self.dinner_list = []
        self.planPrace_Adult_list = []
        self.planPrace_Child_list = []
        self.checkin_option_list = []
        self.bedrockButh_option_list = []
        self.peterAdult_option_list = []
        self.peterChild_option_list = []
        self.parkAdult_option_list = []
        self.parkChild_option_list = []
        self.tennis_option_list = []
        self.hotSpringRental_option_list = []
        self.dogone_option_list = []
        self.numDog_list = []
        self.dogoneSpa_option_list = []
        # ドッグワンオプション変数の初期値
        self.numDog = 0
        self.dogoneSpa_option = 0
        # ウィジェットの生成、入力チェック
        self.create_widget()
        self.check_option()


    def create_widget(self):
        # 入力フォーム以外のウィジェット(1回目だけ)
        if self.room_cnt == 1:
            self.guest_label = ctk.CTkLabel(self.master, text=f'{self.name}様〖{self.email}〗', font=('Times', 20))
            self.guest_label.place(x=20, y=10)
            # 確定ボタンの作成
            self.quotation_button = ctk.CTkButton(self.master, text='確定して見積りを出す＞', font=('Times', 20), command=self.confirmed_info)
            self.quotation_button.place(x=1020, y=10)
            # ベースフレーム(スクロール)の作成
            self.screen_height = self.master.winfo_screenheight()
            self.base_frame_y = int(self.screen_height * 0.8)
            self.base_frame = ctk.CTkFrame(self.master, width=1230, height=self.base_frame_y)
            self.base_frame.place(x=15, y=50)
            self.scroll_frame = ctk.CTkScrollableFrame(self.base_frame, width=1230, height=self.base_frame_y)
            self.scroll_frame.pack(fill="both", expand=True)
            # フレームの管理
            self.frame_lines = []  # 行ごとのフレームリスト
            self.all_frames = []   # 全てのフレームを保存するリスト
        # 新しい部屋フレームを作成
        self.create_room_frame()


    def create_room_frame(self):
        # 行番号と列番号を計算
        self.row = (self.room_cnt - 1) // 3
        self.col = (self.room_cnt - 1) % 3
        # rowが3部屋分になっていたら新しい行にフレームをつくる
        if self.row >= len(self.frame_lines):
            # 新しい行のフレーム
            self.frame_line = ctk.CTkFrame(self.scroll_frame, width=1240, height=self.base_frame_y)
            self.frame_line.pack(fill="x", expand=True)
            self.frame_lines.append(self.frame_line)
        # 新しい部屋フレームを作成
        self.frame = ctk.CTkFrame(self.frame_lines[self.row], width=400, height=550)
        # 各フレームのx座標を決める
        if self.col == 0:
            frame_x = 10
        elif self.col == 1:
            frame_x = 415
        else:  # col == 2
            frame_x = 820
        # フレームの配置
        self.frame.place(x=frame_x, y=13)
        self.all_frames.append(self.frame)
        
        # 部屋数
        self.room_cnt_label = ctk.CTkLabel(self.frame, text=f'{self.room_cnt}部屋目', font=('Times', 16))
        self.room_cnt_label.place(x=10, y=10)
        # 人数(self.numAdult, self.numChild)
        self.numPeople_label = ctk.CTkLabel(self.frame, text='人数', font=('Times', 20))
        self.numPeople_label.place(x=10, y=40)
        self.numAdult_label = ctk.CTkLabel(self.frame, text='大人', font=('Times', 16))
        self.numAdult_label.place(x=100, y=40)
        self.numAdult_menu = [1, 2, 3, 4, 5, 6]
        self.numAdult_Entry = ctk.CTkOptionMenu(self.frame, values=[str(num) for num in self.numAdult_menu], width=60, height=25, font=('Times', 16), command=self.update_numChild_menu)
        self.numAdult_Entry.place(x=150, y=40)
        self.numChild_label = ctk.CTkLabel(self.frame, text='小学生', font=('Times', 16))
        self.numChild_label.place(x=240, y=40)
        self.numChild_menu = [0, 1, 2, 3, 4, 5]
        self.numChild_Entry = ctk.CTkOptionMenu(self.frame, values=[str(num) for num in self.numChild_menu], width=60, height=25, font=('Times', 16))
        self.numChild_Entry.place(x=310, y=40)
        # 泊数(self.numStay)
        self.numStay_label = ctk.CTkLabel(self.frame, text='泊数', font=('Times', 20))
        self.numStay_label.place(x=10, y=80)
        self.numStay_var = ctk.IntVar()
        self.numStay_var.set(1)
        self.numStay_Entry = ctk.CTkEntry(self.frame, width=60, height=25, font=('Times', 16), textvariable=self.numStay_var)
        self.numStay_Entry.place(x=100, y=80)
        self.label = ctk.CTkLabel(self.frame, text='泊', font=('Times', 16))
        self.label.place(x=165, y=80)
        # 部屋プラン(self.room)
        self.room_label = ctk.CTkLabel(self.frame, text='お部屋', font=('Times', 20))
        self.room_label.place(x=10, y=120)
        room_menu = ['本館和室7.5畳', '西館洋室(ツイン)', '岩手山側和室', '岩手山側露天風呂付き和室', '西館和室10畳', '檜内風呂付き和洋室', '西館和洋室', '西館和室28畳']
        self.room_Entry = ctk.CTkOptionMenu(self.frame, values=[room for room in room_menu], font=('Times', 16))
        self.room_Entry.place(x=80, y=120)
        # 夕食プラン(self.dinner)
        self.dinner_label = ctk.CTkLabel(self.frame, text='ご夕食', font=('Times', 20))
        self.dinner_label.place(x=10, y=160)
        dinner_menu = ['スタンダード', '岩手県産牛', '前沢牛', '夕食なし(素泊まり)']
        self.dinner_Entry = ctk.CTkOptionMenu(self.frame, values=[dinner for dinner in dinner_menu], font=('Times', 16))
        self.dinner_Entry.place(x=80, y=160)
        # オプション(self.checkin_option, bedrockButh_option, peterAdult_option, peterChild_option, parkAdult_option, parkChild_option, tennis_option, hotSpringRental_option, dogone_option, numdog, dogoneSpa)
        self.option_label = ctk.CTkLabel(self.frame, text='オプション', font=('Times', 20))
        self.option_label.place(x=10, y=200)
        self.option_menu = ['土曜日チェックイン', '岩盤浴', 'パターゴルフ', 'パークゴルフ', 'テニスコート利用', '温泉貸し切り', 'ドッグワン']
        self.option_vars = []
        for i, option in enumerate(self.option_menu):
            var = ctk.StringVar(value="off")
            self.option_vars.append(var)
            checkbox = ctk.CTkCheckBox(self.frame, text=option, variable=var, onvalue="on", offvalue="off", font=('Times', 16), checkbox_width=15, checkbox_height=15)
            checkbox.place(x=10, y=240 + i * 30)
        self.numDog_var = ctk.IntVar()
        self.numDog_var.set(1)
        self.numDog_Entry = ctk.CTkEntry(self.frame, width=60, height=25, font=('Times', 16), textvariable=self.numDog_var)
        self.numDog_label = ctk.CTkLabel(self.frame, text='匹', font=('Times', 16))
        self.dogoneSpa_label = ctk.CTkLabel(self.frame, text='スパ', font=('Times', 16))
        self.radio_vars = ctk.StringVar(value='unuse')
        self.dogoneSpaUse_label = ctk.CTkRadioButton(self.frame, text='利用する', font=('Times', 16), variable=self.radio_vars, value='use')
        self.dogoneSpaUnUse_label = ctk.CTkRadioButton(self.frame, text='利用しない', font=('Times', 16), variable=self.radio_vars, value='unuse')
        # 部屋追加ボタン
        self.add_room_button = ctk.CTkButton(self.frame, text='部屋の追加', font=('Times', 16), width=80, height=30, command=self.add_room_event)
        self.add_room_button.place(x=300, y=510)
        # 更新メソッドの呼び出し
        self.update_numChild_menu("1")


    def update_numChild_menu(self, about_value):
        try:
            # 大人の人数を取得
            numAdult = int(about_value)
            # 小学生の選択肢の更新
            numChild_max = 6 - numAdult
            new_numChild_menu = [str(i) for i in range(numChild_max + 1)]
            cur_numChild = self.numChild_Entry.get()
            self.numChild_Entry.configure(values=new_numChild_menu)
            # 現在の選択が新しい範囲を超えている場合は、最大値に設定
            if int(cur_numChild) > numChild_max:
                self.numChild_Entry.set(str(numChild_max))
        except Exception as e:
            print(f"Error updating child options: {e}")

    
    def check_option(self):  # オプション選択の有無のチェック、金額の計算
        # チェックボックスのフラグ
        checkin_selected = False
        bedrockButh_selected = False
        petergolf_selected = False
        pardgolf_selected = False
        tennis_selected = False
        hotSpringRental_selected = False
        dogone_selected = False
        # 人数の取得
        self.numAdult = int(self.numAdult_Entry.get())
        self.numChild = int(self.numChild_Entry.get())
        # 入力中に宿泊数を空文字にしないためのtry-except
        try:
            self.numStay = self.numStay_Entry.get()
            if self.numStay == '':
                self.numStay = 1
        except Exception as e:
            self.numStay = 1
        # プランの取得
        self.room = self.room_Entry.get()
        self.dinner = self.dinner_Entry.get()
        self.plan = self.calc_price(self.room, self.dinner)
        self.planPrace_Adult = self.plan[0]
        self.planPrace_Child = self.plan[1]
        # 大人と小学生の合計人数を計算する
        self.numPeople = self.numAdult + self.numChild
        # チェックボックスの判定
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
        # 土曜日チェックイン料金
        if checkin_selected:
            self.checkin_option = 2200 * self.numPeople
        else:
            self.checkin_option = 0
        # 岩盤浴料金
        if bedrockButh_selected:
            self.bedrockButh_option = 1500 * self.numPeople
        else:
            self.bedrockButh_option = 0
        # パターゴルフ料金
        if petergolf_selected:
            self.peterAdult_option = 500 * self.numAdult
            self.peterChild_option = 250 * self.numChild
        else:
            self.peterAdult_option = 0
            self.peterChild_option = 0
        # パークゴルフ料金
        if pardgolf_selected:
            self.parkAdult_option = 600 * self.numAdult
            self.parkChild_option = 300 * self.numChild
        else:
            self.parkAdult_option = 0
            self.parkChild_option = 0
        # テニスコート利用料金
        if tennis_selected:
            self.tennis_option = 1000 * self.numPeople
        else:
            self.tennis_option = 0
        # 温泉貸し切り料金
        if hotSpringRental_selected:
            self.hotSpringRental_option = 2500 * self.numPeople
        else:
            self.hotSpringRental_option = 0
        # ドッグワン料金
        if dogone_selected:
            self.numDog_Entry.place(x=130, y=420)
            self.numDog_label.place(x=195, y=420)
            self.dogoneSpa_label.place(x=130, y=460)
            self.dogoneSpaUse_label.place(x=170, y=460)
            self.dogoneSpaUnUse_label.place(x=170, y=490)
            # 犬の数の入力中に空文字にしないためのtry-except
            try:
                self.numDog = self.numDog_var.get()
                if self.numDog == '':
                    self.numDog = 1
            except Exception as e:
                self.numDog = 1
            # 料金の計算
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
        # 金額のリストの更新
        try:
            self.numAdult_list[self.room_cnt-1] = self.numAdult
            self.numChild_list[self.room_cnt-1] = self.numChild
            self.numStay_list[self.room_cnt-1] = self.numStay
            self.room_list[self.room_cnt-1] = self.room
            self.dinner_list[self.room_cnt-1] = self.dinner
            self.planPrace_Adult_list[self.room_cnt-1] = self.planPrace_Adult
            self.planPrace_Child_list[self.room_cnt-1] = self.planPrace_Child
            self.checkin_option_list[self.room_cnt-1] = self.checkin_option
            self.bedrockButh_option_list[self.room_cnt-1] = self.bedrockButh_option
            self.peterAdult_option_list[self.room_cnt-1] = self.peterAdult_option
            self.peterChild_option_list[self.room_cnt-1] = self.peterChild_option
            self.parkAdult_option_list[self.room_cnt-1] = self.parkAdult_option
            self.parkChild_option_list[self.room_cnt-1] = self.parkChild_option
            self.tennis_option_list[self.room_cnt-1] = self.tennis_option
            self.hotSpringRental_option_list[self.room_cnt-1] = self.hotSpringRental_option
            self.dogone_option_list[self.room_cnt-1] = self.dogone_option
            self.numDog_list[self.room_cnt-1] = self.numDog
            self.dogoneSpa_option_list[self.room_cnt-1] = self.dogoneSpa_option
        except:
            self.numAdult_list.insert(self.room_cnt-1, self.numAdult)
            self.numChild_list.insert(self.room_cnt-1, self.numChild)
            self.numStay_list.insert(self.room_cnt-1, self.numStay)
            self.room_list.insert(self.room_cnt-1, self.room)
            self.dinner_list.insert(self.room_cnt-1, self.dinner)
            self.planPrace_Adult_list.insert(self.room_cnt-1, self.planPrace_Adult)
            self.planPrace_Child_list.insert(self.room_cnt-1, self.planPrace_Child)
            self.checkin_option_list.insert(self.room_cnt-1, self.checkin_option)
            self.bedrockButh_option_list.insert(self.room_cnt-1, self.bedrockButh_option)
            self.peterAdult_option_list.insert(self.room_cnt-1, self.peterAdult_option)
            self.peterChild_option_list.insert(self.room_cnt-1, self.peterChild_option)
            self.parkAdult_option_list.insert(self.room_cnt-1, self.parkAdult_option)
            self.parkChild_option_list.insert(self.room_cnt-1, self.parkChild_option)
            self.tennis_option_list.insert(self.room_cnt-1, self.tennis_option)
            self.hotSpringRental_option_list.insert(self.room_cnt-1, self.hotSpringRental_option)
            self.dogone_option_list.insert(self.room_cnt-1, self.dogone_option)
            self.numDog_list.insert(self.room_cnt-1,self.numDog)
            self.dogoneSpa_option_list.insert(self.room_cnt-1,self.dogoneSpa_option)
        # 毎秒チェックする
        self.master.after(1000, self.check_option)


    def calc_price(self, room, dinner):  # 部屋と夕食から料金を出す
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


    def add_room_event(self):
        # 部屋数のインクリメント
        self.room_cnt += 1
        # 新しいフレームを作る
        self.create_widget()


    def confirmed_info(self):  # 確定ボタンイベント
        print(self.numAdult_list)
        print(self.numChild_list)
        print(self.numStay_list)
        print(self.room_list)
        print(self.dinner_list)
        print(self.planPrace_Adult_list)
        print(self.planPrace_Child_list)
        print(self.checkin_option_list)
        print(self.bedrockButh_option_list)
        print(self.peterAdult_option_list)
        print(self.peterChild_option_list)
        print(self.parkAdult_option_list)
        print(self.parkChild_option_list)
        print(self.tennis_option_list)
        print(self.hotSpringRental_option_list)
        print(self.dogone_option_list)
        print(self.numDog_list)
        
        from auth import pagemove_entrystay_quotationstay
        for widget in self.master.winfo_children():
            widget.destroy()
        pagemove_entrystay_quotationstay(self.master, self.name, self.email, self.numAdult_list, self.numChild_list, self.numStay_list, self.room_list, self.dinner_list, self.planPrace_Adult_list, self.planPrace_Child_list, self.checkin_option_list, self.bedrockButh_option_list, self.peterAdult_option_list, self.peterChild_option_list, self.parkAdult_option_list, self.parkChild_option_list, self.tennis_option_list, self.hotSpringRental_option_list, self.dogone_option_list,self.numDog_list,self.dogoneSpa_option_list)

if __name__ == '__main__':
    root = ctk.CTk()
    app = EntryStay(root, name='aaa', email='aaa')
    root.mainloop()