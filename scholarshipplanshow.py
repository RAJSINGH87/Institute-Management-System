import tkinter
from tkinter import*
from tkinter import messagebox
import pymysql
def showscholarshipplanshow():
    t=tkinter.Tk()
    t.geometry('700x700')
    t.title('institute')
    t.config(bg='pink')
    r=Label(t,text='Scholarshipplan Show Form',font=('arial',20),fg='black',bg='white')
    r.place(x=120,y=10)
    
    ta=Text(t,width=70,height=20)
    ta.place(x=100,y=50)
    def showdata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='institutemanagement')
        cur=db.cursor()
        msg=""
        sql="select * from scholarshipplan"
        cur.execute(sql)
        data=cur.fetchall()
        for r in data:
            msg=msg+"\n"+str(r[0])
            msg=msg+"\t"+r[1]
            msg=msg+"\t"+r[2]
        db.close()
        ta.insert(END,msg)
    showdata()
    t.mainloop()
    
    
