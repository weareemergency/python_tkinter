from tkinter import *
from pprint import pprint
from PIL import ImageTk, Image
from pathlib import Path
import header
import footer

class todo_list:
    def __init__(self, canvas, root):
        self.canvas = canvas
        self.root = root
        self.todo()
         
    def todo(self):
        self.todo_ract = Image.open("img/Rect16.png")
        self.todo_ract = self.todo_ract.resize((915, 538))
        self.root.todo_ract = ImageTk.PhotoImage(self.todo_ract)
        
        self.check = Image.open("img/check.png")
        self.check = self.check.resize((50, 50))
        self.root.check = ImageTk.PhotoImage(self.check)
        
        self.todo_name_label= Label(self.root, text="양유빈님의 투두리스트>",font=('NaumGothic',25),bg="#1b1b1b",fg="white",borderwidth=0, highlightthickness=0, justify="left")
        self.todo_lable = Label(self.root, font=('Noto Sans', 16, 'bold'), text='To Do List',fg="black", bg="white")
        self.due_lable = Label(self.root, font=('Noto Sans', 16, 'bold'), text='Due Date',fg="black", bg="white")
        self.com_lable = Label(self.root, font=('Noto Sans', 16, 'bold'), text='Complete',fg="black", bg="white")
        self.todo_ract = Label(self.root, image=self.root.todo_ract, bg="#1b1b1b", borderwidth=0, highlightthickness=0)
        self.view_list = Listbox(self.root, font=('NaumGothic',20),width=25, height=13, borderwidth=0,bg="white",highlightthickness=0)
        self.date_list = Listbox(self.root, font=('NaumGothic',20),width=10, height=13, borderwidth=0,bg="white",highlightthickness=0)
        self.check_list = Listbox(self.root, font=('NaumGothic',20),width=10, height=13, borderwidth=0,bg="white")
        
        self.date_list.insert(0, '2023.05.15')
        self.date_list.insert(END, '')
        self.date_list.insert(END, '2023.05.17')
        self.date_list.insert(END, '')
        self.date_list.insert(END, '2023.05.14')
        self.date_list.insert(END, '')
        self.date_list.insert(END, '2023.05.14')
        self.date_list.insert(END, '')
        self.date_list.insert(END, '2023.05.14')
        self.date_list.insert(END, '')
        self.date_list.insert(END, '2023.05.14')
        self.date_list.insert(END, '')
        
        self.view_list.insert(0, '신경외과 처방약 (디스크)복용')
        self.view_list.insert(END, '')
        self.view_list.insert(END, '프라임 병원 신경과 16:00 내원')
        self.view_list.insert(END, '')
        self.view_list.insert(END, '내과 내원')
        self.view_list.insert(END, '')
        self.view_list.insert(END, '이좋은 치과 내원 (임플란트 검진)')
        self.view_list.insert(END, '')
        self.view_list.insert(END, '도수 치료, 전기충격파 치료')
        self.view_list.insert(END, '')
        self.view_list.insert(END, '양유빈 경험 담')
        
        self.view_list.bindtags((self.view_list, self.root, "all"))
        self.date_list.bindtags((self.date_list, self.root, "all"))
        
        self.canvas.create_window(820, 890, window=self.check_list)
        self.canvas.create_window(330, 890, window=self.view_list)
        self.canvas.create_window(640, 890, window=self.date_list)
        self.canvas.create_window(540, 840, window=self.todo_ract)
        self.canvas.create_window(254, 524, window=self.todo_name_label)
        self.canvas.create_window(180, 630, window=self.todo_lable)
        self.canvas.create_window(610, 630, window=self.due_lable)
        self.canvas.create_window(810, 630, window=self.com_lable)
        self.todo_lable.lift()
        self.due_lable.lift()
        self.com_lable.lift()
if __name__=="__main__":
    root = Tk()#Tk 생성
    # root.overrideredirect(True)
    canvas = Canvas(root, bg="#1b1b1b") 
    # gui화면 설정 배경 bg="색갈입력" 현재 #1b1b1b 설정됨
    canvas.pack(fill=BOTH, expand=TRUE)
    header.Header_menu(canvas, root)
    footer.footer_menu(canvas, root)
    todo_list(canvas, root)
    root.geometry("1080x1920")
    # 화면 크기를 지정한다
    root.mainloop()