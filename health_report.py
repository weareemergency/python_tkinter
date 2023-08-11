"""
    개발 log{
        2023.08.9 이지석
        - ranking.py 모듈 제작
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

class health_list:
    def __init__(self, canvas, root):
        self.canvas = canvas
        self.root = root
        self.health()
         
    def health(self):
        self.ract = Image.open("img/rank_rect16.png")
        self.ract = self.ract.resize((915,673))
        self.root.ract = ImageTk.PhotoImage(self.ract)
        
        self.note = Image.open("img/notebook.png")
        self.note = self.note.resize((50,50))
        self.root.note = ImageTk.PhotoImage(self.note)
        
        self.health_label = Label(self.root, font=('NanumGothic', 25, 'bold'), text='건강보고함      >',fg="white", bg="#1b1b1b")
        self.note_icon = Label(self.root,image=self.root.note, bg="#1b1b1b", borderwidth=0, highlightthickness=0)
        self.ract_image = Label(self.root, image=self.root.ract, bg="#1b1b1b", borderwidth=0, highlightthickness=0)
        self.health_con = Label(self.root, font=('NanumGothic', 23, 'bold'), text='양유빈님의 현재 건강 상태',fg="black", bg="white")
        self.con_en = Label(self.root, font=('NanumGothic', 18, 'bold'), text='Physical condition',fg="#7c7c7c", bg="white")
        self.con_list = Listbox(self.root, font=('NanumGothic', 19) ,width=54, height=18, borderwidth=1,bg="white",highlightthickness=0)
        
        self.con_list.insert(END, '-올해 3월 경추추간판')
        self.con_list.insert(END, '-탈출증 초기 및 허리뼈')
        
        self.canvas.create_window(540, 1020, window=self.con_list)
        self.canvas.create_window(600,700, window=self.con_en)
        self.canvas.create_window(300,700, window=self.health_con)
        self.canvas.create_window(260, 620, window=self.note_icon)
        self.canvas.create_window(193, 620, window=self.health_label)
        self.canvas.create_window(540, 990, window=self.ract_image)
        
if __name__=="__main__":
    root = Tk()#Tk 생성
    # root.overrideredirect(True)
    canvas = Canvas(root, bg="#1b1b1b") 
    # gui화면 설정 배경 bg="색갈입력" 현재 #1b1b1b 설정됨
    canvas.pack(fill=BOTH, expand=TRUE)
    header.Header_menu(canvas, root)
    # footer.footer_menu(canvas, root)
    health_list(canvas, root)
    root.geometry("1080x1920")
    # 화면 크기를 지정한다
    root.mainloop()