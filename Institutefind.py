import tkinter
from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import pymysql
def showInstitutefind():
    t=tkinter.Tk()
    t.geometry ('700x700')
    t.title('institute')
    r=Label(t,text='Institute Find Form',font=('arial',20),fg='red',bg='skyblue')
    r.place(x=120,y=10)
    t.config(bg='teal')
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='institutemanagement')
        cur=db.cursor()
        xa=int(e1.get())
        sql="select name,address,phone,email,regno from Institute where instid=%d" %(xa)
        cur.execute(sql)
        data=cur.fetchone()
        e2.insert(0,data[0])
        e3.insert(0,data[1])
        e4.insert(0,data[2])
        e5.insert(0,data[3])
        e6.insert(0,data[4])
        db.close()
    
    def filldata():
                        db=pymysql.connect(host='localhost',user='root',password='root',database='institutemanagement')
                        cur=db.cursor()
                        sql="select instid from Institute"
                        cur.execute(sql)
                        m=[]
                        data=cur.fetchall()
                        for r in data:
                            m.append(r[0])
                        db.close()
                        e1['values']=m
    
    
    a=Label(t,text='instid',bg='teal',fg='white')
    a.place(x=50,y=50)
    e1=ttk.Combobox(t)
    e1.place(x=400,y=50)
    b=Label(t,text='name',bg='teal',fg='white')
    b.place(x=50,y=90)
    e2=Entry(t,width=20)
    e2.place(x=400,y=90)
    c=Label(t,text='address',bg='teal',fg='white')
    c.place(x=50,y=130)
    e3=Entry(t,width=20)
    e3.place(x=400,y=130)
    d=Label(t,text='phone',bg='teal',fg='white')
    d.place(x=50,y=170)
    e4=Entry(t,width=20)
    e4.place(x=400,y=170)
    e=Label(t,text='email',bg='teal',fg='white')
    e.place(x=50,y=210)
    e5=Entry(t,width=20)
    e5.place(x=400,y=210)
    f=Label(t,text='regno',bg='teal',fg='white')
    f.place(x=50,y=250)
    e6=Entry(t,width=20)
    e6.place(x=400,y=250)
    b1=Button(t,text='find',bg='green',command=finddata,width=20)
    b1.place(x=50,y=300)
    
    filldata()
    t.mainloop()

