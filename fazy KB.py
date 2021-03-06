import sys
import math
version=0.9
print("Wersja skryptu: "+str(version))
if len(sys.argv)<2:
   pres=int(input("Ilosc miejsc po przecinku: "))
else:
   pres=int(sys.argv[1])
print("Dokladnosc: "+str(pres)+" miejsc po przecinku")
#Zdefiniowanie modulu liczby zespolonej

def modul(a):
   return round(math.sqrt(a.real*a.real+a.imag*a.imag),pres)
def coro(z):
   global pres
   return complex(round(z.real,pres+5),round(z.imag,pres+5))
#zdefiniowanie zasad dla trojkata
def trojkat():
   print("Czyli trojkat")
#pobranie zmiennych
   U1=complex(input("Napiecie miedzyfazowe:"))
   U2=coro(U1*math.cos(-2.09))+coro(U1*math.sin(-2.09))
   U3=coro(U1*math.cos(2.09))+coro(U1*math.sin(2.09))
   R1=complex(input("Opor 1."))
   R2=complex(input("Opor 2."))
   R3=complex(input("Opor 3."))
#oblicznie pradow
   I1=coro(U1/R1)
   I2=coro(U2/R2)
   I3=coro(U3/R3)
   Ia=I1-I3
   Ib=I2-I1
   Ic=I3-I2
   deg1=math.atan(Ia.real*math.sqrt(3)/Ia.imag*math.sqrt(3))
   deg2=0-deg1

#obliczenie mocy
   S1=coro(U1*U1/R1)
   S2=coro(U2*U2/R2)
   S3=coro(U3*U3/R3)


   
  #wydrukowanie wynikow
   if R1==R2==R3:
      print("Napiecie fazowe: "+str(U1)+" V")
      print("Prad fazowy: "+str(round(I1.real,pres))+" "+str(round(I1.imag,pres))+" j A, modul: "+str(modul(I1)))
      print("Prad przewodowy: "+str(round(Ia.real,pres))+" "+str(round(Ia.imag,pres))+"j A, modul: "+str(modul(Ia)))
      print("Moc pozorna : "+str(3*S1)+" AV, czynna: "+str((3*S1).real)+" W, bierna: "+str((3*S1).imag)+" var")

   else:
      print("Napiecie fazowe A: "+str(U1)+" V")
      print("Napiecie fazowe B: "+str(U2)+" V")
      print("Napiecie fazowe C: "+str(U3)+" V")
      print("Prad fazowy AB: "+str(round(I1.real,pres))+" "+str(round(I1.imag,pres))+" j A, modul: "+str(modul(I1)))
      print("Prad fazowy BC: "+str(round(I2.real,pres))+" "+str(round(I2.imag,pres))+" j A, modul: "+str(modul(I2)))
      print("Prad fazowy CA: "+str(round(I3.real,pres))+" "+str(round(I3.imag,pres))+" j A, modul: "+str(modul(I3)))
      print("Prad przewodowy A: "+str(round(Ia.real,pres))+" "+str(round(Ia.imag,pres))+"j A, modul: "+str(modul(Ia)))
      print("Prad przewodowy B: "+str(round(Ib.real,pres))+" "+str(round(Ib.imag,pres))+"j A, modul: "+str(modul(Ib)))
      print("Prad przewodowy C: "+str(round(Ic.real,pres))+" "+str(round(Ic.imag,pres))+"j A, modul: "+str(modul(Ic)))
      print("Moc pozorna a: "+str(S1)+" AV, czynna: "+str((S1).real)+" W, bierna: "+str((S1).imag)+" var")
      print("Moc pozorna b: "+str(S2)+" AV, czynna: "+str((S2).real)+" W, bierna: "+str((S2).imag)+" var")
      print("Moc pozorna c: "+str(S3)+" AV, czynna: "+str((S3).real)+" W, bierna: "+str((S3).imag)+" var")
      print("Suma mocy pozornych: "+str(S1+S2+S3)+" AV")
      print("Suma mocy czynnych: "+str((S1+S2+S3).real)+" W")
      print("Suma mocy biernych: "+str((S1+S2+S3).imag)+" var")


#zdefiniowanie zasad dla gwiazdy
def gwiazda():
   print("Czyli gwiazda")
