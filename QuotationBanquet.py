import customtkinter as ctk
from tkinter import messagebox

class QuotationStay(ctk.CTkFrame):
    def __init__(self, master,name, email,all_num,courcename,courcemoney,staynum,roomgrade1,roomgrade2,roomgrade1num,roomgrade2num,nominum,nomitime,add_menu1,add_menu2,add_menu3,menu1_num,menu2_num,menu3_num,nijikai_plan,nijikai_num,nijikai_money,staymoney,nostaymoney,nomitotal,nijikaitotal,roomgrade1total,roomgrade2total,add_menu1_total,add_menu2_total,add_menu3_total,Banquettotal):
        
        super().__init__(master)
        # お客様情報
        self.name = name
        self.email = email
        
        self.all_num = all_num
        # コース
        self.cource_name = courcename
        self.cource_money = courcemoney
        # 宿泊人数
        self.staynum = staynum
        
        self.staymoney = staymoney
        self.nostaymoney = nostaymoney
        
        # お部屋グレード
        self.roomgrade_money1 = roomgrade1total
        self.roomgrade1_num = roomgrade1num
        self.roomgrade2_money = roomgrade2total
        self.roomgrade2_num = roomgrade2num
        # 飲み放題
        self.nominum = nominum
        self.nomitime = nomitime
        self.nomitotal = nomitotal
        # 追加料理
        self.add_menu1_money = add_menu1_total
        self.add_menu2_money = add_menu2_total
        self.add_menu3_money = add_menu3_total
        self.add_menu1 = add_menu1
        self.add_menu2 = add_menu2
        self.add_menu3 = add_menu3
        # 二次会
        self.nijikai_plan = nijikai_plan
        self.nijikai_num = nijikai_num
        self.niji_money = nijikaitotal
        
        # 合計金額
        self.banquet_total = Banquettotal
        
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
        frame = ctk.CTkFrame(scrollable_frame, fg_color="transparent", height=750)
        frame.pack(fill="both", expand=True)
        frame.pack_propagate(False)

        # 見積り結果の表示
        self.result_label = ctk.CTkLabel(frame, text='お見積り結果', font=('Times', 20))
        self.result_label.place(x=60, y=20)
        self.result = ctk.CTkLabel(frame, text=f'{self.banquet_total}円', font=('Times', 20))
        self.result.place(x=210, y=20)
        
        # 詳細の表示
        self.breakdown_label = ctk.CTkLabel(frame, text='詳細', font=('Times', 20))
        self.breakdown_label.place(x=60, y=80)
        
        self.numPeople_label = ctk.CTkLabel(frame, text=f'人数（ご宿泊になるお客様／お帰りになるお客様）　{self.all_num}名様（{self.staynum}名／{self.all_num-self.staynum}名）', font=('Times', 16))
        self.numPeople_label.place(x=100, y=120)    

        self.cource_label = ctk.CTkLabel(frame, text=f'コース　{self.cource_name}　　　一人当たり{self.cource_money}円', font=('Times', 16))
        self.cource_label.place(x=100, y=160)
        
        self.staynum_label = ctk.CTkLabel(frame, text=f'ご宿泊になるお客様　［ {self.staynum}名 ］', font=('Times', 16))
        self.staynum_label.place(x=100, y=200)
        
        self.nostaynum_label = ctk.CTkLabel(frame, text=f'お帰りになるお客様　［ {self.all_num-self.staynum}名 ］', font=('Times', 16))
        self.nostaynum_label.place(x=100, y=230)
        
        self.stay_prace = ctk.CTkLabel(frame, text=f'　 {self.staymoney}円', font=('Times', 16))
        self.stay_prace.place(relx=1.0, x=-100, y=210, anchor='e')
        
        self.nostay_prace = ctk.CTkLabel(frame, text=f' 　{self.nostaymoney}円', font=('Times', 16))
        self.nostay_prace.place(relx=1.0, x=-100, y=245, anchor='e')
        
        # オプション
        self.op_label = ctk.CTkLabel(frame, text='オプション', font=('Times', 24))
        self.op_label.place(x=100, y=285)
        
        self.grade1_label = ctk.CTkLabel(frame, text=f'お部屋グレードアップ1[ 岩手山展望露天風呂付和室 ] [ {self.roomgrade1_num}名 ]', font=('Times', 16))
        self.grade1_label.place(x=100, y=325)
        self.grade1_prace = ctk.CTkLabel(frame, text=f'{self.roomgrade_money1}円', font=('Times', 16))
        self.grade1_prace.place(relx=1.0, x=-100, y=340, anchor='e')

        self.grade2_label = ctk.CTkLabel(frame, text=f'お部屋グレードアップ2[ 檜の内風呂付和洋室 ] [ {self.roomgrade2_num}名 ]', font=('Times', 16))
        self.grade2_label.place(x=100, y=365)
        self.grade2_price = ctk.CTkLabel(frame, text=f'{self.roomgrade2_money}円', font=('Times', 16))
        self.grade2_price.place(relx=1.0, x=-100, y=380, anchor='e')
        
        self.nomi_label = ctk.CTkLabel(frame, text=f'飲み放題 [ {self.nominum}名 {self.nomitime}時間 ]', font=('Times', 16))
        self.nomi_label.place(x=100, y=435)
        self.nomi_prace = ctk.CTkLabel(frame, text=f'{self.nomitotal}円', font=('Times', 16))
        self.nomi_prace.place(relx=1.0, x=-100, y=450, anchor='e')
        

        self.add_menu1_label = ctk.CTkLabel(frame, text=f'追加料理　八幡平牛ロースのしゃぶしゃぶ [ {self.add_menu1} 名様分 ]', font=('Times', 16))
        self.add_menu1_label.place(x=100, y=505)
        self.add_menu1_prace = ctk.CTkLabel(frame, text=f'{self.add_menu1_money}円', font=('Times', 16))
        self.add_menu1_prace.place(relx=1.0, x=-100, y=520, anchor='e')

        self.add_menu2_label = ctk.CTkLabel(frame, text=f'追加料理　大更ホルモン鍋 [ {self.add_menu2} × 二名様分 ]', font=('Times', 16))
        self.add_menu2_label.place(x=100, y=545)
        self.add_menu2_prace = ctk.CTkLabel(frame, text=f'{self.add_menu2_money}円', font=('Times', 16))
        self.add_menu2_prace.place(relx=1.0, x=-100, y=560, anchor='e')

        self.add_menu3_label = ctk.CTkLabel(frame, text=f'追加料理　岩手県産牛の串焼き [ {self.add_menu3} 本 ]', font=('Times', 16))
        self.add_menu3_label.place(x=100, y=585)
        self.add_menu3_prace = ctk.CTkLabel(frame, text=f'{self.add_menu3_money}円', font=('Times', 16))
        self.add_menu3_prace.place(relx=1.0, x=-100, y=600, anchor='e')
        
        self.niji_label = ctk.CTkLabel(frame, text=f'二次会 [ {self.nijikai_plan} プラン ] [ {self.nijikai_num} 名 ]', font=('Times', 16))
        self.niji_label.place(x=100, y=665)
        self.niji_prace = ctk.CTkLabel(frame, text=f'{self.niji_money}円', font=('Times', 16))
        self.niji_prace.place(relx=1.0, x=-100, y=680, anchor='e')
        
        # 横線を引く
        line = ctk.CTkFrame(frame, height=2, width=620, fg_color="gray")
        line.place(x=80, y=705)
        # 合計
        self.total_label = ctk.CTkLabel(frame, text='合計', font=('Times', 16))
        self.total_label.place(x=100, y=710)
        self.total_prace = ctk.CTkLabel(frame, text=f'{self.banquet_total}円', font=('Times', 16))
        self.total_prace.place(relx=1.0, x=-100, y=725, anchor='e')
        
    def change_button_event(self):
        a=1
        # from EntryBanquet import Enkai_Input
        # self.destroy()
        # Enkai_Input(self.master,self.name,self.email)
    
    def confirm_button_event(self):
        self.storage = messagebox.askyesnocancel('データ保存', '見積り内容をjsonファイルに保存しますか？')
        if self.storage:
            pass
        else:
            pass
        self.send_mail = messagebox.askyesno('メール送信', f'見積り結果を送信しますか？\n{self.email}に送信')
        if self.send_mail:
            pass
        else:
            pass
    
if __name__ == '__main__':
    root = ctk.CTk()
    app = QuotationStay(root, name="ww", email="qwe",all_num=2,courcename="豪華コース",courcemoney=21600,staynum=1,roomgrade1=0,roomgrade2=0,roomgrade1num=0,roomgrade2num=0,nominum=0,nomitime=0,add_menu1=0,add_menu2=0,add_menu3=0,menu1_num=0,menu2_num=0,menu3_num=0,nijikai_plan="未選択",nijikai_num=0,nijikai_money=0,staymoney=21600,nostaymoney=0,nomitotal=0,nijikaitotal=0,roomgrade1total=0,roomgrade2total=0,add_menu1_total=0,add_menu2_total=0,add_menu3_total=0,Banquettotal=int(21600+0.7*(21600)))
    root.mainloop()
