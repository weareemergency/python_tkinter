"""
    2023-05-02 개발 시작
    코드 참여자 이지석, 양유빈
    github: https://github.com/weareemergency/python_tkinter.git
    코드 다운방법
    git clone https://github.com/weareemergency/python_tkinter.git
    프로젝트 싸이트:https://juniper-jumbo-de1.notion.site/python-52d9227c31c340249c001f0698a77eac
    설명:
    python tkinter 을 사용해서 의료용스마트 미러 
    mian화면 gui를 만드는 코드 이다.
"""

from tkinter import *
from PIL import ImageTk, Image
import threading
from datetime import datetime
from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests


def on_enter(event):
    button.config(image=root.btn_active)
# 버튼클릭시 함수
    
def update_time():
    current_time = datetime.now().strftime("%H:%M")
    time_label.config(text=current_time)
    Yemd_label.after(1000, update_time)
# 시분초를 가져와 업데이트 하는 함수 이다

def update_Ymd():
    current_Ymd = datetime.now().strftime("%y년%m월%d일")
    Yemd_label.config(text=current_Ymd)
    Yemd_label.after(1000, update_Ymd)
# 년월일을 가져와 업데이트 하는 함수

def update_weather():
    html = requests.get('https://search.naver.com/search.naver?query=부산강서구날씨')
    #html 주소를 가져온다
    soup = bs(html.text,'html.parser')
    # 주소로들어간 싸이트를 파싱한다
    # (슬라이싱 작업){
    data1 = soup.find('div',{'class':'temperature_text'})
    data2 = data1.findAll('strong')
    data3=str(data2[0])
    data3= data3[data3.find('</span>')+7:]
    data3=data3[:data3.find('<')]+"°"
    # }
    weather_tem_label.config(text=data3)
    weather_tem_label.after(1000, update_weather)
    
    
# 날씨를 실시간을 얻어 온다
def startThread():
    thread = threading.Thread(target=update_time)
    # thead 사용할 함수를 지정한다
    thread.daemon = True
    # thread 사용을 허용 해준다
    thread.start()
    # thread를 시작한다
# 타임 쓰레드 생성

def startThreadYmd():
    thread = threading.Thread(target=update_Ymd)
    # thead 사용할 함수를 지정한다
    thread.daemon = True
    # thread 사용을 허용 해준다
    thread.start()
    #쓰레드를 시작한다
# 년월일 쓰레드 생성

def startTheadweather():
    thread = threading.Thread(target=update_weather)
    # thead 사용할 함수를 지정한다
    thread.daemon = True
    # thread 사용을 허용 해준다
    thread.start()
    #쓰레드를 시작한다
# 날씨 쓰레드를 생성한다

if __name__=="__main__":
    root = Tk()#Tk 생성
    canvas = Canvas(root, bg="#1b1b1b") 
    # gui화면 설정 배경 bg="색갈입력" 현재 #1b1b1b 설정됨
    canvas.pack(fill=BOTH, expand=TRUE)

    btn_inactive = Image.open("img/mainwindow.png")
    btn_inactive = btn_inactive.resize((900, 260))
    # minwindow.png 이미지를 들고 온다
    # resize 를 사용하여 사진 크기를 조정한다
    weather_icon = Image.open("img/sun-dynamic.png")
    weather_icon = weather_icon.resize((100,100))
    # 버튼 이미지 주소를 열어서 사진을 저장한다

    root.btn_inactive = ImageTk.PhotoImage(btn_inactive)
    root.weather_icon = ImageTk.PhotoImage(weather_icon)
    # 이미지를 모듈로 만들어 준다
    
    time_label = Label(root, font=('NanumGothic', 30), fg="white", bg="#1b1b1b")
    Yemd_label = Label(root, font=('NaumGothic',20), fg="white", bg="#1b1b1b")
    weather_icon_label = Label(root, image=root.weather_icon, bg="#1b1b1b", borderwidth=0, highlightthickness=0)
    weather_tem_label = Label(root, font=('NanumGothic', 30), fg="white", bg="#1b1b1b")
    button = Button(root, image=root.btn_inactive, bg="#1b1b1b", width=900, height=260, borderwidth=0, highlightthickness=0)
    # label, Button 등을 설정한다
    
    canvas.create_window(130, 100, window=time_label)
    canvas.create_window(170, 50, window=Yemd_label)
    canvas.create_window(250, 215, window=weather_tem_label) 
    canvas.create_window(130, 200, window=weather_icon_label)
    canvas.create_window(540, 750, window=button)
    # gui 에 추한다
    root.geometry("1080x1920")
    # 화면 크기를 지정한다
    
    startThreadYmd()
    # 년월일을 가져오는 함수 thread 실행
    startThread()
    # 시분초를 가져오는 함수 thread 실행
    startTheadweather()
    # 날씨를 가져오는 함수 thread 실행
    root.mainloop()