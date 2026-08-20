import tkinter 
from tkinter import *
from tkinter import messagebox
import pymysql
from tkinter import ttk
def showenqueryupdate():

    t=tkinter.Tk()
    t.geometry('700x700')
    t.title('enquery')
    t.config(bg='orange')
    r=Label(t,text='Enquery Update Form',font=('arial',20),fg='black',bg='pink')
    r.place(x=120,y=10)
    
    def updatedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='institutemanagement')
        cur=db.cursor()
        xa=int(e1.get())
        xb=e2.get()
        xc=e3.get()
        xd=e4.get()
        xe=e5.get()
        xf=e6.get()
         
        sql="update enquery set name='%s',address='%s',email='%s',phone='%s',courseid='%s' where enqno=%d"%(xb,xc,xd,xe,xf,xa)
        cur.execute(sql)
        db.commit()
        db.close()
        messagebox.showinfo('hi','done')
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e6.delete(0,END)
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='institutemanagement')
        cur=db.cursor()
        xa=int(e1.get())
        sql="select enqno,name,address,email,phone,courseid from enquery where enqno=%d" %(xa)
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
                        sql="select enqno from enquery"
                        cur.execute(sql)
                        m=[]
                        data=cur.fetchall()
                        for r in data:
                            m.append(r[0])
                        db.close()
                        e1['values']=m
    
    a=Label(t,text='enqno',bg='teal',fg='white')
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
    d=Label(t,text='email',bg='teal',fg='white')
    d.place(x=50,y=150)
    e4=Entry(t,width=20)
    e4.place(x=400,y=150)
    e=Label(t,text='phone',bg='teal',fg='white')
    e.place(x=50,y=150)
    e5=Entry(t,width=20)
    e5.place(x=400,y=150)
    f=Label(t,text='courseid',bg='teal',fg='white')
    f.place(x=50,y=200)
    e6=Entry(t,width=20)
    e6.place(x=400,y=200)
    b1=Button(t,text='find',bg='green',command=finddata)
    b1.place(x=50,y=300)
    b2=Button(t,text='update',bg='green',command=updatedata)
    b2.place(x=250,y=300)
    
    
    
    
    filldata()
    
    t.mainloop()

