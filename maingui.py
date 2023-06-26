"""
    2023-05-02 개발 시작
    코드 참여자 이지석, 양유빈
    개발 log{
        2023.05.04 이지석
        - 시간 가져오기 및 표시
        2023.05.08 이지석
        - ract-1.png를 button 추가
        2023.05.15 이지석
        - gui 멈춤 문제 해결
        2023.05.29 이지석
        - grap, 하단바 구현
        2023.06.25 이지석
        - code 모듈화 진행
    }
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
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
from scipy.interpolate import make_interp_spline
import numpy as np
import header
import main
"""
def on_enter(event):
    button.config(image=root.btn_active)
"""
# 버튼클릭시 함수
if __name__=="__main__":
    root = Tk()#Tk 생성
    # root.overrideredirect(True)
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
    
    root.footer_ra_img = ImageTk.PhotoImage(footer_ra_img)
    root.todo_img = ImageTk.PhotoImage(todo_img)
    root.hfile_img = ImageTk.PhotoImage(hfile_img)
    root.searcheck_img = ImageTk.PhotoImage(searcheck_img)
    root.aram_img = ImageTk.PhotoImage(aram_img)
    root.setting_img = ImageTk.PhotoImage(setting_img)
    # 이미지를 모듈로 만들어 준다
    
    footer_img_lable = Label(root, image=root.footer_ra_img, bg="#1b1b1b", borderwidth=0, highlightthickness=0)
    # 하단쪽 그림을 출력하는 label 이다
    
    health_check_button = Button(root, text="양유빈 님의 건강 상태를 확인하세요>",font=('NaumGothic',25),bg="#1b1b1b",fg="white",borderwidth=0, highlightthickness=0)
    
    todo_button = Button(root, image=root.todo_img, bg="#535355", width=100, height=140, borderwidth=0, highlightthickness=0)
    hfile_button = Button(root, image=root.hfile_img, bg="#535355", width=100, height=140, borderwidth=0, highlightthickness=0)
    searcheck_button = Button(root, image=root.searcheck_img, bg="#535355", width=100, height=140, borderwidth=0, highlightthickness=0)
    aram_button = Button(root, image=root.aram_img, bg="#535355", width=100, height=140, borderwidth=0, highlightthickness=0)
    setting_button = Button(root, image=root.setting_img, bg="#535355", width=100, height=140, borderwidth=0, highlightthickness=0)
    
    canvas.create_window(540, 1750, window=footer_img_lable)
    canvas.create_window(270, 1750, window=todo_button)
    canvas.create_window(405, 1750, window=hfile_button)
    canvas.create_window(540, 1750, window=searcheck_button)
    canvas.create_window(675, 1750, window=aram_button)
    canvas.create_window(810, 1750, window=setting_button)
    canvas.create_window(360, 590, window=health_check_button)
    """
    plot()
    """
    # 그래프 출력 함수 이동
    """
    grap_result_label.lift()
    grap_vare_label.lift()
    # 그래프를 버튼 위로 이동 한다
    """
    
    root.geometry("1080x1920")
    # 화면 크기를 지정한다
    
    header.Header_menu(canvas, root, Tk)
    main.main_menu(canvas, root, Tk)
    # header.by 모듈을 불러 온다
    
    # root.wm_attributes('-fullscreen', 'True') # gui 완성시 주석 삭제
    # 윈도우 상당 바를 없애고 풀스크린 설정 한다
    root.mainloop()