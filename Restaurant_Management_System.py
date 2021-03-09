from tkinter import *
import tkinter as tk
import datetime
import random
from tkinter import messagebox


screen=Tk()
screen.config(bg='#4d4b31')
screen.title("R M S")
screen.geometry('1350x750+0+0')


#-----------------------------------------------------------top frame

topframe=Frame(screen,relief=RAISED,bg='blue',bd=10,width=250,height=250)
topframe.pack(side=TOP)

reglabel=Label(topframe,text='RESTUARANTS MANAGEMENT SYSTEM',font=('bold',50),bg='pink',borderwidth=10,justify=CENTER)
reglabel.grid(row=0,column=0)


leftframe=Frame(screen,bg='yellow',relief=SUNKEN)
# leftframe.pack(side=LEFT)
leftframe.place(x=0,y=120)
lefttop=Frame(leftframe,relief=SUNKEN,padx=10,pady=20)
lefttop.pack(side=LEFT)

leftbottom=Frame(leftframe,relief=SUNKEN,padx=10,pady=20)
leftbottom.pack(side=RIGHT)


#----------------------command of check button food and drink

def chkburger():
    if v1.get()==1:
        e1.config(state=NORMAL)             #here we config entry from disable to normal
        e1.focus()
        e1.delete(0,END)



    elif v1.get()==0:
        e1.insert(0,0)
        e1.config(state=DISABLED)
        e1.focus()
        e1.delete(0,END)

def chkpizza():
    if v2.get()==1:
        e2.config(state=NORMAL)
        e2.focus()
        e2.delete(0,END)



    elif v2.get()==0:
        e2.insert(0,0)
        e2.config(state=DISABLED)
        e2.focus()
        e2.delete(0,END)

def chksandwich():
    if v3.get()==1:
        e3.config(state=NORMAL)
        e3.focus()
        e3.delete(0,END)



    elif v3.get()==0:
        e3.insert(0,0)
        e3.config(state=DISABLED)
        e3.focus()
        e3.delete(0,END)

def chksalad():
    if v4.get()==1:
        e4.config(state=NORMAL)
        e4.focus()
        e4.delete(0,END)



    elif v4.get()==0:
        e4.insert(0,0)
        e4.config(state=DISABLED)
        e4.focus()
        e4.delete(0,END)

def chkcoffee():
    if v5.get()==1:
        e5.config(state=NORMAL)
        e5.focus()
        e5.delete(0,END)



    elif v5.get()==0:
        e5.insert(0,0)
        e5.config(state=DISABLED)
        e5.focus()
        e5.delete(0,END)

def chktea():
    if v6.get()==1:
        e6.config(state=NORMAL)
        e6.focus()
        e6.delete(0,END)



    elif v6.get()==0:
        e6.insert(0,0)
        e6.config(state=DISABLED)
        e6.focus()
        e6.delete(0,END)


def chkmojito():
    if v7.get()==1:
        e7.config(state=NORMAL)
        e7.focus()
        e7.delete(0,END)



    elif v7.get()==0:
        e7.insert(0,0)
        e7.config(state=DISABLED)
        e7.focus()
        e7.delete(0,END)

def chkshake():
    if v8.get()==1:
        e8.config(state=NORMAL)
        e8.focus()
        e8.delete(0,END)



    elif v8.get()==0:
        e8.insert(0,0)
        e8.config(state=DISABLED)
        e8.focus()
        e8.delete(0,END)

#***************************************************FOOD  checkbutton and entry made on left frame***********

global v1,v2,v3,v4,v5,v6,v7,v8

v1=IntVar()
v2=IntVar()
v3=IntVar()
v4=IntVar()
v5=IntVar()
v6=IntVar()
v7=IntVar()
v8=IntVar()



cb=Checkbutton(lefttop,text='BURGER 100x',font=('bold',15),bg='white',relief=SUNKEN,borderwidth=5,variable=v1,onvalue=1,offvalue=0,command=chkburger)
cb.grid(row=0,sticky=W)

cp=Checkbutton(lefttop,text='PIZZA 100x',font=('bold',18),bg='white',relief=SUNKEN,borderwidth=5,variable=v2,onvalue=1,offvalue=0,command=chkpizza)
cp.grid(row=1,sticky=W)

cs=Checkbutton(lefttop,text='SANDWICH 50x',font=('bold',18),bg='white',relief=SUNKEN,borderwidth=5,variable=v3,onvalue=1,offvalue=0,command=chksandwich)
cs.grid(row=2,sticky=W)

