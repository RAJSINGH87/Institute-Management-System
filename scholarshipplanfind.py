import tkinter 
from tkinter import *
from tkinter import messagebox
import pymysql
from tkinter import ttk
def showscholarshipplanfind():
    t=tkinter.Tk()
    t.geometry('700x700')
    t.title('Institute')
    t.config(bg='pink')
    r=Label(t,text='Scholarshipplan Find Form',font=('arial',20),fg='black',bg='white')
    r.place(x=120,y=10)
    
    
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='institutemanagement')
        cur=db.cursor()
        xa=int(e1.get())
        sql="select courseid,amount from scholarshipplan where scholarshipplanid=%d" %(xa)
        cur.execute(sql)
        data=cur.fetchone()
        e2.insert(0,data[0])
        e3.insert(0,data[1])
        db.close()
    def filldata():
                        db=pymysql.connect(host='localhost',user='root',password='root',database='institutemanagement')
                        cur=db.cursor()
                        sql="select scholarshipplanid from scholarshipplan"
                        cur.execute(sql)
                        m=[]
                        data=cur.fetchall()
                        for r in data:
                            m.append(r[0])
                        db.close()
                        e1['values']=m
    
    a=Label(t,text='scholarshipplanid',bg='teal',fg='white')
    a.place(x=50,y=50)
    e1=ttk.Combobox(t)
    e1.place(x=400,y=50)
    b=Label(t,text='courseid',bg='teal',fg='white')
    b.place(x=50,y=90)
    e2=Entry(t,width=20)
    e2.place(x=400,y=90)
    c=Label(t,text='amount',bg='teal',fg='white')
    c.place(x=50,y=130)
    e3=Entry(t,width=20)
    e3.place(x=400,y=130)
    
    
    b1=Button(t,text='find',bg='green',command=finddata,width=20)
    b1.place(x=50,y=250)
    filldata()
    t.mainloop()

