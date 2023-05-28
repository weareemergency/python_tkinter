"""
    2023-05-02 개발 시작
    코드 참여자 이지석, 양유빈
    github: https://github.com/weareemergency/python_tkinter.git
    코드 다운방법
    git clone https://github.com/weareemergency/python_tkinter.git
    프로젝트 싸이트:https://juniper-jumbo-de1.notion.site/python-52d9227c31c340249c001f0698a77eac
    설명:
    python tkinter 을 사용해서 의료용스마트 미러 
    main화면 gui를 만드는 코드 이다.
"""

from tkinter import *
from PIL import ImageTk, Image
import threading
from datetime import datetime
from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
from scipy.interpolate import make_interp_spline
import numpy as np

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
    html = requests.get('https://search.naver.com/search.naver?query=부산강서구가락동날씨')
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
    weather_tem_label.after(600000, update_weather)
    # 10분 마다 업데이트 한다

# 글래프를 그리는 함수이다
def plot():
    fig = Figure(figsize = (5, 1),dpi = 100)
    
    x=np.array([1,2,3,4,5,6,7])
    y=np.array([100,100,100,100,10,10,50])
    x2=np.array([1,2,3,4,5,6,7])
    y2=np.array([0,0,0,100,50,50,50])
    
    model=make_interp_spline(x, y)
    model2=make_interp_spline(x2, y2)
    
    xs=np.linspace(1,7,500)
    ys=model(xs)
    
    xs2=np.linspace(1,7,500)
    ys2=model2(xs2)
    
    plot1 = fig.add_subplot(111)
    plot1.plot(xs, ys,zorder=50, color = 'green')
    plot1.plot(xs2, ys2,zorder=50, color = 'blue')
    plot1.axis('off')
    # 그래프에서 축을 삭제한다
    canvas = FigureCanvasTkAgg(fig, master=root)  
    canvas.draw()
    #canvas.create_window(100, 100, window=garap_show)
    canvas.get_tk_widget().place(x=110,y=1040)
    
    #garap_show.get_tk_widget().lift()

    
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

    footer_ra_img = Image.open("img/footer_ract.png")
    footer_ra_img = footer_ra_img.resize((900, 170))
    # footer_ract.png 이미지를 가와서 열고 크기를 설정한다
    
    todo_img = Image.open("img/todo.png")
    todo_img = todo_img.resize((100, 140))
    # todo.png 이미지를 가져와 열고 사이즈 설정
    
    hfile_img = Image.open("img/hfile.png")
    hfile_img = hfile_img.resize((100, 140))
    # hfile.png 이미지를 가져와 열고 사이즈 설정
    
    searcheck_img = Image.open("img/searcheck.png")
    searcheck_img = searcheck_img.resize((100, 140))
    # searcheck.png 이미지를 가져와 열고 사이즈 설정
    
    aram_img = Image.open("img/aram.png")
    aram_img = aram_img.resize((100, 140))
    # aram.png 이미지를 가져와 열고 사이즈 설정
    
    setting_img = Image.open("img/setting.png")
    setting_img = setting_img.resize((100, 140))
    # setting.png 이미지를 가져와 열고 사이즈 설정
    
    ract_img2 = Image.open("img/Rectangle.png")
    ract_img2 = ract_img2.resize((300, 260))
    # Rectangle.png 이미지 가져와서 열기
    
    ract_img = Image.open("img/ract-1.png")
    ract_img = ract_img.resize((560,260))
    # ract-1.png 이미지 가져와서 열기
    
    crow_img = Image.open("img/crow.png")
    crow_img = crow_img.resize((70,70))
    # crow.png 이미지를 가져와 열기 사이지 지정
    
    btn_inactive = Image.open("img/main2.png")
    btn_inactive = btn_inactive.resize((900, 260))
    # minwindow.png 이미지를 들고 온다
    # resize 를 사용하여 사진 크기를 조정한다
    weather_icon = Image.open("img/sun-dynamic.png")
    weather_icon = weather_icon.resize((100,100))
    # 버튼 이미지 주소를 열어서 사진을 저장한다
    list_Value = [10, 20, 30, 20, 40, 10]
    
    
    root.btn_inactive = ImageTk.PhotoImage(btn_inactive)
    root.weather_icon = ImageTk.PhotoImage(weather_icon)
    root.ract_img = ImageTk.PhotoImage(ract_img)
    root.ract_img2 = ImageTk.PhotoImage(ract_img2)
    root.crow_img  = ImageTk.PhotoImage(crow_img)
    root.footer_ra_img = ImageTk.PhotoImage(footer_ra_img)
    root.todo_img = ImageTk.PhotoImage(todo_img)
    root.hfile_img = ImageTk.PhotoImage(hfile_img)
    root.searcheck_img = ImageTk.PhotoImage(searcheck_img)
    root.aram_img = ImageTk.PhotoImage(aram_img)
    root.setting_img = ImageTk.PhotoImage(setting_img)
    # 이미지를 모듈로 만들어 준다
    
    
    grap_result_label = Label(root, font=('NanumGothic', 27,'bold') ,text='자세 분석 결과:',fg="black", bg="white")
    # "자세 분석 결과:" 문자를 출력하는 label 이다
    grap_vare_label = Label(root, font=('NanumGothic', 20), text='전주 대비 향상 되었습니다!',fg="black", bg="white")
    # "전주 대비 향상 되었습니다!" 등 결과를 문자로 출력하는 label 이다
    waether_posion_label = Label(root, font=('NanumGothic', 20), text='부산광역시 강서구 가락동',fg="white", bg="#1b1b1b")
    # "부산광역시 강서구 가락동"등 위치를 알려주는 문자이다
    time_label = Label(root, font=('NanumGothic', 30), fg="white", bg="#1b1b1b")
    # 시간에서 시:분 을 출력하는 label 이다
    Yemd_label = Label(root, font=('NaumGothic',20), fg="white", bg="#1b1b1b")
    # 년월일을 을 출력하는 label 이다
    weather_icon_label = Label(root, image=root.weather_icon, bg="#1b1b1b", borderwidth=0, highlightthickness=0)
    # 날씨 그림을 가져와 출력하는 label 이다
    weather_tem_label = Label(root, font=('NanumGothic', 30), fg="white", bg="#1b1b1b")
    # 날씨 온도를 출력하는 label 이다
    button = Button(root, image=root.btn_inactive, bg="#1b1b1b", width=900, height=260, borderwidth=0, highlightthickness=0)
    # 영상들을 추천하는 그림을 출력하는 button 이다
    ract_img_button = Button(root, image=root.ract_img, bg="#1b1b1b", width=560, height=260, borderwidth=0, highlightthickness=0)
    # 자세분석 결과 박스를 만드는 button 이다
    ract2_img_button = Button(root, image=root.ract_img2, bg="#1b1b1b", width=300, height=260, borderwidth=0, highlightthickness=0)
    # 투두 리스트 박스를 만드는 button 이다
    crow_img_label = Label(root, image = root.crow_img, bg="white", borderwidth=0, highlightthickness=0)
    # 랭크 화면의 이미지를 출력하는 label 이다
    list_label = Label(root, font=('NanumGothic', 20, 'bold') ,text='현재 양유빈님이\n투두 1등 입니다',fg="black", bg="white")
    # 1위 랭크를 출력하는 label 이다
    list_rank_lable = Label(root, font=('NanumGothic', 17), text='2등 이지석님',fg="black", bg="white")
    # 2등 랭크를 출력하는 label 이다
    list_rank2_lable = Label(root, font=('NanumGothic', 17), text='3등 양성웅님',fg="black", bg="white")
    # 3등 랭크를 출력하는 label 이다
    footer_img_lable = Label(root, image=root.footer_ra_img, bg="#1b1b1b", borderwidth=0, highlightthickness=0)
    # 하단쪽 그림을 출력하는 label 이다
    health_check_button = Button(root, text="양유빈 님의 건상 상태를 확인하세요>",font=('NaumGothic',25),bg="#1b1b1b",fg="white",borderwidth=0, highlightthickness=0)
    
    todo_button = Button(root, image=root.todo_img, bg="#535355", width=100, height=140, borderwidth=0, highlightthickness=0)
    hfile_button = Button(root, image=root.hfile_img, bg="#535355", width=100, height=140, borderwidth=0, highlightthickness=0)
    searcheck_button = Button(root, image=root.searcheck_img, bg="#535355", width=100, height=140, borderwidth=0, highlightthickness=0)
    aram_button = Button(root, image=root.aram_img, bg="#535355", width=100, height=140, borderwidth=0, highlightthickness=0)
    setting_button = Button(root, image=root.setting_img, bg="#535355", width=100, height=140, borderwidth=0, highlightthickness=0)
    
    plot()# 그래프 출력 함수
    
    canvas.create_window(130, 100, window=time_label)
    canvas.create_window(170, 50, window=Yemd_label)
    canvas.create_window(250, 220, window=weather_tem_label) 
    canvas.create_window(130, 200, window=weather_icon_label)
    canvas.create_window(540, 750, window=button)
    canvas.create_window(330, 170, window=waether_posion_label)
    canvas.create_window(373, 1040, window=ract_img_button)
    canvas.create_window(250, 960, window=grap_result_label)
    canvas.create_window(285, 1000, window=grap_vare_label)
    canvas.create_window(838, 1040, window=ract2_img_button)
    canvas.create_window(740, 970, window=crow_img_label)
    canvas.create_window(880,975, window=list_label)
    canvas.create_window(840, 1070, window=list_rank_lable)
    canvas.create_window(840, 1100, window=list_rank2_lable)
    canvas.create_window(540, 1750, window=footer_img_lable)
    canvas.create_window(270, 1750, window=todo_button)
    canvas.create_window(405, 1750, window=hfile_button)
    canvas.create_window(540, 1750, window=searcheck_button)
    canvas.create_window(675, 1750, window=aram_button)
    canvas.create_window(810, 1750, window=setting_button)
    canvas.create_window(360, 590, window=health_check_button)
    grap_result_label.lift()
    grap_vare_label.lift()
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
