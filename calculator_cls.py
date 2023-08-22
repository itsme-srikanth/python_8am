#tkinter
from tkinter import Tk ,Frame,Button,Label,StringVar
screen_val = Tk()
screen_val.title("calculator")
#screen_val.geometry('450*450+500+150')
#screen_val.resizable(0,0)
#screen_val.mainloop()
val = ''
data = StringVar()

def btn1_isclicked():
    global val
    val= val+'1'
    data.set(val)

def btn2_isclicked():
    global val
    val= val+'2'
    data.set(val)

def btn3_isclicked():
    global val
    val= val+'3'
    data.set(val)



def btn4_isclicked():
    global val
    val= val+'4'
    data.set(val)


def btn5_isclicked():
    global val
    val= val+'5'
    data.set(val)

def btn6_isclicked():
    global val
    val= val+'6'
    data.set(val)

def btn7_isclicked():
    global val
    val= val+'7'
    data.set(val)

def btn8_isclicked():
    global val
    val= val+'8'
    data.set(val)

def btn9_isclicked():
    global val
    val= val+'9'
    data.set(val)


def btn0_isclicked():
    global val
    val= val+'0'
    data.set(val)


def btnmult_isclicked():
    global val
    val= val+'mult'
    data.set(val)

def btnplus_isclicked():
    global val
    val= val+'+'
    data.set(val)

def btnsub_isclicked():
    global val
    val= val+'-'
    data.set(val)


def btndivid_isclicked():
    global val
    val= val+'/'
    data.set(val)


def btnc_isclicked():
    global val
    val= val+'clear'
    data.set(val)

def btnequal_isclicked():
    global val
    val= eval(val)
    val= str(val)
    data.set(val)



lbl_data = Label(screen_val,text='This is label',anchor='se',font=('verdana',20),textvariable=data)
lbl_data.pack(expand=True,fill='both')

frame1 = Frame(screen_val,bg='red')
frame1.pack(expand=True,fill='both')
frame2 = Frame(screen_val,bg='blue')
frame2.pack(expand=True,fill='both')
frame3 = Frame(screen_val,bg= 'green')
frame3.pack(expand=True,fill='both')
frame4 = Frame(screen_val,bg='white')
frame4.pack(expand=True,fill= 'both')
#screen_val.mainloop()

btn1 = Button(frame1,text='1',font=('verdana',20),border=0,command=btn1_isclicked)
btn1.pack(expand=True,fill='both',side='left')



btn2 = Button(frame1,text='2',font=('verdana',20),border=0,command=btn2_isclicked)
btn2.pack(expand=True,fill='both',side='left')


btn3 = Button(frame1,text='3',font=('verdana',20),border=0,command=btn3_isclicked)
btn3.pack(expand=True,fill='both',side='left')


btn4 = Button(frame2,text='4',font=('verdana',20),border=0,command=btn4_isclicked)
btn4.pack(expand=True,fill='both',side='left')


btn5 = Button(frame2,text='5',font=('verdana',20),border=0,command=btn5_isclicked)
btn5.pack(expand=True,fill='both',side='left')

btn6 = Button(frame2,text='6',font=('verdana',20),border=0,command=btn6_isclicked)
btn6.pack(expand=True,fill='both',side='left')

btn7 = Button(frame3,text='7',font=('verdana',20),border=0,command=btn7_isclicked)
btn7.pack(expand=True,fill='both',side='left')

btn8 = Button(frame3,text='8',font=('verdana',20),border=0,command=btn8_isclicked)
btn8.pack(expand=True,fill='both',side='left')


btn9 = Button(frame3,text='9',font=('verdana',20),border=0,command=btn9_isclicked)
btn9.pack(expand=True,fill='both',side='left')

btnsub = Button(frame2,text='sub',font=('verdana',20),border=0,command=btnsub_isclicked)
btnsub.pack(expand=True,fill='both',side='left')

btnplus = Button(frame1,text='plus',font=('verdana',20),border=0,command=btnplus_isclicked)
btnplus.pack(expand=True,fill='both',side='left')

btn0 = Button(frame3,text='0',font=('verdana',20),border=0,command=btn0_isclicked)
btn0.pack(expand=True,fill='both',side='left')


btnmult = Button(frame4,text='*',font=('verdana',20),border=0,command=btnmult_isclicked)
btnmult.pack(expand=True,fill='both',side='left')

btnequal = Button(frame4,text='=',font=('verdana',20),border=0,command=btnequal_isclicked)
btnequal.pack(expand=True,fill='both',side='left')

btnc = Button(frame4,text='clear',font=('verdana',20),border=0,command=btnc_isclicked)
btnc.pack(expand=True,fill='both',side='left')

btndivid = Button(frame4,text='/',font=('verdana',20),border=0,command=btndivid_isclicked)
btndivid.pack(expand=True,fill='both',side='left')


screen_val.mainloop()