csa=Checkbutton(lefttop,text='SALAD 50x',font=('bold',18),bg='white',relief=SUNKEN,borderwidth=5,variable=v4,onvalue=1,offvalue=0,command=chksalad)
csa.grid(row=3,sticky=W)

e1=Entry(lefttop,borderwidth=10,bg='white')
e1.grid(row=0,column=1)
e1.insert(0,0)
e1.config(state=DISABLED)

e2=Entry(lefttop,borderwidth=10,bg='white')
e2.grid(row=1,column=1)
e2.insert(0,0)
e2.config(state=DISABLED)

e3=Entry(lefttop,borderwidth=10,bg='white')
e3.grid(row=2,column=1)
e3.insert(0,0)
e3.config(state=DISABLED)

e4=Entry(lefttop,borderwidth=10,bg='white')
e4.grid(row=3,column=1)
e4.insert(0,0)
e4.config(state=DISABLED)

#*************************checkbutton drinks and entry made on leftframe---------------------------------

cc=Checkbutton(leftbottom,text='COFFEE 10x ',font=('bold',18),bg='white',relief=SUNKEN,borderwidth=5,variable=v5,onvalue=1,offvalue=0,command=chkcoffee)
cc.grid(row=0,column=1,sticky=W)

ct=Checkbutton(leftbottom,text='TEA 10x',font=('bold',18),bg='white',relief=SUNKEN,borderwidth=5,variable=v6,onvalue=1,offvalue=0,command=chktea)
ct.grid(row=1,column=1,sticky=W)

cm=Checkbutton(leftbottom,text='MOJITO 50x',font=('bold',18),bg='white',relief=SUNKEN,borderwidth=5,variable=v7,onvalue=1,offvalue=0,command=chkmojito)
cm.grid(row=2,column=1,sticky=W)

csh=Checkbutton(leftbottom,text='SHAKE 50x',font=('bold',18),bg='white',relief=SUNKEN,borderwidth=5,variable=v8,onvalue=1,offvalue=0,command=chkshake)
csh.grid(row=3,column=1,sticky=W)


e5=Entry(leftbottom,borderwidth=10,bg='white')
e5.grid(row=0,column=2)
e5.insert(0,0)
e5.config(state=DISABLED)

e6=Entry(leftbottom,borderwidth=10,bg='white')
e6.grid(row=1,column=2)
e6.insert(0,0)
e6.config(state=DISABLED)

e7=Entry(leftbottom,borderwidth=10,bg='white')
e7.grid(row=2,column=2)
e7.insert(0,0)
e7.config(state=DISABLED)

e8=Entry(leftbottom,borderwidth=10,bg='white')
e8.grid(row=3,column=2)
e8.insert(0,0)
e8.config(state=DISABLED)




#**********************CONSTRUNCTION OF RIGHT FRAME

rightframe=Frame(screen,relief=SUNKEN)
# rightframe.pack(side=RIGHT)
rightframe.place(x=720,y=120)

righttop=Frame(rightframe,relief=SUNKEN,padx=10,pady=10)
righttop.pack(side=LEFT)

rightbuttom=Frame(rightframe,relief=SUNKEN,padx=10,pady=10)
rightbuttom.pack(side=RIGHT)




#***************************cost table, label and entry ON RIGHT FRAME-------------------------

#---food,bevrages,gst charge,total

lf=Label(righttop,text=' COST OF FOOD',font=('bold',18),borderwidth=5,bg='white',relief=SUNKEN)
lf.grid(row=0,column=0,sticky=W)

lb=Label(righttop,text=' COST OF DRINKS',font=('bold',18),borderwidth=5,bg='white',relief=SUNKEN)
lb.grid(row=1,column=0,sticky=W)

lg=Label(righttop,text='GST (+18%)==',font=('bold',18),borderwidth=5,bg='white',relief=SUNKEN)
lg.grid(row=2,column=0,sticky=W)

lt=Label(righttop,text='NET TOTAL==',font=('bold',18),borderwidth=5,bg='white',relief=SUNKEN)
lt.grid(row=3,column=0,sticky=W)


e9=Entry(righttop,borderwidth=5,bg='white')
e9.grid(row=0,column=1)

e10=Entry(righttop,borderwidth=5,bg='white')
e10.grid(row=1,column=1)

e11=Entry(righttop,borderwidth=5,bg='white')
e11.grid(row=2,column=1)

e12=Entry(righttop,borderwidth=5,bg='white')
e12.grid(row=3,column=1)

#------------------------------receipt table

receipt=Text(rightbuttom,bg='white',height=17,width=27,borderwidth=5)
receipt.grid(row=0,column=1)

#------------------------Buttons on right frame

