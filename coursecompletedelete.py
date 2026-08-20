import tkinter
from tkinter import*
from tkinter import messagebox
import pymysql
from tkinter import ttk
def showcoursecompletedelete():

    t=tkinter.Tk()
    t.geometry ('700x700')
    t.title('course')
    t.config(bg='yellow')
    r=Label(t,text='coursecomplete Delete Form',font=('arial',15),fg='black',bg='blue')
    r.place(x=120,y=10)
    
    def deletedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='institutemanagement')
        cur=db.cursor()
        xa=int(e1.get())
        sql="delete from coursecomplete where regno=%d" %(xa)
        cur.execute(sql)
        db.commit()
        db.close()
        messagebox.showinfo('Hi','Deleted')
        e1.delete(0,END)
    a=Label(t,text='regno')
    a.place(x=50,y=50)
    e1=Entry(t,width=20)
    e1.place(x=200,y=50)    
    bt1=Button(t,text='Delete',command=deletedata)
    bt1.place(x=100,y=100)
    t.mainloop()