"""
    개발 log{
        2023.06.25 이지석
        - header.py 모듈 제작
    }
    사용 label{
        time_label //시분초를 출력
        Yemd_label //년월일을 출력   
    }
"""

from tkinter import *
from datetime import datetime
import threading

class Header_menu:
    def __init__(self, canvas, root, Tk):
        self.canvas = canvas
        self.root = root
        self.Tk = Tk
        self.write_header()
        # write_header 함수를 실행하여 label을 출력한다
        
    def write_header(self):
        self.time_label = Label(self.root, font=('NanumGothic', 30), fg="white", bg="#1b1b1b") 
        # 시분초 출력 label 설정 정의
        self.Yemd_label = Label(self.root, font=('NaumGothic',20), fg="white", bg="#1b1b1b")
        # 년월일 출력 label 설정 정의
        
        self.Thread_time()
        self.startThread_Ymd()
        # 스레드를 생성한다
        
        self.canvas.create_window(130, 100, window=self.time_label)
        self.canvas.create_window(170, 50, window=self.Yemd_label)
        # label window 에 생성 한다
        
    def update_time(self):
        current_time = datetime.now().strftime("%H:%M")
        self.time_label.config(text=current_time)
        self.Yemd_label.after(1000, self.update_time)
        # 시분초를 가져와 업데이트 하는 함수 이다
    
    def update_Ymd(self):
        current_Ymd = datetime.now().strftime("%y년%m월%d일")
        self.Yemd_label.config(text=current_Ymd)
        self.Yemd_label.after(1000, self.update_Ymd)
        # 년월일을 가져와 업데이트 하는 함수
        
    def Thread_time(self):
        # 시분초 를 출력하는 쓰레드를 생성한다
        thread = threading.Thread(target=self.update_time)
        # thead 사용할 함수를 지정한다
        thread.daemon = True
        # thread 사용을 허용 해준다
        thread.start()
        # thread를 시작한다

    def startThread_Ymd(self):
        # 년월일 쓰레드 생성
        thread = threading.Thread(target=self.update_Ymd)
        # thead 사용할 함수를 지정한다
        thread.daemon = True
        # thread 사용을 허용 해준다
        thread.start()
        #쓰레드를 시작한다