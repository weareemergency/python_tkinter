from tkinter import *
import header
import footer
class todo_list:
    def __init__(self, canvas, root):
        self.canvas = canvas
        self.root = root
        self.todo()
         
    def todo(self):
        self.todo_name_label= Label(self.root, text="양유빈님의 투두리스트>",font=('NaumGothic',25),bg="#1b1b1b",fg="white",borderwidth=0, highlightthickness=0, justify="left")
        
        self.canvas.create_window(254, 424, window=self.todo_name_label)

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