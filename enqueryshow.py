import tkinter
from tkinter import*
from tkinter import messagebox
import pymysql
def showenqueryshow():

    t=tkinter.Tk()
    t.geometry('700x700')
    t.title('enquery')
    ta=Text(t,width=70,height=20)
    ta.place(x=100,y=50)
    t.config(bg='orange')
    r=Label(t,text='Enquery Show Form',font=('arial',20),fg='black',bg='pink')
    r.place(x=120,y=10)
    
    def showdata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='institutemanagement')
        cur=db.cursor()
        msg=""
        sql="select * from enquery"
        cur.execute(sql)
        data=cur.fetchall()
        for r in data:
            msg=msg+"\n"+str(r[0])
            msg=msg+"\t"+r[1]
            msg=msg+"\t"+r[2]
            msg=msg+"\t"+str(r[3])
            msg=msg+"\t"+r[4]
        db.close()
        ta.insert(END,msg)
    showdata()
    t.mainloop()
    

