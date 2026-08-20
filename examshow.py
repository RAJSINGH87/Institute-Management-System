import tkinter
from tkinter import*
from tkinter import messagebox
import pymysql
def showexamshow():
    t=tkinter.Tk()
    t.geometry('700x700')
    t.title('exam')
    t.config(bg='purple')
    r=Label(t,text='Exam Show Form',font=('arial',20),fg='black',bg='yellow')
    r.place(x=120,y=10)
    
    ta=Text(t,width=70,height=20)
    ta.place(x=100,y=50)
    def showdata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='institutemanagement')
        cur=db.cursor()
        msg=""
        sql="select * from exam"
        cur.execute(sql)
        data=cur.fetchall()
        for r in data:
            msg=msg+"\n"+str(r[0])
            msg=msg+"\t"+r[1]
            msg=msg+"\t"+r[2]
            msg=msg+"\t"+str(r[3])
        
        db.close()
        ta.insert(END,msg)
    showdata()
    t.mainloop()
    
    
