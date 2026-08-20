import tkinter
from tkinter import*
from tkinter import messagebox
import pymysql
def showcertificatesave():

    t=tkinter.Tk()
    t.geometry ('700x700')
    t.title('certificate')
    t.config(bg='brown')
    r=Label(t,text='Certificate Save Form',font=('arial',20),fg='black',bg='white')
    r.place(x=120,y=10)
    
    def savedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='institutemanagement')
        cur=db.cursor()
        xa=int(e1.get())
        xb=e2.get()
        xc=e3.get()
        xd=e4.get()
    
    
        sql="insert into certificate values (%d,'%s','%s','%s')" % (xa,xb,xc,xd)
        cur.execute(sql)
        db.commit()
        messagebox.showinfo('Hi','Saved')
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
    
    
        
    a=Label(t,text='regno',bg='teal',fg='white')
    a.place(x=50,y=50)
    e1=Entry(t,width=20)
    e1.place(x=400,y=50)
    b=Label(t,text='name',bg='teal',fg='white')
    b.place(x=50,y=90)
    e2=Entry(t,width=20)
    e2.place(x=400,y=90)
    c=Label(t,text='certificatename',bg='teal',fg='white')
    c.place(x=50,y=180)
    e3=Entry(t,width=20)
    e3.place(x=400,y=180)
    d=Label(t,text='dateofissue',bg='teal',fg='white')
    d.place(x=50,y=250)
    e4=Entry(t,width=20)
    e4.place(x=400,y=250)
    
    
    b1=Button(t,text='Save',bg='green',command=savedata)
    b1.place(x=50,y=350)
    b2=Button(t,text='Close')
    b2.place(x=400,y=400)
    
    t.mainloop()
