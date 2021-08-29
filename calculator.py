from tkinter import *
import math

root = Tk()
root.geometry("540x600+0+0")
root.title("Calculator")

in_put=StringVar()
oc=""

def onclick(n):
    global oc
    oc=oc+str(n)
    in_put.set(oc)

def sini():
    global oc
    oc=math.sin(int(oc))
    in_put.set(oc)
    

def cosi():
    global oc
    oc=math.cos(int(oc))
    in_put.set(oc)
    

def tani():
    global oc
    oc=math.tan(int(oc))
    in_put.set(oc)
    

def square():
    global oc
    oc=math.sqrt(int(oc))
    in_put.set(oc)  

def exponent():
    global oc
    oc=math.exp(int(oc))
    in_put.set(oc)
    

def floori():
    global oc
    oc=math.floor(int(oc))
    in_put.set(oc)
    

def absolute():
    global oc
    oc=math.fabs(int(oc))
    in_put.set(oc)


def arcsin():
    global oc
    oc=math.asin(int(oc))
    in_put.set(oc)


def arccos():
    global oc
    oc=math.acos(int(oc))
    in_put.set(oc)
    

def arctan():
    global oc
    oc=math.atan(int(oc))
    in_put.set(oc)
    

def fact():
    global oc
    oc=math.factorial(int(oc))
    in_put.set(oc)
    

def ceilf():
    global oc
    oc=math.ceil(int(oc))
    in_put.set(oc)
    
def degree():
    global oc
    oc=math.degrees(int(oc))
    in_put.set(oc)
    
    
def radian():
    global oc
    oc=math.radian(int(oc))
    in_put.set(oc)
    
    
def logritham():
    global oc
    oc=math.log10(int(oc))
    in_put.set(oc)
    

def cube():
    global oc
    oc=math.pow((int(oc),3))
    in_put.set(oc)
    


def inverse():
    global oc
    oc=(1/(int(oc)))
    in_put.set(oc)
    

def pie():
    in_put.set(3.14159265358)
    
    
def clearfn():
    global oc
    oc=""
    in_put.set(oc)

def evalution():
    global oc
    solve=str(eval(oc))
    in_put.set(solve)
    oc=""


f1=Frame(root,bg="cyan",height=10,width=540)
f1.pack(side=TOP)

lab=Label(f1,text="☺☺☺",font=("arial",25),bg="cyan",width=8,height=2)
lab.pack(side=LEFT)

#lab=Label(f1,text="Kumar",font=("arial",15),bg="steel cyan",width=8)
#lab.pack(side=LEFT)

lab1=Label(f1,text="≡  Scientific Calculator",font=("arial",15),bg="cyan",width=20,height=2)
lab1.pack(side=LEFT)

#lab2=Label(f1,text="Singh",font=("arial",15),bg="steel cyan",width=8)
#lab2.pack(side=LEFT)

lab21=Label(f1,text="☺☺☺",font=("arial",25),bg="cyan",width=8,height=2)
lab21.pack(side=LEFT)

f2=Frame(root,bg="cyan",width=540,height=10)
f2.pack(side=TOP)

lab23=Label(f2,text="»»»",font=("arial",15),bg="cyan",width=8,height=5)
lab23.pack(side=LEFT)

e1=Entry(f2,textvariable=in_put,width=56,bd=10,justify="right",relief="flat")
e1.pack(side=LEFT)

lab24=Label(f2,text="«««",font=("arial",15),bg="cyan",width=8,height=5)
lab24.pack(side=LEFT)


#f
f3=Frame(root,bg="black",width=540)
f3.pack(side=TOP)

fx=Frame(f3,bg="black",height=50,width=100)
fx.pack(side=LEFT)

lax=Label(fx,text="♫♫♫",font=("arial",15),bg="cyan",wraplength=10,width=8,height=8)
lax.pack()

frama=Frame(f3,bg="black",width=540)
frama.pack(side=LEFT)

#0

frame = Frame(frama, bg="black" ,cursor="arrow") 
frame.pack(side=BOTTOM,padx=5)

deci=Button(frame,width=5, height=2,bg="dark gray",relief=FLAT, text="1/x", command=inverse)
deci.pack(side=LEFT,padx=2, pady=2)

cube=Button(frame,width=5,height=2,bg="dark gray",relief=FLAT,text="x³", command=cube)
cube.pack(side=LEFT,padx=2, pady=2)

l_parenthesis=Button(frame,width=5,height=2,bg="dark gray",relief=FLAT,text="(" , command=lambda:onclick("("))
l_parenthesis.pack(side=LEFT,padx=2, pady=2)

r_parenthesis=Button(frame,width=5,height=2,bg="dark gray",relief=FLAT,text=")", command=lambda:onclick(")"))
r_parenthesis.pack(side=LEFT,padx=2, pady=2)

zero=Button(frame,width=5,height=2,bg="gray",relief=FLAT,text="0", command=lambda:onclick(0))
zero.pack(side=LEFT,padx=2, pady=2)

dot=Button(frame,width=5,height=2,bg="dark gray",relief=FLAT,text=".", command=lambda:onclick("."))
dot.pack(side=LEFT,padx=2, pady=2)

