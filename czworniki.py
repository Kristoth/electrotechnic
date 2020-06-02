# -*- coding: utf-8 -*-
# coding: utf-8
import math
import sys

if len(sys.argv)<2:
   pres=int(input("Ilosc miejsc po przecinku: "))
else:
   pres=int(sys.argv[1])
print("Dokladnosc: "+str(pres)+" miejsc po przecinku")


def modul(a):
   return round(math.sqrt(a.real*a.real+a.imag*a.imag),pres)


def coro(z):
   global pres
   return complex(round(z.real,pres+5),round(z.imag,pres+5))
def cort(z):
   global pres
   if z.real<0:
      return complex(0,round(math.sqrt(z.imag),pres+5)+round(math.sqrt(-1*z.real),pres+5))   
   else:
      return complex(round(math.sqrt(z.real),pres+5),round(math.sqrt(z.imag),pres+5))


type=None
if len(sys.argv)<3:
   ask=int(input("'T'[0] czy 'TT'[1] ? "))
else:
   ask=sys.argv[2]


if ask ==0:
   type="T"
elif ask ==1:
   type="TT"
else:
   print("Nie rozpoznano typu,\nSprobuj ponownie")
   exit()

if type=="T":
   print("    ┏━━━━━━━━━┓    ")
   print("I11 ┃ Z1   Z2 ┃ I21")
   print("─>──╂─▭──┬─▭──╂─<──")
   print("^   ┃    │    ┃  ^  ")
   print("│U1 ┃    ▯Z3  ┃  │U2")
   print("│   ┃    │    ┃  │   ")
   print("─<──╂────┴────╂─>──")
   print(" I12┗━━━━━━━━━┛ I22 ")
else:
   print("    ┏━━━━━━━━━━━┓    ")
   print("I11 ┃     Z3    ┃ I21")
   print("─>──╂──┬──▭──┬──╂─<──")
   print("^   ┃  │     │  ┃  ^  ")
   print("│U1 ┃  ▯Z1   ▯Z2┃  │U2")
   print("│   ┃  │     │  ┃  │   ")
   print("─<──╂──┴─────┴──╂─>──")
   print(" I12┗━━━━━━━━━━━┛ I22 ")

#ask=raw_input("Podaj symbole Danych (po średnikach) ")
ask="z1;z2;z3"
ask=ask.lower()
dat=ask.split(";")
if "z1" in dat:
  z1=complex(input("Podaj Z1: "))
  z1=coro(z1)
  y1=coro(1/z1)

if "z2" in dat:
  z2=complex(input("Podaj Z2: "))
  z2=coro(z2)
  y2=coro(1/z2)
if "z3" in dat:
  z3=complex(input("Podaj Z3: "))
  z3=coro(z3)
  y3=coro(1/z3)

ask=int(input("Rowania lancuchowe? [1/0]"))
if ask == 1:
   rowlan=True
else:
   rowlan=False
ask=int(input("Przekladnia itp? [1/0]"))
if ask ==1:
   przek=True
else:
  przek=False

#ask=raw_input("Podaj Szukane (po średnikach) ")
ask="a;b;c;d"
ask=ask.lower()
lok=ask.split(";")
if "a" in lok and type=="T":
  a=1+coro(z1/z3)
  print("A=1+ Z1 / Z3 = 1 +"+str(z1)+" / "+str(z3)+" = "+str(a))
if "b" in lok and type=="T":
  b=coro(z1+z2+z1*z2/z3)
  print("B=Z1 + Z2 + Z1 * Z2 / Z3 = "+str(z1)+" + "+str(z2)+" + "+str(z1)+" * "+str(z2)+" / "+str(z3)+" = "+str(b)) 
if "c" in lok and type=="T":
  c=coro(1/z3)
  print("C=1/ Z3 = 1/ "+str(z3)+"= "+str(c)+" S")
if "d" in lok and type=="T":
  d=coro(1+z2/z3)
  print("D=1+ Z2 / Z3= 1+ "+str(z2)+" / "+str(z3)+" = "+str(d))

if "a" in lok and type=="TT":
  a=1+coro(1/z2*z3)
  print("A=1+ Y3*Z2  = 1 +1 /"+str(z2)+" / "+str(z3)+" = "+str(a))
if "b" in lok and type=="TT":
  b=z3
  print("B=Z3 = "+str(z3)) 
if "c" in lok and type=="TT":
  c=coro(y1+y2+y1*y2*z3)
  print("C=Y1 + Y2 + Y1 * Y2 * Z3 = "+str(y1)+" + "+str(y2)+" + "+str(y1)+" * "+str(y2)+" / "+str(z3)+" = "+str(c)) 
if "d" in lok and type=="TT":
  d=coro(1+z3/z1)
  print("D=1+ Z3 / Z1= 1+ "+str(z3)+" / "+str(z1)+" = "+str(d))
if przek==True:
   zc=cort(b/c)
   print("Impedancja falowa: Zc= (B/C)^1/2= "+str(zc))
   k=a+cort(b*c)
   km=modul(k)
   fi=math.atan(k.imag/k.real)/math.pi*180
   print("Przekładnia: K= A+ √(B*C)= "+str(k)+" modul: "+str(km))
   print("Kat: "+str(round(fi,pres)))
   print("Wspolczynik przenoszenia (a): "+str(1-km))
   print("Wspolczynik fazowy (b): "+str(round(fi,pres))+" stopni")
   print("Wspolczynik przenoszenia (g): "+str(round(fi,pres))+"j stopni")

if rowlan==True:
   print("Rownania lancuchowe: ")
   print("U1 = "+str(a)+"* U2 + "+str(b)+"* I2")
   print("I1 = "+str(c)+"* U2 + "+str(d)+"* I2")
#made by Krzysztof Budzisz
