# -*- coding: utf-8 -*-
# coding: utf-8
import math
import sys

if len(sys.argv)<2:
   pres=input("Ilosc miejsc po przecinku: ")
else:
   pres=int(sys.argv[1])
print("Dokladnosc: "+str(pres)+" miejsc po przecinku")


def modul(a):
   if sys.argv[0] == "czworniki.py":
      zero=0
   else:
      print("Skrypt By Krzysztof Budzisz")
   return round(math.sqrt(a.real*a.real+a.imag*a.imag),pres)


def coro(z):
   global pres
   return complex(round(z.real,pres+5),round(z.imag,pres+5))

type=None
if len(sys.argv)<3:
   ask=raw_input("'T'-(0) czy 'TT'-(1) ? ")
else:
   ask=sys.argv[2]


if ask in ["0","T","t","te"]:
   type="T"
elif ask in ["1","TT","tt","pi","Pi"]:
   type="TT"
else:
   print("Nie rozpoznano typu,\nSprobuj ponownie")
   exit()

if type=="t":
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
  z1=input("Podaj Z1: ")
  z1=coro(z1)
  y1=coro(1/z1)

if "z2" in dat:
  z2=input("Podaj Z2: ")
  z2=coro(z2)
  y2=coro(1/z2)
if "z3" in dat:
  z3=input("Podaj Z3: ")
  z3=coro(z3)
  y3=coro(1/z3)

ask=raw_input("Rowania lancuchowe? ")
ask=ask.lower()
if ask in ["tak","true","yes","1"]:
   rowlan=True
else:
   rowlan=False


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
e=coro(1/z1+z3)
print("\n\nE=1/ Z1 + Z3= 1/ "+str(z1)+" + "+str(z3)+" = "+str(e))



if rowlan==True:
   print("Rownania lancuchowe: ")
   print("U1 = "+str(a)+"* U2 + "+str(b)+"* I2")
   print("I1 = "+str(c)+"* U2 + "+str(d)+"* I2")