equal=Button(frame,width=5,height=2,bg="dark gray",relief=FLAT,text="=", command=evalution)
equal.pack(side=LEFT,padx=2, pady=2)

#1

frame1=Frame(frama,bg="black" ,cursor="arrow")
frame1.pack(side=BOTTOM, padx=5)

valofunderoot=Button(frame1,width=5, height=2,bg="dark gray",relief=FLAT,text="ⁿ√x", command=lambda:onclick("ⁿ√x"))
valofunderoot.pack(side=LEFT,padx=2, pady=2)

eklo=Button(frame1,width=5, height=2,bg="dark gray",relief=FLAT,text="eⁿ", command=exponent)
eklo.pack(side=LEFT,padx=2, pady=2)

mod=Button(frame1,width=5, height=2,bg="dark gray",relief=FLAT,text="±", command=lambda:onclick("±"))
mod.pack(side=LEFT,padx=2, pady=2)

one=Button(frame1,width=5, height=2,bg="gray",relief=FLAT,text="1", command=lambda:onclick(1))
one.pack(side=LEFT,padx=2, pady=2)

two=Button(frame1,width=5, height=2,bg="gray",relief=FLAT,text="2", command=lambda:onclick(2))
two.pack(side=LEFT,padx=2, pady=2)

three=Button(frame1,width=5, height=2,bg="gray",relief=FLAT,text="3", command=lambda:onclick(3))
three.pack(side=LEFT,padx=2, pady=2)

plus=Button(frame1,width=5, height=2,bg="dark gray",relief=FLAT,text="+", command=lambda:onclick("+"))
plus.pack(side=LEFT,padx=2, pady=2)

#2

frame2=Frame(frama,bg="black" ,cursor="arrow")
frame2.pack(side=BOTTOM, padx=5)

sininverse=Button(frame2,width=5, height=2,bg="dark gray",relief=FLAT,text="asin", command=arcsin)
sininverse.pack(side=LEFT,padx=2, pady=2)

cosinverse=Button(frame2,width=5, height=2,bg="dark gray",relief=FLAT,text="acos", command=arccos)
cosinverse.pack(side=LEFT,padx=2, pady=2)

fact=Button(frame2,width=5, height=2,bg="dark gray",relief=FLAT,text="n!", command=fact)
fact.pack(side=LEFT, padx=2, pady=2)

four=Button(frame2,width=5, height=2,bg="gray",relief=FLAT,text="4", command=lambda:onclick(4))
four.pack(side=LEFT, padx=2, pady=2)

five=Button(frame2,bg="gray",relief=FLAT,text="5",width=5, height=2,command=lambda:onclick(5))
five.pack(side=LEFT, padx=2, pady=2)

six=Button(frame2,width=5, height=2,bg="gray",relief=FLAT,text="6", command=lambda:onclick(6))
six.pack(side=LEFT, padx=2, pady=2)

minus=Button(frame2,width=5, height=2,bg="dark gray",relief=FLAT,text="-", command=lambda:onclick("-"))
minus.pack(side=LEFT, padx=2, pady=2)

#3

frame3=Frame(frama ,bg="black" ,cursor="arrow")
frame3.pack(side=BOTTOM, padx=5)

taninverse=Button(frame3,width=5, height=2,bg="dark gray",relief=FLAT,text="atan", command=arctan)
taninverse.pack(side=LEFT,padx=2, pady=2)

ln=Button(frame3,width=5, height=2,bg="dark gray",relief=FLAT,text="ln", command=lambda:onclick("ln"))
ln.pack(side=LEFT,padx=2, pady=2)

pi=Button(frame3,width=5, height=2,bg="dark gray",relief=FLAT,text="π", command=pie)
pi.pack(side=LEFT,padx=2, pady=2)

seven=Button(frame3,width=5, height=2,bg="gray",relief=FLAT,text="7", command=lambda:onclick(7))
seven.pack(side=LEFT,padx=2, pady=2)

eight=Button(frame3,width=5, height=2,bg="gray",relief=FLAT,text="8", command=lambda:onclick(8))
eight.pack(side=LEFT,padx=2, pady=2)

nine=Button(frame3,width=5, height=2,bg="gray",relief=FLAT,text="9", command=lambda:onclick(9))
nine.pack(side=LEFT,padx=2, pady=2)

multiply=Button(frame3,width=5, height=2,bg="dark gray",relief=FLAT,text="*", command=lambda:onclick("*"))
multiply.pack(side=LEFT,padx=2, pady=2)

#4
frame4=Frame(frama ,bg="black" ,cursor="arrow")
frame4.pack(side=BOTTOM, padx=5)

doni=Button(frame4,width=5, height=2,bg="dark gray",relief=FLAT,text="don", command=lambda:onclick("deg"))
doni.pack(side=LEFT,padx=2, pady=2)

dmsval=Button(frame4,width=5, height=2,bg="dark gray",relief=FLAT,text="dms", command=lambda:onclick("dms"))
dmsval.pack(side=LEFT,padx=2, pady=2)

