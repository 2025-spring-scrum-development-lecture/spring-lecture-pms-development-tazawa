import customtkinter as ctk

class SelectPurpose(ctk.CTkFrame):
    def __init__(self, master,name,email):
        super().__init__(master)
        self.master = master
        self.email = email
        self.name = name


        self.master.state('zoomed')
        master.title('利用用途の確認')
        
        ctk.set_appearance_mode("Light")
        ctk.set_default_color_theme("green")
        

        self.create_widgets()
        
        
        
    def create_widgets(self):
        self.label1 = ctk.CTkLabel(self.master, text=f'{self.name} 様  〖{self.email}〗', font=('Times', 20)) 
        self.label1.place(x=20, y=10)
        
        self.frame = ctk.CTkFrame(self.master, width=1000, height=500)
        self.frame.place(x=130, y=70)
        
        self.label = ctk.CTkLabel(self.frame, text='利用用途確認', font=('Times', 30))
        self.label.place(x=50, y=50)
        
        self.stay_button = ctk.CTkButton(self.frame, text="宿泊", command=self.stay_event,font=('Times',40),width=300,height=300 )
        self.stay_button.place(x=130, y= 130)
        
        self.banquet_button = ctk.CTkButton(self.frame, text="宴会", command=self.banquet_event,font=('Times',40),width=300,height=300 )
        self.banquet_button.place(x=560, y= 130)
        
                
    def stay_event(self):
        from auth import pagemove_select_entrystay
        for widget in self.master.winfo_children():
            widget.destroy()
        pagemove_select_entrystay(self.master,self.name,self.email)
    def banquet_event(self):
        from auth import pagemove_select_entrybanquet
        for widget in self.master.winfo_children():
            widget.destroy()
        pagemove_select_entrybanquet(self.master,self.name,self.email)
                
        
if __name__ == '__main__':
    root = ctk.CTk()
    app = SelectPurpose(root)
    app.mainloop()
    
    
 