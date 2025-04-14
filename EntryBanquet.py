import customtkinter as ctk
from tkinter import messagebox as msb
class Enkai_Input(ctk.CTkFrame):
    def __init__(self, master, name, email):
        super().__init__(master, width=500, height=645)
        self.master = master
        self.pack()
        self.master.state('zoomed')
        ctk.set_appearance_mode("Light")
        ctk.set_default_color_theme("green")
        master.title('宴会---入力画面')
        
        self.customer_name = name
        self.customer_email = email
        self.create_widgets()
        
    def create_widgets(self):
        self.cuslabel = ctk.CTkLabel(self,text=f"{self.customer_name}様 ",font=("Times",16,"bold"))
        self.cuslabel.place(x=30,y=1)
        
        self.return_btn = ctk.CTkButton(self,text=" ↩ ",font=("Times",16,"bold"),width=10,height=10,fg_color="coral",hover_color="#CC4E39",command=self.return_toppage)
        self.return_btn.place(x=1,y=3)
        
        self.unl = ctk.CTkLabel(self,text="_________________________________________________________________________________",text_color="#33aa33")
        self.unl.place(x=10,y=39)
        self.l = ctk.CTkLabel(self,text="宴会",font=("Times",30,"bold"))
        self.l.place(x=35,y=26)
        
        self.l1 = ctk.CTkLabel(self,text="人数",font=("Times",16,"bold"))
        self.l1.place(x=25,y=60)
        self.np = [2,10,20,30,40,50,100,200]
        self.np_combo = ctk.CTkComboBox(self,values=[str(num)for num in self.np],border_color="#62D176",button_color="#62D176",button_hover_color="green",\
            command=self.np_sp)
        self.np_combo.place(x=10,y=90)
        
        self.l2 = ctk.CTkLabel(self,text="コース",font=("Times",16,"bold"))
        self.l2.place(x=9,y=130)
        course = ["豪華コース","雅コース","錦コース","椿コース"]
        self.crs_combo = ctk.CTkComboBox(self,values=[str(num)for num in course],state='readonly',font=("Times",12,"bold"),border_color="#62D176",button_color="#62D176",button_hover_color="green")
        self.crs_combo.place(x=10,y=160)
        self.crs_combo.set("未選択")
        
        self.l3 = ctk.CTkLabel(self,text="宿泊が必要な人数",font=("Times",16,"bold"))
        self.l3.place(x=240,y=60)
        # サイトで絞り込みするときの人数(1~10)
        self.np = [0,1,2,3,4,5,6,7,8,9,10]
        self.stay_num_conbo = ctk.CTkComboBox(self,values=[str(i) for i in range(int(self.np_combo.get())+1)],state='normal',border_color="#62D176",button_color="#62D176",button_hover_color="green",\
            command=self.np_sp)
        self.stay_num_conbo.set(self.np_combo.get())
        self.stay_num_conbo.place(x=240,y=90)
        
        # ここからオプション
        self.unl2 = ctk.CTkLabel(self,text="_________________________________________________________________________________",text_color="#CC4E39")
        self.unl2.place(x=10,y=220)
        self.l4 = ctk.CTkLabel(self,text="オプション",font=("Times",24,"bold"))
        self.l4.place(x=20,y=220)
        self.l5 = ctk.CTkLabel(self,text="お部屋グレードアップ",font=("Times",16,"bold"))
        self.l5.place(x=9,y=250)
        # 部屋グレード１
        self.option_room_grade_status1 = ctk.BooleanVar()
        self.option_room_grade_1 = ctk.CTkCheckBox(self,text="岩手山展望露天風呂付和室",font=("Times",12,"bold"),variable=self.option_room_grade_status1,command=self.rg_num,checkbox_width=15,checkbox_height=15,)
        self.option_room_grade_1.place(x=9,y=275)
        self.roomgrade_num1 = ctk.CTkComboBox(self,values=[str(i) for i in range(1,int(self.np_combo.get())+1)],command=self.np_sp)
        self.roomgrade_num1.place(x=9,y=305)
        self.roomgrade_num1.set("0")
        self.roomgrade_num1.configure(state="disable")
        self.room_nin1 = ctk.CTkLabel(self,text="人",font=("Times",12,"bold"))
        self.room_nin1.place(x=150,y=305)
        # 部屋グレード２
        self.option_room_grade_status2 = ctk.BooleanVar()
        self.option_room_grade_2 = ctk.CTkCheckBox(self,text="檜の内風呂付和洋室",font=("Times",12,"bold"),variable=self.option_room_grade_status2,command=self.rg_num2,checkbox_width=15,checkbox_height=15,)
        self.option_room_grade_2.place(x=200,y=275)
        self.roomgrade_num2 = ctk.CTkComboBox(self,values=[str(i) for i in range(1,int(self.np_combo.get())+1)],command=self.np_sp)
        self.roomgrade_num2.place(x=200,y=305)
        self.roomgrade_num2.set("0")
        self.roomgrade_num2.configure(state="disable")
        self.room_nin2 = ctk.CTkLabel(self,text="人",font=("Times",12,"bold"))
        self.room_nin2.place(x=341,y=305)
        
        # 飲み放題
        self.l6 = ctk.CTkLabel(self,text="飲み放題",font=("Times",16,"bold"))
        self.l6.place(x=9,y=345)
        self.option_bottomless_cup_state = ctk.BooleanVar()
        self.option_bottomless_cup = ctk.CTkCheckBox(self,text="飲ん兵衛コース",font=("Times",12,"bold"),variable=self.option_bottomless_cup_state,\
            checkbox_width=15,checkbox_height=15,command=self.bottomless_cup_plan)
        self.option_bottomless_cup.place(x=80,y=348)
        
        self.bottomlesscup_num = ctk.CTkComboBox(self,values=[str(i) for i in range(1,int(self.np_combo.get())+1)],state="readonly",command=self.np_sp)
        self.bottomlesscup_num.set("0")
        self.bottomlesscup_num.configure(state="disable")
        self.bottomlesscup_num.place(x=9,y=375)
        self.label_alc_pnum = ctk.CTkLabel(self,text="人",font=("Times",12,"bold"))
        self.label_alc_pnum.place(x=150,y=375)
        
        # 二時間単位での申し込みになる
        self.bottomlesscup_hour = ctk.CTkComboBox(self,values=["2","4","6","8","10","12"],state="readonly")
        self.bottomlesscup_hour.set("0")
        self.bottomlesscup_hour.configure(state="disable")
        self.bottomlesscup_hour.place(x=200,y=375)
        self.label_alc_hour = ctk.CTkLabel(self,text="時間",font=("Times",12,"bold"))
        self.label_alc_hour.place(x=341,y=375)
          
        # 追加料理
        self.l7 = ctk.CTkLabel(self,text="追加料理",font=("Times",16,"bold"))
        self.l7.place(x=9,y=415)
        
        self.sara = [10,20,30,40,50,60,70,80,90,100,200,300]
        self.additional_dishes1_state = ctk.BooleanVar()
        self.additional_dishes1 = ctk.CTkCheckBox(self,text="八幡平牛ロースのしゃぶしゃぶ",font=("Times",12,"bold"),checkbox_width=15,checkbox_height=15,command=self.additional_dishes_add1,variable=self.additional_dishes1_state)
        self.additional_dishes_num1 = ctk.CTkComboBox(self,values=[str(num)for num in self.sara])
        self.additional_dishes_num1.set("0")
        self.additional_dishes_num1.configure(state="disable")
        self.label_additional1 = ctk.CTkLabel(self,text="名様分",font=("Times",12,"bold"))
        self.additional_dishes1.place(x=9,y=440)
        self.additional_dishes_num1.place(x=250,y=440)
        self.label_additional1.place(x=395,y=443)
        
        self.additional_dishes2_state = ctk.BooleanVar()
        self.additional_dishes2 = ctk.CTkCheckBox(self,text="大更ホルモン鍋",font=("Times",12,"bold"),checkbox_width=15,checkbox_height=15,command=self.additional_dishes_add2,variable=self.additional_dishes2_state)
        self.additional_dishes_num2 = ctk.CTkComboBox(self,values=[str(num)for num in self.sara])
        self.additional_dishes_num2.set("0")
        self.additional_dishes_num2.configure(state="disable")
        self.label_additional2 = ctk.CTkLabel(self,text="＊２名様分",font=("Times",12,"bold"))
        self.additional_dishes2.place(x=9,y=470)
        self.additional_dishes_num2.place(x=250,y=470)
        self.label_additional2.place(x=395,y=473)
        
        self.additional_dishes3_state = ctk.BooleanVar()
        self.additional_dishes3 = ctk.CTkCheckBox(self,text="岩手県産牛の串焼き",font=("Times",12,"bold"),checkbox_width=15,checkbox_height=15,command=self.additional_dishes_add3,variable=self.additional_dishes3_state)
        self.additional_dishes_num3 = ctk.CTkComboBox(self,values=[str(num)for num in self.sara])
        self.additional_dishes_num3.set("0")
        self.additional_dishes_num3.configure(state="disable")
        self.label_additional3 = ctk.CTkLabel(self,text="本",font=("Times",12,"bold"))
        self.additional_dishes3.place(x=9,y=500)
        self.additional_dishes_num3.place(x=250,y=500)
        self.label_additional3.place(x=395,y=503)
        
        # 二次会
        self.l8 = ctk.CTkLabel(self,text="二次会",font=("Times",16,"bold"))
        self.l8.place(x=9,y=530)
        self.Niji_state = ctk.BooleanVar()
        self.Nijikai = ctk.CTkCheckBox(self,text="飲み放題・カラオケ歌い放題",checkbox_width=15,checkbox_height=15,font=("Times",12,"bold"),variable=self.Niji_state,command=self.Niji_input)
        self.Nijikai.place(x=65,y=533)
        self.nplan = ["スナック3,000円","スナック2,500円","カラオケ"]
        self.Niji_plan = ctk.CTkComboBox(self,values=self.nplan,state="readonly",font=("Times",12,"bold"))
        self.Niji_plan.set("未選択")
        self.Niji_plan.configure(state="disable")
        self.Niji_plan.place(x=9,y=560)
        self.label_Niji1 = ctk.CTkLabel(self,text="コース",font=("Times",12,"bold"))
        self.label_Niji1.place(x=150,y=563)
        self.Niji_num  = ctk.CTkComboBox(self,values=[str(i) for i in range(1,int(self.np_combo.get())+1)],state="readonly",font=("Times",12,"bold"),width=90,command=self.np_sp)
        self.Niji_num.set("0")
        self.Niji_num.configure(state="disable")
        self.Niji_num.place(x=200,y=560)
        self.label_Niji2 = ctk.CTkLabel(self,text="人",font=("Times",12,"bold"))
        self.label_Niji2.place(x=290,y=563)

        # 使う宴会会場
        self.kasuga_st = ctk.BooleanVar()
        self.heian_st = ctk.BooleanVar()
        self.suehiro_st = ctk.BooleanVar()
        self.fuyo_st = ctk.BooleanVar()
        self.ran_st = ctk.BooleanVar()
        self.ganju_st = ctk.BooleanVar()
        
        self.room_label = ctk.CTkLabel(self,text="ご利用になるお部屋",font=("Times",16,"bold"))
        self.kasuga_check = ctk.CTkCheckBox(self,text="春日",font=("Times",12,"bold"),variable=self.kasuga_st,checkbox_width=15,checkbox_height=15,)
        self.heian_check = ctk.CTkCheckBox(self,text="平安",font=("Times",12,"bold"),variable=self.heian_st,checkbox_width=15,checkbox_height=15)
        self.suehiro_check = ctk.CTkCheckBox(self,text="末広",font=("Times",12,"bold"),variable=self.suehiro_st,checkbox_width=15,checkbox_height=15)
        self.fuyo_check = ctk.CTkCheckBox(self,text="芙蓉",font=("Times",12,"bold"),variable=self.fuyo_st,checkbox_width=15,checkbox_height=15)
        self.ran_check = ctk.CTkCheckBox(self,text="蘭",font=("Times",12,"bold"),variable=self.ran_st,checkbox_width=15,checkbox_height=15)
        self.ganju_check = ctk.CTkCheckBox(self,text="岩鷲",font=("Times",12,"bold"),variable=self.ganju_st,checkbox_width=15,checkbox_height=15)
        
        self.room_label.place(x=240,y=130)
        self.kasuga_check.place(x=240,y=155)
        self.heian_check.place(x=310,y=155)
        self.suehiro_check.place(x=380,y=155)
        self.fuyo_check.place(x=240,y=180)
        self.ran_check.place(x=310,y=180)
        self.ganju_check.place(x=380,y=180)
        
        self.con = ctk.CTkButton(self,text="確認",font=("HG正楷書体-PRO",20,"bold"),width=80,height=30,command=self.check_info)
        self.con.place(x=350,y=615)
        self.clear_btn = ctk.CTkButton(self,text="入力クリア",font=("HG正楷書体-PRO",20,"bold"),height=30,command=self.all_clear)
        self.clear_btn.place(x=0,y=615)
      
    #お部屋グレード 
    def rg_num(self):
        if self.option_room_grade_status1.get():
            self.roomgrade_num1.configure(state='normal',border_color="#62D176",button_color="#62D176",button_hover_color="green")
        else:
            self.roomgrade_num1.set("0")
            self.roomgrade_num1.configure(state="disable",border_color="gray",button_color="gray",button_hover_color="gray")     
    def rg_num2(self):
        if self.option_room_grade_status2.get():
            self.roomgrade_num2.configure(state="normal",border_color="#62D176",button_color="#62D176",button_hover_color="green")
        else:
            self.roomgrade_num2.set("0")
            self.roomgrade_num2.configure(state="disable",border_color="gray",button_color="gray",button_hover_color="gray")
    #酒飲み放題
    def bottomless_cup_plan(self):
        if self.option_bottomless_cup_state.get():
            self.bottomlesscup_num.configure(state="normal",border_color="#62D176",button_color="#62D176",button_hover_color="green")
            self.bottomlesscup_hour.configure(state="readonly",border_color="#62D176",button_color="#62D176",button_hover_color="green")
        else:
            self.bottomlesscup_num.set("0")
            self.bottomlesscup_num.configure(state="disable",border_color="gray",button_color="gray",button_hover_color="gray")
            self.bottomlesscup_hour.set("0")
            self.bottomlesscup_hour.configure(state="disable",border_color="gray",button_color="gray",button_hover_color="gray")
    #追加料理の
    def additional_dishes_add1(self):
        if self.additional_dishes1_state.get():
            self.additional_dishes_num1.configure(state="normal",border_color="#62D176",button_color="#62D176",button_hover_color="green")
        else:
            self.additional_dishes_num1.set("0")
            self.additional_dishes_num1.configure(state="disable",border_color="gray",button_color="gray",button_hover_color="gray")
    def additional_dishes_add2(self):
        if self.additional_dishes2_state.get():
            self.additional_dishes_num2.configure(state="normal",border_color="#62D176",button_color="#62D176",button_hover_color="green")
        else:
            self.additional_dishes_num2.set("0")
            self.additional_dishes_num2.configure(state="disable",border_color="gray",button_color="gray",button_hover_color="gray")
    def additional_dishes_add3(self):
        if self.additional_dishes3_state.get():
            self.additional_dishes_num3.configure(state="normal",border_color="#62D176",button_color="#62D176",button_hover_color="green")
        else:
            self.additional_dishes_num3.set("0")
            self.additional_dishes_num3.configure(state="disable",border_color="gray",button_color="gray",button_hover_color="gray")
    # 二次会
    def Niji_input(self):
        if self.Niji_state.get():
            self.Niji_plan.configure(state="readonly",border_color="#62D176",button_color="#62D176",button_hover_color="green")
            self.Niji_num.configure(state="normal",border_color="#62D176",button_color="#62D176",button_hover_color="green")
        else:
            self.Niji_plan.set("未選択")
            self.Niji_plan.configure(state="disable",border_color="gray",button_color="gray",button_hover_color="gray")
            self.Niji_num.set("0")
            self.Niji_num.configure(state="disable",border_color="gray",button_color="gray",button_hover_color="gray")
    # 全てクリア
    def all_clear(self):
        self.np_combo.set("2")
        self.stay_num_conbo.set("0")
        self.crs_combo.set("未選択")
        self.option_room_grade_1.deselect()
        self.roomgrade_num1.set("0")
        self.roomgrade_num1.configure(state="disable",border_color="gray",button_color="gray",button_hover_color="gray")
        self.option_room_grade_2.deselect()
        self.roomgrade_num2.set("0")
        self.roomgrade_num2.configure(state="disable",border_color="gray",button_color="gray",button_hover_color="gray")
        self.option_bottomless_cup.deselect()
        self.bottomlesscup_num.set("0")
        self.bottomlesscup_num.configure(state="disable",border_color="gray",button_color="gray",button_hover_color="gray")
        self.bottomlesscup_hour.set("0")
        self.bottomlesscup_hour.configure(state="disable",border_color="gray",button_color="gray",button_hover_color="gray")
        
        self.additional_dishes1.deselect()
        self.additional_dishes2.deselect()
        self.additional_dishes3.deselect()
        self.additional_dishes_num1.set("0")
        self.additional_dishes_num1.configure(state="disable",border_color="gray",button_color="gray",button_hover_color="gray")
        self.additional_dishes_num2.set("0")
        self.additional_dishes_num2.configure(state="disable",border_color="gray",button_color="gray",button_hover_color="gray")
        self.additional_dishes_num3.set("0")
        self.additional_dishes_num3.configure(state="disable",border_color="gray",button_color="gray",button_hover_color="gray")
        
        self.Nijikai.deselect()
        self.Niji_plan.set("未選択")
        self.Niji_plan.configure(state="disable",border_color="gray",button_color="gray",button_hover_color="gray")
        self.Niji_num.set("0")
        self.Niji_num.configure(state="disable",border_color="gray",button_color="gray",button_hover_color="gray")
        
        self.kasuga_check.deselect()
        self.heian_check.deselect()
        self.suehiro_check.deselect()
        self.fuyo_check.deselect()
        self.ran_check.deselect()
        self.ganju_check.deselect()
    # 選択画面に🔙
    def return_toppage(self):
        from SelectPurpose import SelectPurpose
        self.destroy()
        SelectPurpose(self.master,self.customer_name,self.customer_email)  
    # 入力の制限
    # nowmumはエラー回避のためだけのやつなのでそのままでおｋ（コマンド実行時に引数を渡してる）
    def np_sp(self,now_num):
        a = self.np_combo.get()
        st = self.stay_num_conbo.get()
        r1 = self.roomgrade_num1.get()
        r2 = self.roomgrade_num2.get()
        nomi = self.bottomlesscup_num.get()
        ni = self.Niji_num.get()

        if a.isdecimal() == False:
            print("error_all")
            a = "0"
            self.np_combo.set("2")
            self.stay_num_conbo.set("0")
            self.roomgrade_num1.set("0")
            self.roomgrade_num2.set("0")
            self.bottomlesscup_num.set("0")
            self.Niji_num.set("0")
            
        if st.isdecimal() == False:
            print("error_stay")
            st = "0"
            self.stay_num_conbo.set("0")
        elif int(st) > int(a):
            self.stay_num_conbo.set(int(a))
            st = self.stay_num_conbo.get()
            
        if r1.isdecimal() == False:
            print("error_op1")
            self.roomgrade_num1.set(int(st))
        elif int(r1) > int(st):
            self.roomgrade_num1.set(int(st))
            
        if r2.isdecimal() == False:
            print("error_op2")
            self.roomgrade_num2.set("0")
        elif int(r2) > int(st)-int(r1):
            self.roomgrade_num2.set("0")
            
        if nomi.isdecimal() == False:
            print("error_nijika")
            self.bottomlesscup_num.set("0")
        elif int(ni) > int(a):
            self.bottomlesscup_num.set(a)
            
        if ni.isdecimal() == False:
            print("error_nijika")
            self.Niji_num.set("0")
        elif int(ni) > int(a):
            self.Niji_num.set(a)
        
        self.stay_num_conbo.configure(values = [str(i) for i in range(0,int(a)+1,10)] )
        self.roomgrade_num1.configure(values = [str(i) for i in range(0,int(st)+1-int(r2),10)] )
        self.roomgrade_num2.configure(values = [str(i) for i in range(0,int(st)+1-int(r1),10)] )
        self.bottomlesscup_num.configure(values = [str(i) for i in range(0,int(a)+1,10)] )
        self.Niji_num.configure(values = [str(i) for i in range(0,int(a)+1,10)] )
        
    def check_info(self):
        # 0だと確認画面に
        check_clear_flag = 0
        # エラーのリスト
        bad_list = []
        
        # 全体の人数
        self.all_num = self.np_combo.get()
        if self.all_num.isdecimal():
            if int(self.all_num) >= 2:
                pass
            else:
                check_clear_flag +=1
                bad_list.append("人数")
        else:
            # check_clear_flag +=1
            # bad_list.append("人数")
            # ここだめだとダメなので帰します一旦
            msb.showerror("エラー","不正な入力：\n人数")
            return
            
        # コース名
        self.cource_name = self.crs_combo.get()
        if self.cource_name == "未選択":
            check_clear_flag +=1
            bad_list.append("コース選択")
        else:
            pass
        
        # 宿泊人数
        self.staynum = self.stay_num_conbo.get()
        if self.staynum.isdecimal():
            if int(self.staynum) > int(self.all_num):
                check_clear_flag +=1
                bad_list.append("宿泊人数")
            else:
                pass
        else:
            check_clear_flag +=1
            bad_list.append("宿泊人数")
        
        # option　部屋グレード　１
        self.roomgrade1 = self.roomgrade_num1.get()   
        # option　部屋グレード　２
        self.roomgrade2 = self.roomgrade_num2.get()
        if self.roomgrade1.isdecimal() and self.roomgrade2.isdecimal():
            if int(self.roomgrade1) + int(self.roomgrade2) > int(self.staynum):
                check_clear_flag += 1
                bad_list.append("部屋グレードの人数")
            else:
                pass 
        else:
            check_clear_flag += 1
            bad_list.append("部屋グレード")
            
        # 飲み放題人数
        self.nominum = self.bottomlesscup_num.get()
        if self.nominum.isdecimal():
            if int(self.nominum) > int(self.all_num):
                check_clear_flag += 1
                bad_list.append("飲み放題の人数")
            else:
                pass
        else:
            check_clear_flag += 1
            bad_list.append("飲み放題の人数")
            self.nominum = "0"
        
        # 飲み放題時間
        self.nomitime = self.bottomlesscup_hour.get()
        if self.nomitime.isdecimal():
            if int(self.nominum) == 0:
                self.nomitime = "0"
            else:
                pass
        else:
            check_clear_flag += 1
            bad_list.append("飲み放題時間")
        
        # 追加料理１　個数
        self.add_menu1 = self.additional_dishes_num1.get()
        if self.add_menu1.isdecimal():
            pass
        else:
            check_clear_flag+=1
            bad_list.append("追加料理1")        
        # 追加料理2
        self.add_menu2 = self.additional_dishes_num2.get()
        if self.add_menu2.isdecimal():
            pass
        else:
            check_clear_flag+=1
            bad_list.append("追加料理2")        
        # 追加料理3
        self.add_menu3 = self.additional_dishes_num3.get()
        if self.add_menu3.isdecimal():
            pass
        else:
            check_clear_flag+=1
            bad_list.append("追加料理3")        
        
        # 二次会人数
        self.nijikai_num = self.Niji_num.get()
        if self.nijikai_num.isdecimal():
                if int(self.nijikai_num) > int(self.all_num):
                    check_clear_flag += 1
                    bad_list.append("二次会人数")
                else:
                    pass
        else:
            check_clear_flag += 1
            bad_list.append("二次会人数")
            self.nijikai_num ="0"
        # 二次会プラン
        self.nijikai_plan = self.Niji_plan.get()
        if self.nijikai_plan == "未選択":
            if int( self.nijikai_num) == 0:
                pass
            else:
                self.nijikai_num = "0"
        else:
            pass
            

        # クリア判定！！
        if check_clear_flag == 0:
            print("clear")
            self.move_confirm()
        else:
            errortext = "以下の項目でエラーが起きています\n-------------------------------------\n"
            for i in bad_list:
                errortext += f"{i}\n"
            msb.showerror("エラー",errortext)
        
    def move_confirm(self):
        # 全体の人数
        all_num = int(self.all_num)
        # コース　名
        cource_name = self.cource_name
        # コース金
        cource_money = 0
        if cource_name == "豪華コース":
            cource_money = 21600
        elif cource_name == "雅コース":
            cource_money= 18600
        elif cource_name == "錦コース":
            cource_money= 15600
        elif cource_name == "椿コース":
            cource_money= 12600
        else:
            print("error")
        # 宿泊人数
        staynum = int(self.staynum)
        # option　部屋グレード　１
        roomgrade1_num = int(self.roomgrade1)
        roomgrade1_money = 2000
        # option　部屋グレード　２
        roomgrade2_num = int(self.roomgrade2)
        roomgrade2_money = 3000
        # 飲み放題人数
        nominum = int(self.nominum)
        # 飲み放題時間
        nomitime = int(self.nomitime)
        # 追加料理１
        add_menu1 = int(self.add_menu1)
        add_menu1_money = 4000
        # 追加料理2
        add_menu2 = int(self.add_menu2)
        add_menu2_money = 1100
        # 追加料理3
        add_menu3 = int(self.add_menu3) 
        add_menu3_money = 750
        
        # 二次会プラン名
        nijikai_plan = self.nijikai_plan
        # 二次会一人当たりの値段
        niji_money = 0
        if nijikai_plan == "スナック3,000円":
          niji_money = 3000
        elif nijikai_plan == "スナック2,500円" or "カラオケ":
          niji_money = 2500
        else:
            pass
        # 二次会人数
        nijikai_num = int(self.nijikai_num)
         
        name = self.customer_name
        email = self.customer_email       
        from auth import pagemove_entrybanquet_quotationbanquet
        self.destroy()
        pagemove_entrybanquet_quotationbanquet(self.master, name, email,\
        all_num,cource_name,cource_money,staynum,\
                roomgrade1_money,roomgrade2_money,roomgrade1_num,roomgrade2_num,\
        nominum,nomitime,add_menu1_money,add_menu2_money,add_menu3_money,add_menu1,add_menu2,add_menu3,nijikai_plan,nijikai_num,niji_money)

if __name__ == '__main__':
    root = ctk.CTk()
    app = Enkai_Input(root)
    app.mainloop()