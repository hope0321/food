from tkinter import *

import tkinter as tk

menu = ["돈까스", "라면", "짜장면", "짬뽕", "햄버거"]




root = Tk()
root.title("오늘 뭐 먹지?")
root.geometry("540x380")

#뭘 먹을지 잘 모르겠을땐 버튼을 누르라고 물어보자
Label(text = "뭘 먹을지 잘 모르겠어? 버튼을 눌러봐!", font=("돋움체",15),fg = "purple").pack()

#사진 추가해보자  
돈까스2 = "C:\\Users\정석기\Desktop"  #사진 추가하는 부분이 계속 에러뜸
img = tk.PhotoImage(file = 돈까스2)

돈까스2_label = tk.Label(root, image=img)
돈까스2_label.pack()

btn1 = Button(root, text = "추천메뉴")
btn1.pack()


root.mainloop()

