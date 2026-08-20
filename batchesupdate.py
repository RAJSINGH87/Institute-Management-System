import tkinter 
from tkinter import *
from tkinter import messagebox
import pymysql
from tkinter import ttk
def showbatchesupdate():

    t=tkinter.Tk()
    t.geometry('700x700')
    t.title('batches')
    t.config(bg='gold')
    r=Label(t,text='Batches Update Form',font=('arial',20),fg='black',bg='red')
    r.place(x=120,y=10)
    
    def updatedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='institutemanagement')
        cur=db.cursor()
        xa=int(e1.get())
        xb=e2.get()
        xc=e3.get()
        xd=e4.get()
        xe=e5.get()
        
         
        sql="update batches set startdate='%s',enddate='%s',fromtime='%s',totime='%s' where batchid=%d"%(xb,xc,xd,xe,xa)
        cur.execute(sql)
        db.commit()
        db.close()
        messagebox.showinfo('hi','done')
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='institutemanagement')
        cur=db.cursor()
        xa=int(e1.get())
        sql="select startdate,enddate,fromtime,totime  from batches where batchid=%d" %(xa)
        cur.execute(sql)
        data=cur.fetchone()
        e2.insert(0,data[0])
        e3.insert(0,data[1])
        e4.insert(0,data[2])
        e5.insert(0,data[3])
        db.close()
    def filldata():
                        db=pymysql.connect(host='localhost',user='root',password='root',database='institutemanagement')
                        cur=db.cursor()
                        sql="select batchid from batches"
                        cur.execute(sql)
                        m=[]
                        data=cur.fetchall()
                        for r in data:
                            m.append(r[0])
                        db.close()
                        e1['values']=m
    
    a=Label(t,text='batchid',bg='teal',fg='white')
    a.place(x=50,y=50)
    e1=ttk.Combobox()
    e1.place(x=400,y=50)
    b=Label(t,text='startdate',bg='teal',fg='white')
    b.place(x=50,y=90)
    e2=Entry(t,width=20)
    e2.place(x=400,y=90)
    c=Label(t,text='enddate',bg='teal',fg='white')
    c.place(x=50,y=180)
    e3=Entry(t,width=20)
    e3.place(x=400,y=180)
    d=Label(t,text='fromtime',bg='teal',fg='white')
    d.place(x=50,y=250)
    e4=Entry(t,width=20)
    e4.place(x=400,y=250)
    e=Label(t,text='totime',bg='teal',fg='white')
    e.place(x=50,y=300)
    e5=Entry(t,width=20)
    e5.place(x=400,y=300)
    
    b1=Button(t,text='find',bg='green',command=finddata,width=20)
    b1.place(x=50,y=350)
    b2=Button(t,text='update',command=updatedata,bg='red',width=20)
    b2.place(x=400,y=350)
    filldata()
    t.mainloop()
