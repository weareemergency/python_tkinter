from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import time
import threading
from datetime import datetime


def on_enter(event):
    button.config(image=root.btn_active)
# 버튼클릭시 함수
    
def update_time():
    current_time = datetime.now().strftime("%H:%M")
    time_label.config(text=current_time)
    Yemd_label.after(1000, update_time)

def update_Ymd():
    current_Ymd = datetime.now().strftime("%y년%m월%d일")
    Yemd_label.config(text=current_Ymd)
    Yemd_label.after(1000, update_Ymd)
# 시간 업데이트 함수

def startThread():
    thread = threading.Thread(target=update_time)
    thread.daemon = True
    thread.start()
# 타임 쓰레드 생성

def startThreadYmd():
    thread = threading.Thread(target=update_Ymd)
    thread.daemon = True
    thread.start()
# 년월일 쓰레드 생성

if __name__=="__main__":
    root = Tk()#Tk 생성
    canvas = Canvas(root, bg="#1b1b1b") 
    # gui화면 설정 배경 bg="색갈입력" 현재 #1b1b1b 설정됨
    canvas.pack(fill=BOTH, expand=TRUE)

    btn_inactive = Image.open("img/mainwindow.png")
    btn_inactive = btn_inactive.resize((900, 260))

    # 버튼 이미지 주소를 열어서 사진을 저장한다

    root.btn_inactive = ImageTk.PhotoImage(btn_inactive)
    wear_label = Label(root, font=('NanumGothic', 20), text="")
    time_label = Label(root, font=('NanumGothic', 30), fg="white", bg="#1b1b1b")
    Yemd_label = Label(root, font=('NaumGothic',20), fg="white", bg="#1b1b1b")
    button = Button(root, image=root.btn_inactive, bg="#1b1b1b", width=900, height=260, borderwidth=0, highlightthickness=0)

    canvas.create_window(130, 100, window=time_label)
    canvas.create_window(540, 750, window=button)
    canvas.create_window(170, 50, window=Yemd_label)


    root.geometry("1080x1920")
    
    startThreadYmd()
    startThread()
    root.mainloop()