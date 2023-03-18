import requests
import time
import webbrowser
import os
import tkinter as tk
import tkinter.messagebox
from win11toast import toast

def show_warning(msg):
    top = tkinter.Tk()
    top.withdraw()
    top.update()
    tk.messagebox.showwarning('提示',msg)
    top.destroy()

def post_message(username,password,key):
    url = 'http://172.16.200.11/'
    d = {'DDDDD': username,
         'upass': password,
         '0MKKey': key}
    response = requests.post(url, data=d)
    if ('您已经成功登录' in response.text):
        #show_warning('成功上网！')
        toast('成功上网！')
    else:
        time.sleep(1)
        #show_warning('将会打开浏览器访问登录网址')
        #webbrowser.open('http://172.16.200.11/')
        toast('配置错误，将会打开浏览器访问登录网址','点击进入', on_click='http://172.16.200.11/')

if __name__ == '__main__':
    username = '********'
    password = '******'
    key = '***'
    post_message(username, password, key)