b1=Button(righttop,text='EXIT',font=('bold',18),borderwidth=5,bg='ORANGE',relief=SUNKEN,justify=LEFT,command=lambda :closewindow())
b1.grid(row=20,column=0,sticky=W)

bR=Button(righttop,text='RECEIPT',font=('bold',18),borderwidth=5,bg='ORANGE',relief=SUNKEN,command=lambda:rec1())
bR.grid(row=50,column=0,sticky=W)

bT=Button(righttop,text='TOTAL',font=('bold',18),borderwidth=5,bg='ORANGE',relief=SUNKEN,justify=RIGHT,command=lambda: cost())
bT.grid(row=20,column=1)

brs=Button(righttop,text='RESET',font=('bold',18),borderwidth=5,bg='ORANGE',relief=SUNKEN,justify=RIGHT,command=lambda:reset1())
brs.grid(row=50,column=1)

#----------------------------------cost of items
def cost():

    item1=e1.get()
    item2=e2.get()
    item3=e3.get()
    item4=e4.get()
    item5=e5.get()
    item6=e6.get()
    item7=e7.get()
    item8=e8.get()

    global item11

    item11=int(item1)
    item12=int(item2)
    item13=int(item3)
    item14=int(item4)
    item15=int(item5)
    item16=int(item6)
    item17=int(item7)
    item18=int(item8)

    cost1=(item11*100)+(item12*100)+(item13*50)+(item14*50)
    e9.insert(0,cost1)

    drink=(item15*10)+(item16*10)+(item17*50)+(item18*50)
    e10.insert(0,drink)

    a1=e9.get()
    a11=int(a1)

    a2=e10.get()
    a12=int(a2)
    global add1

    add1=a11+a12

    gst=add1*.18
    e11.insert(0,gst)

    add2=(add1+gst)
    e12.insert(0,add2)





#------------------------------receipt disclosure--

def rec1():

    receipt.delete('1.0',END)
    date=datetime.datetime.now()
    date1=str(date)

    receipt.insert(END,'\n')
    receipt.insert(END,date1+'\n')
    receipt.insert(END,'\n')
    if v1.get()==1:
        receipt.insert(END,'BURGER  '+e1.get()+'\n')

    if v2.get()==1:
        receipt.insert(END,'PIZZA  '+e2.get()+'\n')

    if v3.get()==1:
        receipt.insert(END,'BURGER  '+e3.get()+'\n')

    if v4.get()==1:
        receipt.insert(END,'SANDWICH  '+e4.get()+'\n')

    if v5.get()==1:
        receipt.insert(END,'COFFEE  '+e5.get()+'\n')

    if v6.get()==1:
        receipt.insert(END,'TEA  '+e6.get()+'\n')

    if v7.get()==1:
        receipt.insert(END,'MOJITO  '+e7.get()+'\n')

    if v8.get()==1:
        receipt.insert(END,'SHAKE  '+e8.get()+'\n')

    receipt.insert(END,'\n')
    receipt.insert(END,'FOOD COST'+'\t'+ e9.get()+'\n')
    receipt.insert(END,'BEVRAGES COST'+'\t'+ e10.get()+'\n')
    receipt.insert(END,'\n')
    receipt.insert(END,'GST 18% '+e11.get()+'\n')
    receipt.insert(END,'\n')
    receipt.insert(END,'NET AMOUNT '+e12.get()+'\n')

#---------------------------------reset-----------

def reset1():



    v1.set(0)
    v2.set(0)
    v3.set(0)
    v4.set(0)
    v5.set(0)
    v6.set(0)
    v7.set(0)
    v8.set(0)

    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)
    e7.delete(0,END)
    e8.delete(0,END)

    e9.delete(0,END)
    e10.delete(0,END)
    e11.delete(0,END)
    e12.delete(0,END)

    e1.insert(0,'0')
    e2.insert(0,'0')
    e3.insert(0,'0')
    e4.insert(0,'0')
    e5.insert(0,'0')
    e6.insert(0,'0')
    e7.insert(0,'0')
    e8.insert(0,'0')

    e1.config(state=DISABLED)
    e2.config(state=DISABLED)
    e3.config(state=DISABLED)
    e4.config(state=DISABLED)
    e5.config(state=DISABLED)
    e6.config(state=DISABLED)
    e7.config(state=DISABLED)
    e8.config(state=DISABLED)

    receipt.delete('1.0',END)


#----------------------------EXIT


def closewindow():
    response=tk.messagebox.askokcancel("EXIT WINDOW","Do You Want to EXIT")
    if response==1:
        screen.quit()
        return










screen.mainloop()
