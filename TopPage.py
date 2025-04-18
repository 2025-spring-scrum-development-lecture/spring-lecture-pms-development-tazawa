import customtkinter as ctk
import re

class TopPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=450, height=350)
        self.master = master
        self.place(x=400, y=100)

        self.master.state('zoomed')
        master.title('お客様情報')
        
        ctk.set_appearance_mode("Light")
        ctk.set_default_color_theme("green")
        
        self.create_widgets()
        
        
        
    def create_widgets(self):
        self.label = ctk.CTkLabel(self, text='お客様情報の入力', font=('Times', 25))
        self.label.place(x=50, y=30)
        
        self.entryname = ctk.CTkEntry(master=self, placeholder_text="氏名", width=250, font=('Times',20))
        self.entryname.place(x=100, y=100)
        
        self.entrymail = ctk.CTkEntry(master=self, placeholder_text="メールアドレス", width=250,font=('Times',20))
        self.entrymail.place(x=100, y=200)
        
        self.button2 = ctk.CTkButton(master=self, text="利用用途へ", command=self.button_event,font=('Times',15))
        self.button2.place(x=250, y= 290)
        
        self.name_label = ctk.CTkLabel(self, text='')
        self.name_label.place(x = 140, y =150 )
        
        self.mail_label = ctk.CTkLabel(self, text='')
        self.mail_label.place(x = 140, y = 250)
        
                
    
        
    def button_event(self):
        # 氏名：name/メールアドレス：mail
        email = self.entrymail.get().strip()
        name = self.entryname.get()
        
        if not name:
            self.name_label.configure(text="※名前を入力してください", text_color="red",font=('Times',13))
            return
        elif re.search(r'[0-9\W_]', name):
            self.name_label.configure(text="※数字または記号が含まれています", text_color="red",font=('Times',13))
            
        else:
            self.name_label.configure(text="")
            
        
        if not email:
            self.mail_label.configure(text="※メールを入力してください", text_color="red",font=('Times',13))
            return
        elif "@" not in email or "." not in email or re.search(r'[^\x00-\x7F\W_]', email):
            self.mail_label.configure(text="※正しいメールアドレスを入力してください", text_color="red",font=('Times',13))
            return             
        elif not re.search(r'[a-zA-Z]', email) or not re.search(r'[0-9]', email):
            self.mail_label.configure(text="※メールアドレスには英字と数字を含めてください", text_color="red", font=('Times',13))
            return
        else:
            self.mail_label.configure(text="")
        
        from auth import pagemove_top_select
        self.destroy()
        pagemove_top_select(self.master,name,email)
        
        
if __name__ == '__main__':
    root = ctk.CTk()
    app = TopPage(root)
    app.mainloop()
    
    
 