
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' type the description of this module file here'

__author__ = 'Justin Zhao'

# if you want to change the default setting format:
# Setting -> Code Style -> File and Code Templates

# 1 导入tkinter包
from tkinter import *

import tkinter.messagebox as messagebox

# 2 Frame派生一个类，作控件的容器
class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        #label
        self.helloLabel = Label(self, text='Hello, world!')
        self.helloLabel.pack()  #pack是一种布局方式，在frame的布局形式
        #input
        self.nameInput = Entry(self)
        self.nameInput.pack()
        #button
        self.quitButton = Button(self, text='ok',command=self.hello)
        self.quitButton.pack()
        # button
        self.quitButton = Button(self, text='no', command=self.quit)
        self.quitButton.pack()
    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message','Hello,%s'%name)

# 3 实例化
app = Application()
# 设置标题
app.master.title('HelloWorld')
# 主消息循环:GUI程序的主线程负责监听来自操作系统的消息
app.mainloop()