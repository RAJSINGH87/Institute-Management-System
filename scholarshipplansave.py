import tkinter
from tkinter import*
from tkinter import messagebox
import pymysql
def showscholarshipplansave():
    t=tkinter.Tk()
    t.geometry ('700x700')
    t.title('institute')
    t.config(bg='pink')
    r=Label(t,text='Scholarshipplan Save Form',font=('arial',20),fg='black',bg='white')
    r.place(x=120,y=10)
    
    def savedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='institutemanagement')
        cur=db.cursor()
        xa=int(e1.get())
        xb=e2.get()
        xc=e3.get()
        sql="insert into scholarshipplan values (%d,'%s','%s')" % (xa,xb,xc)
        cur.execute(sql)
        db.commit()
        messagebox.showinfo('Hi','Saved')
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        
    a=Label(t,text='scholarshipplanid',bg='teal',fg='white')
    a.place(x=50,y=50)
    e1=Entry(t,width=20)
    e1.place(x=400,y=50)
    b=Label(t,text='courseid',bg='teal',fg='white')
    b.place(x=50,y=90)
    e2=Entry(t,width=20)
    e2.place(x=400,y=90)
    c=Label(t,text='amount',bg='teal',fg='white')
    c.place(x=50,y=130)
    e3=Entry(t,width=20)
    e3.place(x=400,y=130)
    
    
    b1=Button(t,text='Save',bg='green',command=savedata)
    b1.place(x=50,y=300)
    b2=Button(t,text='Close')
    b2.place(x=400,y=300)
    t.mainloop()