#pobranie danych
   form=int(input("Napiecie fazowe(0) czy miedzyfazowe?(1)"))
   if form ==0:
      U1=int(input("Napiecie Fazowe:"))
   else:
      U1=round(int(input("Napiecie Miedzyfazowe:"))/math.sqrt(3),pres)
   U2=coro(U1*math.cos(-2.09))+coro(U1*math.sin(-2.09))
   U3=coro(U1*math.cos(2.09))+coro(U1*math.sin(2.09))
   R1=complex(input("Opor 1."))
   R2=complex(input("Opor 2."))
   R3=complex(input("Opor 3."))
   R4=complex(input("Opor na przewodzie neutralym: "))
   Y1=1/R1
   Y2=1/R2
   Y3=1/R3
#oblicznie napiecia nierownosci   
   if R4==0:
      Un=(Y1*U1+Y2*U2+Y3*U3)/(Y1+Y2+Y3)
   else:
      Y4=1/R4
      Un=(Y1*U1+Y2*U2+Y3*U3)/(Y1+Y2+Y3+Y4)
      U1=U1-Un
      U2=U2-Un
      U3=U3-Un 
   print("Napiecie nierownosci: "+str(complex(round(Un.real,pres),round(Un.imag,pres)))+" V, modul: "+str(modul(Un)))
   I1=coro(U1/R1)
   I2=coro(U2/R2)
   I3=coro(U3/R3)
   #deg1=math.atan(I1.real*math.sqrt(3)/I1.imag*math.sqrt(3))
   #deg2=0-deg1
#obliczenie mocy
   S1=coro(U1*U1/R1)
   S2=coro(U2*U2/R2)
   S3=coro(U3*U3/R3)
  #wydrukowanie wynikow
   if R1==R2==R3:
      if R4==0:
         print("Brak pradu w przewodzie neutralnym")
      else: 
         print("Prad w przewodzie neutralnym: "+str(I1+I2+I3)+" A, modul: "+str(modul(I1+I2+I3)))
      print("Napiecie fazowe: "+str(U1)+" V")
      print("Prad fazowy: "+str(round(I1.real,pres))+" "+str(round(I1.imag,pres))+" j A, modul: "+str(modul(I1)))
      print("Moc pozorna: "+str(S1)+" AV, czynna: "+str((S1).real)+" W, bierna: "+str((S1).imag)+" var")
   else:
      print("Napiecie fazowe A: "+str(U1)+" V")
      print("Napiecie fazowe B: "+str(U2)+" V")
      print("Napiecie fazowe C: "+str(U3)+" V")
      print("Prad fazowy A: "+str(round(I1.real,pres))+" "+str(round(I1.imag,pres))+" j A, modul: "+str(modul(I1)))
      print("Prad fazowy B: "+str(round(I2.real,pres))+" "+str(round(I2.imag,pres))+" j A, modul: "+str(modul(I2)))
      print("Prad fazowy C: "+str(round(I3.real,pres))+" "+str(round(I3.imag,pres))+" j A, modul: "+str(modul(I3)))
      print("Moc pozorna a: "+str(S1)+" AV, czynna: "+str((S1).real)+" W, bierna: "+str((S1).imag)+" var")
      print("Moc pozorna b: "+str(S2)+" AV, czynna: "+str((S2).real)+" W, bierna: "+str((S2).imag)+" var")
      print("Moc pozorna c: "+str(S3)+" AV, czynna: "+str((S3).real)+" W, bierna: "+str((S3).imag)+" var")
   print("Suma mocy pozornych: "+str(S1+S2+S3)+" AV, modul: "+str(modul(S1+S2+S3)))
   print("Suma mocy czynnych: "+str((S1+S2+S3).real)+" W")
   print("Suma mocy biernych: "+str((S1+S2+S3).imag)+" var")


#zdefiniowanie mocy

def moc():
   print("Liczenie mocy metoda dwoch watomierzy")
   P1=int(input("Podaj moc 1. "))
   P2=int(input("Podaj moc 2. "))
   P=P1+P2
   Q=round(math.sqrt(3)*(P1 - P2),pres)
   deg=round(math.atan(Q/P),pres)
   rat=round(math.cos(deg),pres)
   S=P/rat
   print("Moc czynna: "+str(P)+" W") 
   print("Moc bierna: "+str(Q)+" var")
   print("Moc pozorna: "+str(round(S,pres))+" VA")
   print("Wspolczynnik mocy: "+str(rat))
   print("Kat: "+str(round(deg/math.pi*180, pres))+ " stopni")


#spytanie o uklad
if len(sys.argv)<3:
   form=int(input("Trojkat(0), gwiazda(1) czy moc(2)- zd9.28 ? "))
else:
   form=str(sys.argv[2])

if form == 0:
   trojkat()
elif form == 2:
   moc()
else:
  gwiazda()


# Skrypt by Krzysztof Budzisz