floora=Button(frame4,width=5, height=2,bg="dark gray",relief=FLAT,text="//", command=floori)
floora.pack(side=LEFT,padx=2, pady=2)

clear=Button(frame4,width=5, height=2,bg="dark gray",relief=FLAT,text="CE", command=lambda:onclick("CE"))
clear.pack(side=LEFT,padx=2, pady=2)

allclear=Button(frame4,width=5, height=2,bg="dark gray",relief=FLAT,text="C", command=clearfn)
allclear.pack(side=LEFT,padx=2, pady=2)

cancel=Button(frame4,width=5, height=2,bg="dark gray",relief=FLAT,text="x", command=lambda:onclick("x"))
cancel.pack(side=LEFT,padx=2, pady=2)

division=Button(frame4,width=5, height=2,bg="dark gray",relief=FLAT,text="/", command=lambda:onclick("/"))
division.pack(side=LEFT,padx=2, pady=2)

#5
frame5=Frame(frama ,bg="black" ,cursor="arrow")
frame5.pack(side=BOTTOM, padx=5)

ciel=Button(frame5,width=5, height=2,bg="dark gray",relief=FLAT,text="ceil", command=ceilf)
ciel.pack(side=LEFT,padx=2, pady=2)

dot=Button(frame5,width=5, height=2,bg="dark gray",relief=FLAT,text=".", command=lambda:onclick("."))
dot.pack(side=LEFT,padx=2, pady=2)

unroot=Button(frame5,width=5, height=2,bg="dark gray",relief=FLAT,text="√", command=square)
unroot.pack(side=LEFT,padx=2, pady=2)

tenrtn=Button(frame5,width=5, height=2,bg="dark gray",relief=FLAT,text="10ⁿ", command=lambda:onclick("10ⁿ"))
tenrtn.pack(side=LEFT,padx=2, pady=2)

logrith=Button(frame5,width=5, height=2,bg="dark gray",relief=FLAT,text="log", command=logritham)
logrith.pack(side=LEFT,padx=2, pady=2)

exponent=Button(frame5,width=5, height=2,bg="dark gray",relief=FLAT,text="Exp", command=lambda:onclick("exp"))
exponent.pack(side=LEFT,padx=2, pady=2)

modulus=Button(frame5,width=5, height=2,bg="dark gray",relief=FLAT,text="Mod", command=absolute)
modulus.pack(side=LEFT,padx=2, pady=2)

#6

frame6=Frame(frama ,bg="black" ,cursor="arrow")
frame6.pack(side=BOTTOM, padx=5)

reddy=Button(frame6,width=5, height=2,bg="dark gray",relief=FLAT,text="rad", command=radian)
reddy.pack(side=LEFT,padx=2, pady=2)

dego=Button(frame6,width=5, height=2,bg="dark gray",relief=FLAT,text="deg", command=degree)
dego.pack(side=LEFT,padx=2, pady=2)

squree=Button(frame6,width=5, height=2,bg="dark gray",relief=FLAT,text="x²", command=lambda:onclick("x²"))
squree.pack(side=LEFT,padx=2, pady=2)

powofst=Button(frame6,width=5, height=2,bg="dark gray",relief=FLAT,text="xⁿ", command=lambda:onclick("xⁿ"))
powofst.pack(side=LEFT,padx=2, pady=2)

sino=Button(frame6,width=5, height=2,bg="dark gray",relief=FLAT,text="sin", command=sini)
sino.pack(side=LEFT,padx=2, pady=2)

cosi=Button(frame6,width=5, height=2,bg="dark gray",relief=FLAT,text="cos", command=cosi)
cosi.pack(side=LEFT,padx=2, pady=2)

tani=Button(frame6,width=5, height=2,bg="dark gray",relief=FLAT,text="tan", command=tani)
tani.pack(side=LEFT,padx=2, pady=2)

fx1=Frame(f3,bg="black",height=50,width=100)
fx1.pack(side=LEFT)

lax=Label(fx1,text="♫♫♫",font=("arial",15),bg="cyan",wraplength=10,width=8,height=8)
lax.pack()

f12=Frame(root,bg="cyan",height=10,width=540)
f12.pack(side=TOP)

lab=Label(f12,text="☻☻☻",font=("arial",25),bg="cyan",width=8,height=2)
lab.pack(side=LEFT)

#lab=Label(f1,text="Kumar",font=("arial",15),bg="steel cyan",width=8)
#lab.pack(side=LEFT)

lab12=Label(f12,text="≡  Kr-Gulson Kumar",font=("arial",15),bg="cyan",width=20,height=2)
lab12.pack(side=LEFT)

#lab2=Label(f1,text="Singh",font=("arial",15),bg="steel cyan",width=8)
#lab2.pack(side=LEFT)

lab20=Label(f12,text="☻☻☻",font=("arial",25),bg="cyan",width=8,height=2)
lab20.pack(side=LEFT)

'''w=Canvas(root,cursor="heart" ,highlightcolor="-+dth=40 ,height=60 ,bd=10 ,bg="brown")
w.pack(side=BOTTOM)
'''
