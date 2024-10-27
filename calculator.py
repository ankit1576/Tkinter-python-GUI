from tkinter import *
from PIL import ImageTk,Image
import math


fno=sno=op=None

def get_digit(digit):
    current=result_label['text']
    new=current+str(digit)
    result_label.config(text=new)

def clear():
    result_label.config(text='')

def get_op(opr):
    global fno,op
    fno=float(result_label['text'])
    op=opr
    result_label.config(text='')


def get_result():
    global fno, sno, op
    try:
        sno = float(result_label['text'])

        # Perform the operation
        if op == '+':
            result = fno + sno
        elif op == '-':
            result = fno - sno
        elif op == '*':
            result = fno * sno
        elif op == '/':
            result = fno / sno if sno != 0 else 'Error'
        elif op == '%':
            result = fno % sno
        elif op == '**':
            result = fno ** sno

        # Check if the result is an integer, format it accordingly
        if isinstance(result, float) and result.is_integer():
            result = int(result)  # Convert to integer if there's no decimal part
        elif isinstance(result, float):
            result = round(result, 2)  # Round to 2 decimal places

        result_label.config(text=str(result))

    except Exception as e:
        result_label.config(text='Error')


def sqrt():
    try:
        num = float(result_label['text'])
        result_label.config(text=str(math.sqrt(num)))
    except:
        result_label.config(text='Error')

def cbrt():
    try:
        num = float(result_label['text'])
        result_label.config(text=str(math.pow(num, 1/3)))
    except:
        result_label.config(text='Error')

def log():
    try:
        num = float(result_label['text'])
        result_label.config(text=str(math.log10(num)))
    except:
        result_label.config(text='Error')

def sin():
    try:
        num = math.radians(float(result_label['text']))
        result_label.config(text=str(math.sin(num)))
    except:
        result_label.config(text='Error')

def cos():
    try:
        num = math.radians(float(result_label['text']))
        result_label.config(text=str(math.cos(num)))
    except:
        result_label.config(text='Error')

def tan():
    try:
        num = math.radians(float(result_label['text']))
        result_label.config(text=str(math.tan(num)))
    except:
        result_label.config(text='Error')

def factorial():
    try:
        num = int(result_label['text'])
        result_label.config(text=str(math.factorial(num)))
    except:
        result_label.config(text='Error')

def abs_val():
    try:
        num = float(result_label['text'])
        result_label.config(text=str(abs(num)))
    except:
        result_label.config(text='Error')

def dot():
    current = result_label['text']
    if '.' not in current:
        result_label.config(text=current + '.')


root=Tk()
root.title('Scientific Calculator')
root.geometry('280x443')
root.resizable(0,0)
root.configure(background='black')

result_label=Label(root,text='',bg='black',fg='white')
result_label = Label(root, text='', bg='black', fg='white', anchor='e')#align right
result_label.grid(row=0, column=0, pady=(50, 25), columnspan=10, sticky='we')
result_label.config(font=('verdana',15,'bold'))

#_______________________________________________

btn7=Button(root,text='7',bg='#00a65a',fg='white',width=5,height=1,command=lambda :get_digit(7))
btn7.grid(row=1,column=0)
btn7.config(font=('verdana',14))

btn8=Button(root,text='8',bg='#00a65a',fg='white',width=5,height=1,command=lambda :get_digit(8))
btn8.grid(row=1,column=1)
btn8.config(font=('verdana',14))

btn9=Button(root,text='9',bg='#00a65a',fg='white',width=5,height=1,command=lambda :get_digit(9))
btn9.grid(row=1,column=2)
btn9.config(font=('verdana',14))

btn_add=Button(root,text='+',bg='#00a65a',fg='white',width=5,height=1,command=lambda :get_op('+'))
btn_add.grid(row=1,column=3)
btn_add.config(font=('verdana',14))
#________________________________________________

#_______________________________________________

btn4=Button(root,text='4',bg='#00a65a',fg='white',width=5,height=1,command=lambda :get_digit(4))
btn4.grid(row=2,column=0)
btn4.config(font=('verdana',14))

btn5=Button(root,text='5',bg='#00a65a',fg='white',width=5,height=1,command=lambda :get_digit(5))
btn5.grid(row=2,column=1)
btn5.config(font=('verdana',14))

btn6=Button(root,text='6',bg='#00a65a',fg='white',width=5,height=1,command=lambda :get_digit(6))
btn6.grid(row=2,column=2)
btn6.config(font=('verdana',14))

btn_sub=Button(root,text='-',bg='#00a65a',fg='white',width=5,height=1,command=lambda :get_op('-'))
btn_sub.grid(row=2,column=3)
btn_sub.config(font=('verdana',14))
#________________________________________________

#_______________________________________________

btn1=Button(root,text='1',bg='#00a65a',fg='white',width=5,height=1,command=lambda :get_digit(1))
btn1.grid(row=3,column=0)
btn1.config(font=('verdana',14))

