import tkinter
from tkinter import*
from tkinter import messagebox
import pymysql
def showcoursecompleteshow():

    t=tkinter.Tk()
    t.geometry('700x700')
    t.title('course')
    t.config(bg='yellow')
    r=Label(t,text='coursecomplete Show Form',font=('arial',20),fg='black',bg='blue')
    r.place(x=120,y=10)
    
    ta=Text(t,width=70,height=20)
    ta.place(x=100,y=50)
    def showdata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='institutemanagement')
        cur=db.cursor()
        msg=""
        sql="select * from coursecomplete"
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
    
    
