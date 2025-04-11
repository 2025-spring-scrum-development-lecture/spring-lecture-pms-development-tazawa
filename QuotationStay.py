import customtkinter as ctk
from tkinter import messagebox

class QuotationStay(ctk.CTkFrame):
    def __init__(self, master, name, email, numAdult, numChild, numStay, room, dinner, planPrace_Adult, planPrace_Child, checkin_option, bedrockButh_option, peterAdult_option, peterChild_option, parkAdult_option, parkChild_option, tennis_option, hotSpringRental_option, dogone_option, numDog, dogoneSpa , total):
        
        super().__init__(master)
        
        self.master = master
        self.name = name
        self.email = email
        self.numAdult = numAdult
        self.numChild = numChild
        self.numPeople = numAdult + numChild
        self.numStay = numStay
        self.room = room
        self.dinner = dinner
        self.planPrace_Adult = planPrace_Adult
        self.planPrace_Child = planPrace_Child
        self.checkin_option = checkin_option
        self.bedrockButh_option = bedrockButh_option
        self.peterAdult_option = peterAdult_option
        self.peterChild_option = peterChild_option
        self.parkAdult_option = parkAdult_option
        self.parkChild_option = parkChild_option
        self.tennis_option = tennis_option
        self.hotSpringRental_option = hotSpringRental_option
        self.dogone_option = dogone_option
        self.total = total
        
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        master.geometry(f'{screen_width}x{screen_height}')
        master.title('入力内容の確認')

        ctk.set_appearance_mode("Light")
        ctk.set_default_color_theme("green")
        
        self.create_widget()
        
    def create_widget(self):
        # ゲストの名前とメールアドレスの表示
        self.guest_label = ctk.CTkLabel(self.master, text=f'{self.name}様〖{self.email}〗', font=('Times', 20))
        self.guest_label.place(x=20, y=10)
        # 入力内容の変更ボタン
        self.change_button = ctk.CTkButton(self.master, text='入力に戻る', font=('Times', 16), width=170, height=40, command=self.change_button_event)
        self.change_button.place(x=900, y=10)
        # データ保存ボタン
        self.confirm_button = ctk.CTkButton(self.master, text='確定してTopへ', font=('Times', 16), width=170, height=40, command=self.confirm_button_event)
        self.confirm_button.place(x=1080, y=10)
        
        # ベースフレームの作成(表示サイズの固定)
        base_frame = ctk.CTkFrame(self.master, width=800, height=550)
        base_frame.place(x=250, y=60)
        base_frame.pack_propagate(False)
        # スクロールフレームの作成(スクロール機能の追加)
        scrollable_frame = ctk.CTkScrollableFrame(base_frame, width=800, height=550)
        scrollable_frame.pack(fill="both", expand=True)
        # 内部フレームの作成(レイアウト用)
        frame = ctk.CTkFrame(scrollable_frame, fg_color="transparent", height=700)
        frame.pack(fill="both", expand=True)
        frame.pack_propagate(False)

        # 見積り結果の表示
        self.result_label = ctk.CTkLabel(frame, text='お見積り結果', font=('Times', 20))
        self.result_label.place(x=60, y=20)
        self.result = ctk.CTkLabel(frame, text=f'{self.total}円', font=('Times', 20))
        self.result.place(x=210, y=20)
        
        # 詳細の表示
        self.breakdown_label = ctk.CTkLabel(frame, text='詳細', font=('Times', 20))
        self.breakdown_label.place(x=60, y=80)
        # 人数（大人／小学生）
        self.numPeople_label = ctk.CTkLabel(frame, text=f'人数（大人／小学生）　{self.numPeople}名様（{self.numAdult}名／{self.numChild}名）', font=('Times', 16))
        self.numPeople_label.place(x=100, y=120)    
        # 泊数
        self.numStay_label = ctk.CTkLabel(frame, text=f'泊数　{self.numStay}泊', font=('Times', 16))
        self.numStay_label.place(x=100, y=160)
        # プラン
        self.planroom_label = ctk.CTkLabel(frame, text=f'プラン　お部屋［ {self.room} ］', font=('Times', 16))
        self.planroom_label.place(x=100, y=200)
        self.plandinner_label = ctk.CTkLabel(frame, text=f'ご夕食［ {self.dinner} ］', font=('Times', 16))
        self.plandinner_label.place(x=162, y=230)
        self.planPrace_Adult_prace = ctk.CTkLabel(frame, text=f'大人 {self.planPrace_Adult * self.numAdult}円', font=('Times', 16))
        self.planPrace_Adult_prace.place(relx=1.0, x=-100, y=230, anchor='e')
        self.planPrace_Child_prace = ctk.CTkLabel(frame, text=f'小学生 {self.planPrace_Child * self.numChild}円', font=('Times', 16))
        self.planPrace_Child_prace.place(relx=1.0, x=-100, y=260, anchor='e')
        # 土曜日チェックイン
        self.checkin_option_label = ctk.CTkLabel(frame, text='土曜日チェックイン', font=('Times', 16))
        self.checkin_option_label.place(x=100, y=285)
        self.checkin_option_prace = ctk.CTkLabel(frame, text=f'{self.checkin_option}円', font=('Times', 16))
        self.checkin_option_prace.place(relx=1.0, x=-100, y=300, anchor='e')
        # 岩盤浴
        self.bedrockButh_option_label = ctk.CTkLabel(frame, text='岩盤浴', font=('Times', 16))
        self.bedrockButh_option_label.place(x=100, y=325)
        self.bedrockButh_option_prace = ctk.CTkLabel(frame, text=f'{self.bedrockButh_option}円', font=('Times', 16))
        self.bedrockButh_option_prace.place(relx=1.0, x=-100, y=340, anchor='e')
        # パターゴルフ
        self.petergolf_option_label = ctk.CTkLabel(frame, text='パターゴルフ', font=('Times', 16))
        self.petergolf_option_label.place(x=100, y=365)
        self.peterAdult_option_price = ctk.CTkLabel(frame, text=f'大人{self.peterAdult_option}円', font=('Times', 16))
        self.peterAdult_option_price.place(relx=1.0, x=-100, y=380, anchor='e')
        self.peterChild_option_price = ctk.CTkLabel(frame, text=f'小学生{self.peterChild_option}円', font=('Times', 16))
        self.peterChild_option_price.place(relx=1.0, x=-100, y=410, anchor='e')
        # パークゴルフ
        self.parkgolf_option_label = ctk.CTkLabel(frame, text='パークゴルフ', font=('Times', 16))
        self.parkgolf_option_label.place(x=100, y=435)
        self.parkAdult_option_prace = ctk.CTkLabel(frame, text=f'大人{self.parkAdult_option}円', font=('Times', 16))
        self.parkAdult_option_prace.place(relx=1.0, x=-100, y=450, anchor='e')
        self.parkChild_option_prace = ctk.CTkLabel(frame, text=f'小学生{self.parkChild_option}円', font=('Times', 16))
        self.parkChild_option_prace.place(relx=1.0, x=-100, y=480, anchor='e')
        # テニスコート利用
        self.tennis_option_label = ctk.CTkLabel(frame, text='テニスコート', font=('Times', 16))
        self.tennis_option_label.place(x=100, y=505)
        self.tennis_option_prace = ctk.CTkLabel(frame, text=f'{self.tennis_option}円', font=('Times', 16))
        self.tennis_option_prace.place(relx=1.0, x=-100, y=520, anchor='e')
        # 温泉貸し切り
        self.hotSpringRental_option_label = ctk.CTkLabel(frame, text='温泉貸し切り', font=('Times', 16))
        self.hotSpringRental_option_label.place(x=100, y=545)
        self.hotSpringRental_option_prace = ctk.CTkLabel(frame, text=f'{self.hotSpringRental_option}円', font=('Times', 16))
        self.hotSpringRental_option_prace.place(relx=1.0, x=-100, y=560, anchor='e')
        # ドッグワン
        self.dogone_option_label = ctk.CTkLabel(frame, text='ドッグワン', font=('Times', 16))
        self.dogone_option_label.place(x=100, y=585)
        self.dogone_option_prace = ctk.CTkLabel(frame, text=f'{self.dogone_option}円', font=('Times', 16))
        self.dogone_option_prace.place(relx=1.0, x=-100, y=600, anchor='e')
        # 横線を引く
        line = ctk.CTkFrame(frame, height=2, width=620, fg_color="gray")
        line.place(x=80, y=620)
        # 合計
        self.total_label = ctk.CTkLabel(frame, text='合計', font=('Times', 16))
        self.total_label.place(x=100, y=630)
        self.total_prace = ctk.CTkLabel(frame, text=f'{self.total}円', font=('Times', 16))
        self.total_prace.place(relx=1.0, x=-100, y=642, anchor='e')
        
    def change_button_event(self):  # 入力画面に戻るイベント
        self.destroy()
        # from auth import
    
    def confirm_button_event(self):  # 確定ボタンのイベント(データ保存、メール送信、Topページへ)
        self.storage = messagebox.askyesnocancel('データ保存', '見積り内容をjsonファイルに保存しますか？')
        if self.storage:
            from auth import stay_estimate_data
        else:
            pass
        self.send_mail = messagebox.askyesno('メール送信', f'見積り結果を送信しますか？\n{self.email}に送信')
        if self.send_mail:
            from auth import Stay_Send_email 
            Stay_Send_email( self.name, self.email, self.numAdult_list, self.numChild_list, self.numStay_list, self.room_list, self.dinner_list, self.planPrace_Adult_list, self.planPrace_Child_list, self.checkin_option_list, self.bedrockButh_option_list, self.peterAdult_option_list, self.peterChild_option_list, self.parkAdult_option_list, self.parkChild_option_list, self.tennis_option_list, self.hotSpringRental_option_list, self.dogone_option_list,self.numDog_list,self.dogoneSpa_option_list)
    
            for widget in self.master.winfo_children():
                widget.destroy()
                
        else:
            pass
    
if __name__ == '__main__':
    root = ctk.CTk()
    app = QuotationStay(root, name='aaa', email='aaa', numAdult=2, numChild=2, numStay=1, room='西館和洋室',dinner='スタンダード', planPrace_Adult=0, planPrace_Child=0, checkin_option=0, bedrockButh_option=0, peterAdult_option=0, peterChild_option=0, parkAdult_option=0, parkChild_option=0, tennis_option=0, hotSpringRental_option=0, dogone_option=0, total=0)
    root.mainloop()