btn2=Button(root,text='2',bg='#00a65a',fg='white',width=5,height=1,command=lambda :get_digit(2))
btn2.grid(row=3,column=1)
btn2.config(font=('verdana',14))

btn3=Button(root,text='3',bg='#00a65a',fg='white',width=5,height=1,command=lambda :get_digit(3))
btn3.grid(row=3,column=2)
btn3.config(font=('verdana',14))

btn_mul=Button(root,text='x',bg='#00a65a',fg='white',width=5,height=1,command=lambda :get_op('*'))
btn_mul.grid(row=3,column=3)
btn_mul.config(font=('verdana',14))
#________________________________________________

#_______________________________________________

btnc=Button(root,text='clear',bg='#00a65a',fg='black',width=5,height=1,command=lambda :clear())
btnc.grid(row=4,column=0)
btnc.config(font=('verdana',14))

btn0=Button(root,text='0',bg='#00a65a',fg='white',width=5,height=1,command=lambda :get_digit(0))
btn0.grid(row=4,column=1)
btn0.config(font=('verdana',14))

btn_equal=Button(root,text='=',bg='#00a65a',fg='black',width=5,height=1,command=get_result)
btn_equal.grid(row=4,column=2)
btn_equal.config(font=('verdana',14))

btn_div=Button(root,text='/',bg='#00a65a',fg='white',width=5,height=1,command=lambda :get_op('/'))
btn_div.grid(row=4,column=3)
btn_div.config(font=('verdana',14))
#________________________________________________

#_______________________________________________

btn_sqrt=Button(root,text='sqrt',bg='#00a65a',fg='white',width=5,height=1,command=sqrt)
btn_sqrt.grid(row=5,column=0)
btn_sqrt.config(font=('verdana',14))

btn_cbrt=Button(root,text='cbrt',bg='#00a65a',fg='white',width=5,height=1,command=cbrt)
btn_cbrt.grid(row=5,column=1)
btn_cbrt.config(font=('verdana',14))

btn_log=Button(root,text='log',bg='#00a65a',fg='white',width=5,height=1,command=log)
btn_log.grid(row=5,column=2)
btn_log.config(font=('verdana',14))

btn_pow=Button(root,text='^',bg='#00a65a',fg='white',width=5,height=1,command=lambda :get_op('**'))
btn_pow.grid(row=5,column=3)
btn_pow.config(font=('verdana',14))
#________________________________________________

#_______________________________________________

btn_sin=Button(root,text='sin',bg='#00a65a',fg='white',width=5,height=1,command=sin)
btn_sin.grid(row=6,column=0)
btn_sin.config(font=('verdana',14))

btn_cos=Button(root,text='cos',bg='#00a65a',fg='white',width=5,height=1,command=cos)
btn_cos.grid(row=6,column=1)
btn_cos.config(font=('verdana',14))

btn_tan=Button(root,text='tan',bg='#00a65a',fg='white',width=5,height=1,command=tan)
btn_tan.grid(row=6,column=2)
btn_tan.config(font=('verdana',14))

btn_mod=Button(root,text='%',bg='#00a65a',fg='white',width=5,height=1,command=lambda :get_op('%'))
btn_mod.grid(row=6,column=3)
btn_mod.config(font=('verdana',14))
#________________________________________________

#_______________________________________________

btn_asin=Button(root,text='asin',bg='#00a65a',fg='white',width=5,height=1)
btn_asin.grid(row=7,column=0)
btn_asin.config(font=('verdana',14))

btn_acos=Button(root,text='acos',bg='#00a65a',fg='white',width=5,height=1)
btn_acos.grid(row=7,column=1)
btn_acos.config(font=('verdana',14))

btn_atan=Button(root,text='atan',bg='#00a65a',fg='white',width=5,height=1)
btn_atan.grid(row=7,column=2)
btn_atan.config(font=('verdana',14))

btn_fab=Button(root,text='|x|',bg='#00a65a',fg='white',width=5,height=1)
btn_fab.grid(row=7,column=3)
btn_fab.config(font=('verdana',14))
#________________________________________________

#_______________________________________________

btn_open=Button(root,text='(',bg='#00a65a',fg='white',width=5,height=1)
btn_open.grid(row=8,column=0)
btn_open.config(font=('verdana',14))

btn_close=Button(root,text=')',bg='#00a65a',fg='white',width=5,height=1)
btn_close.grid(row=8,column=1)
btn_close.config(font=('verdana',14))

btn_exc=Button(root,text='!',bg='#00a65a',fg='white',width=5,height=1,command=factorial)
btn_exc.grid(row=8,column=2)
btn_exc.config(font=('verdana',14))

btn_dot=Button(root,text='.',bg='#00a65a',fg='white',width=5,height=1,command=dot)
btn_dot.grid(row=8,column=3)
btn_dot.config(font=('verdana',14))
#________________________________________________

root.mainloop()