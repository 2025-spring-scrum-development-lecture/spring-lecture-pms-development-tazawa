import customtkinter as ctk
from tkinter import messagebox

class QuotationStay(ctk.CTkFrame):
    def __init__(self, master, name, email, numAdult, numChild, numStay, room, dinner, planPrace_Adult, planPrace_Child, checkin_option, bedrockButh_option, peterAdult_option, peterChild_option, parkAdult_option, parkChild_option, tennis_option, hotSpringRental_option, dogone_option, numDog, dogoneSpa , total):
        
        super().__init__(master)
        
        self.master = master
        self.name = name
        self.email = email
        self.numAdult_list = [int(num) for num in numAdult]
        self.numChild_list = [int(num) for num in numChild]
        # self.numPeople_list = numAdult + numChild
        self.numStay_list = [int(num) for num in numStay]
        self.room_list = room
        self.dinner_list = dinner
        self.planPrace_Adult_list = [int(num) for num in planPrace_Adult]
        self.planPrace_Child_list = [int(num) for num in planPrace_Child]
        self.checkin_option_list = [int(num) for num in checkin_option]
        self.bedrockButh_option_list = [int(num) for num in bedrockButh_option]
        self.peterAdult_option_list = [int(num) for num in peterAdult_option]
        self.peterChild_option_list = [int(num) for num in peterChild_option]
        self.parkAdult_option_list = [int(num) for num in parkAdult_option]
        self.parkChild_option_list = [int(num) for num in parkChild_option]
        self.tennis_option_list = [int(num) for num in tennis_option]
        self.hotSpringRental_option_list = [int(num) for num in hotSpringRental_option]
        self.dogone_option_list = [int(num) for num in dogone_option]
        self.numDog_list = [int(num) for num in numDog]
        self.dogoneSpa_option_list = [int(num) for num in dogoneSpa]
        self.total_list = [int(num) for num in total]
        
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
        self.change_button = ctk.CTkButton(self.master, text='入力に戻る', font=('Times', 16), width=170, height=30, command=self.change_button_event)
        self.change_button.place(x=900, y=10)
        # データ保存ボタン
        self.confirm_button = ctk.CTkButton(self.master, text='確定してTopへ', font=('Times', 16), width=170, height=30, command=self.confirm_button_event)
        self.confirm_button.place(x=1080, y=10)
        # ベースフレームの作成(表示サイズの固定)
        base_frame = ctk.CTkFrame(self.master, width=880, height=500)
        base_frame.place(x=210, y=120)
        base_frame.pack_propagate(False)
        # スクロールフレームの作成(スクロール機能の追加)
        scrollable_frame = ctk.CTkScrollableFrame(base_frame, width=880, height=500)
        scrollable_frame.pack(fill="both", expand=True)
        # 内部フレームの作成(レイアウト用)
        self.frame = ctk.CTkFrame(scrollable_frame, fg_color="transparent", height=500)
        self.frame.pack(fill="both", expand=True)
        self.frame.pack_propagate(False)
        # 見積結果の表示
        self.totalresult = ctk.CTkLabel(self.master, text=f'合計金額:{sum(self.total_list)}円', font=('Times', 20))
        self.totalresult.place(x=210, y=80)
        # テキストの作成
        self.text = ''
        text = self.create_text()
        # 詳細を表示
        result_label = ctk.CTkLabel(self.frame, text=text, font=('Times', 16), anchor="w", justify="left", padx=0, pady=0)
        result_label.place(x=20, y=20)
        # ここでフレームの高さを動的に調整
        self.frame.update_idletasks()
        text_height = result_label.winfo_height()
        # フレームの高さを動的に設定
        self.frame.configure(height=text_height)
        
    def create_text(self):
        for i in range(len(self.room_list)):
            if i == 0:
                self.text += f'{i+1}部屋目　{self.total_list[i]}円\n'
            else:
                self.text += f'\n\n{i+1}部屋目　{self.total_list[i]}円\n'
            self.text += f'【人数】{self.numAdult_list[i]+self.numChild_list[i]}名（大人{self.numAdult_list[i]}名／小学生{self.numChild_list[i]}名）\n'
            self.text += f'【ご宿泊】{self.numStay_list[i]}泊\n'
            self.text += f'【お部屋<{self.room_list[i]}> × 夕食<{self.dinner_list[i]}> プラン】　{self.planPrace_Adult_list[i]+self.planPrace_Child_list[i]}円（大人:{self.planPrace_Adult_list[i]}円／小学生:{self.planPrace_Child_list[i]}円）\n'
            self.text += f'【土曜日チェックインの追加料金】　{self.checkin_option_list[i]}円\n'
            self.text += f'【岩盤浴】　{self.bedrockButh_option_list[i]}円\n'
            self.text += f'【パターゴルフ】　{self.peterAdult_option_list[i]+self.peterChild_option_list[i]}円（大人:{self.peterAdult_option_list[i]}円／小学生:{self.peterChild_option_list[i]}円）\n'
            self.text += f'【パークゴルフ】　{self.parkAdult_option_list[i]+self.parkChild_option_list[i]}円（大人:{self.parkAdult_option_list[i]}円／小学生:{self.parkChild_option_list[i]}円）\n'
            self.text += f'【テニスコート利用】 {self.tennis_option_list[i]}円\n'
            self.text += f'【温泉貸し切り】{self.hotSpringRental_option_list[i]}円\n'
            self.text += f'【ドッグワン】　{self.dogone_option_list[i]}円（{self.numDog_list[i]}匹、ケージ代:{self.numDog_list[i]*1000}円／スパ利用料金:{self.dogoneSpa_option_list[i]}）'
        return self.text
            
    def change_button_event(self):  # 入力画面に戻るイベント
        pass
    
    def confirm_button_event(self):  # 確定ボタンのイベント(データ保存、メール送信、Topページへ)
        self.storage = messagebox.askyesno('データ保存', '見積り内容をjsonファイルに保存しますか？')
        if self.storage == True:
            from auth import stay_estimate_data
            stay_estimate_data(self.name, self.email, self.numAdult_list, self.numChild_list, self.numStay_list, self.room_list, self.dinner_list, self.planPrace_Adult_list, self.planPrace_Child_list, self.checkin_option_list, self.bedrockButh_option_list, self.peterAdult_option_list, self.peterChild_option_list, self.parkAdult_option_list, self.parkChild_option_list, self.tennis_option_list, self.hotSpringRental_option_list, self.dogone_option_list, self.numDog_list, self.dogoneSpa_option_list, self.total_list)
        elif self.storage == False:
            pass
        # elif self.storage == None:
            # self.create_widget()
            pass
        self.send_mail = messagebox.askyesno('メール送信', f'見積り結果を送信しますか？\n{self.email}に送信')
        if self.send_mail:
            from auth import Stay_Send_email 
            Stay_Send_email( self.name, self.email, self.numAdult_list, self.numChild_list, self.numStay_list, self.room_list, self.dinner_list, self.planPrace_Adult_list, self.planPrace_Child_list, self.checkin_option_list, self.bedrockButh_option_list, self.peterAdult_option_list, self.peterChild_option_list, self.parkAdult_option_list, self.parkChild_option_list, self.tennis_option_list, self.hotSpringRental_option_list, self.dogone_option_list,self.numDog_list,self.dogoneSpa_option_list, self.total_list)               
        else:
            pass
        # from auth import reset_quotationstay_entry
        # reset_quotationstay_entry(self.master)
        for widget in self.master.winfo_children():
                widget.destroy()
        import sys
        sys.exit()
        
    
if __name__ == '__main__':
    root = ctk.CTk()
    app = QuotationStay(root)
    root.mainloop()