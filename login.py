from tkinter import *
import header
import main
import footer
import start_main

if __name__=="__main__":
    root = Tk()#Tk 생성
    # root.overrideredirect(True)
    canvas = Canvas(root, bg="#1b1b1b") 
    # gui화면 설정 배경 bg="색갈입력" 현재 #1b1b1b 설정됨
    canvas.pack(fill=BOTH, expand=TRUE)
    
    root.geometry("1080x1920")
    # 화면 크기를 지정한다
    root.mainloop()