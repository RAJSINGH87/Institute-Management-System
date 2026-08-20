import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql


from certificatesave import*
from certificatedelete import*
from certificateshow import*
from certificatefind import*
from certificateupdate import*

from Institutesave import*
from Institutedelete import*
from Instituteshow import*
from Instituteupdate import*
from Institutefind import*


from feeplansave import*
from feeplandelete import*
from feeplanfind import*
from feeplanshow import*
from feeplanupdate import*

from coursesupdate import*
from coursesdelete import*
from coursesshow import*
from coursesfind import*
from coursessave import*

from scholarshipplandelete import*
from scholarshipplansave import*
from scholarshipplanupdate import*
from scholarshipplanshow import*
from scholarshipplanfind import*


from enquerydelete import*
from enquerysave import*
from enqueryshow import*
from enqueryfind import*
from enqueryupdate import*

from batchesdelete import*
from batchessave import*
from batchesshow import*
from batchesfind import*
from batchesupdate import*


from registrationdelete import*
from registrationshow import*
from registrationsave import*
from registrationfind import*
from registrationupdate import*

from examdelete import*
from examsave import*
from examfind import*
from examshow import*
from examupdate import*

from coursecompleteupdate import*
from coursecompletedelete import*
from coursecompletesave import*
from coursecompletefind import*
from coursecompleteshow import*

t=tkinter.Tk()    
t.geometry('1500x1500')
t.title('institution registration')
j=Label(t,text='Student Registration Dashboard',font=('arial',20),fg='blue',bg='pink')
j.place(x=400,y=25)
t.config(bg='#0f172a')

    


    
a=Label(t,text='Institute',font=('arial',15))
a.place(x=50,y=70)
b1=Button(t,text='find',command=showInstitutefind,bg='purple',fg='black',width=8)
b1.place(x=50,y=150)
    
b2=Button(t,text='show',command=showInstituteshow,bg='purple',fg='black',width=8)
b2.place(x=50,y=250)
    
b3=Button(t,text='save',command=showInstitutesave,bg='purple',fg='black',width=8)
b3.place(x=50,y=350)
    
b4=Button(t,text='update',command=showInstituteupdate,bg='purple',fg='black',width=8)
b4.place(x=50,y=450)
    
b5=Button(t,text='delete',command=showInstitutedelete,bg='purple',fg='black',width=8)
b5.place(x=50,y=550)
    
    
    
b=Label(t,text='Fee plan',font=('arial',15))
b.place(x=150,y=70)
    
b6=Button(t,text='find',command=showfeeplanfind,bg='cyan',fg='black',width=8)
b6.place(x=150,y=150)
    
b7=Button(t,text='show',command=showfeeplanshow,bg='cyan',fg='black',width=8)
b7.place(x=150,y=250)
    
b8=Button(t,text='save',command=showfeeplansave,bg='cyan',fg='black',width=8)
b8.place(x=150,y=350)
    
b9=Button(t,text='update',command=showfeeplanupdate,bg='cyan',fg='black',width=8)
b9.place(x=150,y=450)
    
b10=Button(t,text='delete',command=showfeeplandelete,bg='cyan',fg='black',width=8)
b10.place(x=150,y=550)
    
    
    
c=Label(t,text='courses',font=('arial',15))
c.place(x=250,y=70)    
b11=Button(t,text='find',command=showcoursesfind,bg='red',fg='black',width=8)
b11.place(x=250,y=150)
    
b12=Button(t,text='show',command=showcoursesshow,bg='red',fg='black',width=8)
b12.place(x=250,y=250)
b13=Button(t,text='save',command=showcoursessave,bg='red',fg='black',width=8)
b13.place(x=250,y=350)
    
b14=Button(t,text='update',command=showcoursesupdate,bg='red',fg='black',width=8)
b14.place(x=250,y=450)
    
b15=Button(t,text='delete',command=showcoursesdelete,bg='red',fg='black',width=8)
b15.place(x=250,y=550)
    
    
    
    
d=Label(t,text='Scholarshipplan',font=('arial',15))
d.place(x=350,y=70)

b16=Button(t,text='find',command=showscholarshipplanfind,bg='pink',fg='black',width=8)
b16.place(x=370,y=150)

b17=Button(t,text='show',command=showscholarshipplanshow,bg='pink',fg='black',width=8)
b17.place(x=370,y=250)

b18=Button(t,text='save',command=showscholarshipplansave,bg='pink',fg='black',width=8)
b18.place(x=370,y=350)

b19=Button(t,text='update',command=showscholarshipplanupdate,bg='pink',fg='black',width=8)
b19.place(x=370,y=450)

b20=Button(t,text='delete',command=showscholarshipplandelete,bg='pink',fg='black',width=8)
b20.place(x=370,y=550)




