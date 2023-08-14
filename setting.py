"""
    개발 log{
        2023.08.15 이지석
        - setting.py 모듈 제작
        .......
    }
    사용 label{
        
    }
    사용 listbox{
        
    }
"""
from tkinter import *
from tkinter import ttk
from pprint import pprint
from PIL import ImageTk, Image
from pathlib import Path
from tkinter.scrolledtext import ScrolledText
import header
import footer

class rank_list:
    def __init__(self, canvas, root):
        self.canvas = canvas
        self.root = root
        self.rank()
         
    def rank(self):
        self.setting_icon = Image.open("img/setting.png")
        self.setting_icon = self.setting_icon.resize((50,50))
        self.root.setting_icon = ImageTk.PhotoImage(self.setting_icon)
        
        self.rect1 = Image.open("img/Rectangle_setting.png")
        self.root.rect1 = ImageTk.PhotoImage(self.rect1)
        

        self.setting_label = Label(self.root, font=('NanumGothic', 25, 'bold'), text='양유빈님의 설정       >',fg="white", bg="#1b1b1b")
        self.setting_icon = Label(self.root,image=self.root.setting_icon, bg="#1b1b1b", borderwidth=0, highlightthickness=0)
        self.setting_rect = Label(self.root,image=self.root.rect1, bg="#1b1b1b", borderwidth=0, highlightthickness=0)
        
        self.canvas.create_window(700, 815, window=self.setting_rect)
        self.canvas.create_window(325, 620, window=self.setting_icon)
        self.canvas.create_window(218, 620, window=self.setting_label)
if __name__=="__main__":
    root = Tk()#Tk 생성
    # root.overrideredirect(True)
    canvas = Canvas(root, bg="#1b1b1b") 
    # gui화면 설정 배경 bg="색갈입력" 현재 #1b1b1b 설정됨
    canvas.pack(fill=BOTH, expand=TRUE)
    header.Header_menu(canvas, root)
    # footer.footer_menu(canvas, root)
    rank_list(canvas, root)
    root.geometry("1080x1920")
    # 화면 크기를 지정한다
    root.mainloop()