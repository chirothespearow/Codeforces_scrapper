from bs4 import BeautifulSoup
import tkinter
from tkinter import scrolledtext
from tabulate import tabulate
from tkinter import messagebox
import requests
def info():
    try:
        usr=name.get()
        url=requests.get('https://codeforces.com/api/user.info?handles='+usr)#DmitriyH
        soup = BeautifulSoup(url.text,'lxml')
        a=(soup.get_text())
        b=eval(a)
        d={}
        d.update(b['result'][0])
        rank=d['rank']
        handle=d['handle']
        cur_rating=d['rating']
        max_rating=d['maxRating']
        max_rank=d['maxRank']
        adwindow=tkinter.Toplevel()
        adwindow.title('User Details')
        adwindow.geometry('300x120+120+120')
        table=[['Rank',rank],['Handle',handle],['Rating',cur_rating],['Max Rating',max_rating],['Max Rank',max_rank]]
        x=(tabulate(table, tablefmt="psql"))
        label=scrolledtext.ScrolledText(adwindow,height=150,width=850)
        label.pack()
        label.insert(tkinter.INSERT,x)
        label.config(state=tkinter.DISABLED)
    except:
         messagebox.showerror('Error!',"Either the handle you entered is not valid, or is not experienced enough and lacks required information.")

    
window=tkinter.Tk()
window.title('Airport Management System')
window.geometry('400x250+120+120')
window.configure(bg='sky blue')
label=tkinter.Label(window,text='Codeforces Scrapper',font='Menlo 30',bg='Sky Blue',bd=10 ,fg='Black').place(x=5,y=10)
tkinter.Label(window,text='Enter User Handle:').place(x=150,y=100)
name=tkinter.Entry(window,font='Menlo')
name.focus_set()
name.place(x=110,y=150)
tkinter.Button(window,text='Submit',width=5,height=1,command=info).place(x=180,y=200)
window.mainloop()