e=Label(t,text='Enquery',font=('arial',15))
e.place(x=510,y=70)

b21=Button(t,text='find',command=showenqueryfind,bg='teal',fg='black',width=8)
b21.place(x=490,y=150)

b22=Button(t,text='show',command=showenqueryshow,bg='teal',fg='black',width=8)
b22.place(x=490,y=250)

b23=Button(t,text='save',command=showenquerysave,bg='teal',fg='black',width=8)
b23.place(x=490,y=350)

b24=Button(t,text='update',command=showenqueryupdate,bg='teal',fg='black',width=8)
b24.place(x=490,y=450)

b25=Button(t,text='delete',command=showenquerydelete,bg='teal',fg='black',width=8)
b25.place(x=490,y=550)


    
    
f=Label(t,text='Batches',font=('arial',15))
f.place(x=600,y=70)
    
b26=Button(t,text='find',command=showbatchesfind,bg='dark green',fg='black',width=8)
b26.place(x=600,y=150)
    
b27=Button(t,text='show',command=showbatchesshow,bg='dark green',fg='black',width=8)
b27.place(x=600,y=250)
    
b28=Button(t,text='save',command=showbatchessave,bg='dark green',fg='black',width=8)  
b28.place(x=600,y=350)
    
b29=Button(t,text='update',command=showbatchesupdate,bg='dark green',fg='black',width=8)
b29.place(x=600,y=450)
    
b30=Button(t,text='delete',command=showbatchesdelete,bg='dark green',fg='black',width=8)
b30.place(x=600,y=550)
    
    
    
g=Label(t,text='Registration',font=('arial',15))
g.place(x=700,y=70)
    
b31=Button(t,text='find',command=showregistrationfind,bg='light coral',fg='black',width=8)
b31.place(x=710,y=150)
    
b32=Button(t,text='show',command=showregistrationshow,bg='light coral',fg='black',width=8)
b32.place(x=710,y=250)
    
b33=Button(t,text='save',command=showregistrationsave,bg='light coral',fg='black',width=8)
b33.place(x=710,y=350)
    
b34=Button(t,text='update',command=showregistrationupdate,bg='light coral',fg='black',width=8)
b34.place(x=710,y=450)
    
b35=Button(t,text='delete',command=showregistrationdelete,bg='light coral',fg='black',width=8)
b35.place(x=710,y=550)
    
    
    
    
h=Label(t,text='Exams',font=('arial',15))
h.place(x=850,y=70)
    
b36=Button(t,text='find',command=showexamfind,fg='black',bg='yellow',width=8)
b36.place(x=850,y=150)
    
b37=Button(t,text='show',command=showexamshow,fg='black',bg='yellow',width=8)
b37.place(x=850,y=250)
    
b38=Button(t,text='save',command=showexamsave,fg='black',bg='yellow',width=8)
b38.place(x=850,y=350)
    
b39=Button(t,text='update',command=showexamupdate,fg='black',bg='yellow',width=8)
b39.place(x=850,y=450)
    
b40=Button(t,text='delete',command=showexamdelete,fg='black',bg='yellow',width=8)
b40.place(x=850,y=550)
    
    
    
    
i=Label(t,text='Coursecomplete',font=('arial',15))
i.place(x=950,y=70)
    
b41=Button(t,text='find',command=showcoursecompletefind,fg='black',bg='navy',width=8)
b41.place(x=980,y=150)
    
b42=Button(t,text='show',command=showcoursecompleteshow,fg='black',bg='navy',width=8)
b42.place(x=980,y=250)
    
b43=Button(t,text='save',command=showcoursecompletesave,fg='black',bg='navy',width=8)
b43.place(x=980,y=350)
    
b44=Button(t,text='update',command=showcoursecompleteupdate,fg='black',bg='navy',width=8)
b44.place(x=980,y=450)
    
b45=Button(t,text='delete',command=showcoursecompletedelete,fg='black',bg='navy',width=8)
b45.place(x=980,y=550)
    
    
    
j=Label(t,text='Certificateissue',font=('arial',15))
j.place(x=1120,y=70)
    
b46=Button(t,text='find',command=showcertificatefind,fg='black',bg='dark red',width=8)
b46.place(x=1130,y=150)
    
b47=Button(t,text='show',command=showcertificateshow,fg='black',bg='dark red',width=8)
b47.place(x=1130,y=250)
    
b48=Button(t,text='save',command=showcertificatesave,fg='black',bg='dark red',width=8)
b48.place(x=1130,y=350)
    
b49=Button(t,text='update',command=showcertificateupdate,fg='black',bg='dark red',width=8)
b49.place(x=1130,y=450)
b50=Button(t,text='delete',command=showcertificatedelete,fg='black',bg='dark red',width=8)
b50.place(x=1130,y=550)
    
t.mainloop()