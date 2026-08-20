import tkinter
from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import pymysql
def showcoursesupdate():
    t=tkinter.Tk()
    t.geometry ('700x700')
    t.title('institute')
    t.config(bg='red')
    r=Label(t,text='Courses Update Form',font=('arial',20),fg='black',bg='white')
    r.place(x=120,y=10)
    
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='institutemanagement')
        cur=db.cursor()
        xa=int(e1.get())
        sql="select cname,durationmonth,feeplanid from courses where courseid=%d" %(xa)
        cur.execute(sql)
        data=cur.fetchone()
        e2.insert(0,data[0])
        e3.insert(0,data[1])
        e4.insert(0,data[2])
        db.close()
    
    
    def filldata():
                        db=pymysql.connect(host='localhost',user='root',password='root',database='institutemanagement')
                        cur=db.cursor()
                        sql="select courseid from courses"
                        cur.execute(sql)
                        m=[]
                        data=cur.fetchall()
                        for r in data:
                            m.append(r[0])
                        db.close()
                        e1['values']=m
    
    def updatedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='institutemanagement')
        cur=db.cursor()
        xa=int(e1.get())
        xb=e2.get()
        xc=e3.get()
        xd=e4.get()
      
        sql="update courses set cname='%s',durationmonth='%s',feeplanid='%s' where courseid=%d"%(xb,xc,xd,xa)
        cur.execute(sql)
        db.commit()
        db.close()
        messagebox.showinfo('hi','done')
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
    a=Label(t,text='courseid',bg='teal',fg='white')
    a.place(x=50,y=50)
    e1=ttk.Combobox(t)
    e1.place(x=400,y=50)
    b=Label(t,text='cname',bg='teal',fg='white')
    b.place(x=50,y=90)
    e2=Entry(t,width=20)
    e2.place(x=400,y=90)
    c=Label(t,text='durationmonth',bg='teal',fg='white')
    c.place(x=50,y=130)
    e3=Entry(t,width=20)
    e3.place(x=400,y=130)
    d=Label(t,text='feeplanid',bg='teal',fg='white')
    d.place(x=50,y=170)
    e4=Entry(t,width=20)
    e4.place(x=400,y=170)
    
    b1=Button(t,text='update',bg='green',command=updatedata,width=20)
    b1.place(x=50,y=250)
    b2=Button(t,text='find',command=finddata,width=20,bg='red')
    b2.place(x=400,y=250)
    filldata()
    t.mainloop()

