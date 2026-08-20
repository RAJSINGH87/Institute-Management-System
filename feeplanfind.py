import tkinter
from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import pymysql
def showfeeplanfind():
    t=tkinter.Tk()
    t.geometry ('700x700')
    t.title('institute')
    r=Label(t,text='Feeplan Find Form',font=('arial',20,'bold'),fg='red',bg='white')
    r.place(x=120,y=10)
    t.config(bg='navy')
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='institutemanagement')
        cur=db.cursor()
        xa=int(e1.get())
        sql="select totalfee,numberofinstallments from feeplan where feeplanid=%d" %(xa)
        cur.execute(sql)
        data=cur.fetchone()
        e2.insert(0,data[0])
        e3.insert(0,data[1])
        db.close()
    
    def filldata():
                        db=pymysql.connect(host='localhost',user='root',password='root',database='institutemanagement')
                        cur=db.cursor()
                        sql="select feeplanid from feeplan"
                        cur.execute(sql)
                        m=[]
                        data=cur.fetchall()
                        for r in data:
                            m.append(r[0])
                        db.close()
                        e1['values']=m
    
    a=Label(t,text='feeplanid',bg='white')
    a.place(x=50,y=50)
    e1=ttk.Combobox(t)
    e1.place(x=400,y=50)
    b=Label(t,text='totalfee',bg='white')
    b.place(x=50,y=90)
    e2=Entry(t,width=20)
    e2.place(x=400,y=90)
    c=Label(t,text='no.ofinstallments',bg='white')
    c.place(x=50,y=130)
    e3=Entry(t,width=20)
    e3.place(x=400,y=130)
    
    b1=Button(t,text='find',bg='green',command=finddata,width=20)
    b1.place(x=100,y=200)
    
    filldata()
    t.mainloop()

