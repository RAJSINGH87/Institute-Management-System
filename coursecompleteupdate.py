import tkinter 
from tkinter import *
from tkinter import messagebox
import pymysql
from tkinter import ttk
def showcoursecompleteupdate():

    t=tkinter.Tk()
    t.geometry('700x700')
    t.title('course')
    t.config(bg='yellow')
    r=Label(t,text='coursecomplete Update Form',font=('arial',20),fg='black',bg='blue')
    r.place(x=120,y=10)
    
    def updatedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='institutemanagement')
        cur=db.cursor()
        xa=int(e1.get())
        xb=e2.get()
        xc=e3.get()
         
        sql="update coursecomplete set courseid='%s',dateofcomplete='%s' where regno=%d"%(xb,xc,xa)
        cur.execute(sql)
        db.commit()
        db.close()
        messagebox.showinfo('hi','done')
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='institutemanagement')
        cur=db.cursor()
        xa=int(e1.get())
        sql="select courseid,dateofcomplete  from coursecomplete where regno=%d" %(xa)
        cur.execute(sql)
        data=cur.fetchone()
        e2.insert(0,data[0])
        e3.insert(0,data[1])
        db.close()
    def filldata():
                        db=pymysql.connect(host='localhost',user='root',password='root',database='institutemanagement')
                        cur=db.cursor()
                        sql="select regno from coursecomplete"
                        cur.execute(sql)
                        m=[]
                        data=cur.fetchall()
                        for r in data:
                            m.append(r[0])
                        db.close()
                        e1['values']=m
       
    a=Label(t,text='regno',bg='teal',fg='white')
    a.place(x=50,y=50)
    e1=ttk.Combobox(t)
    e1.place(x=400,y=50)
    b=Label(t,text='courseid',bg='teal',fg='white')
    b.place(x=50,y=90)
    e2=Entry(t,width=20)
    e2.place(x=400,y=90)
    c=Label(t,text='dateofcomplete',bg='teal',fg='white')
    c.place(x=50,y=180)
    e3=Entry(t,width=20)
    e3.place(x=400,y=180)
    b1=Button(t,text='find',bg='green',command=finddata,width=20)
    b1.place(x=50,y=250)
    b2=Button(t,text='update',command=updatedata,bg='red',width=20)
    b2.place(x=400,y=250)
    filldata()
    
    t.mainloop()
  
