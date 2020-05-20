from time import sleep
import sys
import math
import os
clear=lambda:os.system('clear')
version=0.9
print("Wersja skryptu: "+str(version))
if len(sys.argv)<2:
   pres=input("Ilosc miejsc po przecinku: ")
else:
   pres=int(sys.argv[1])
print("Dokladnosc: "+str(pres)+" miejsc po przecinku")
#Zdefiniowanie modulu liczby zespolonej

def modul(a):
   return round(math.sqrt(a.real*a.real+a.imag*a.imag),pres)

#zdefiniowanie zasad dla trojkata
def trojkat():
   print("Czyli trojkat")
#pobranie zmiennych
   U1=input("Napiecie miedzyfazowe:")
   U2=complex(round(U1*math.cos(-2.09),pres),round(U1*math.sin(-2.09),pres))
   U3=complex(round(U1*math.cos(2.09),pres),round(U1*math.sin(2.09),pres))
   R1=input("Opor 1.")
   R2=input("Opor 2.")
   R3=input("Opor 3.")
#oblicznie pradow
   I1=complex(round((U1/R1).real,pres),round((U1/R1).imag,pres))
   I2=complex(round((U2/R2).real,pres),round((U2/R2).imag,pres))
   I3=complex(round((U3/R3).real,pres),round((U3/R3).imag,pres))
   Ia=I1-I3
   Ib=I2-I1
   Ic=I3-I2
   deg1=math.atan(Ia.real*math.sqrt(3)/Ia.imag*math.sqrt(3))
   deg2=0-deg1

#obliczenie mocy
   S1=complex(round((U1*U1/R1).real,pres),round((U1*U1/R1).imag,pres))
   S2=complex(round((U1*U1/R2).real,pres),round((U1*U1/R2).imag,pres))
   S3=complex(round((U1*U1/R3).real,pres),round((U1*U1/R3).imag,pres))

   
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
   form=raw_input("Napiecie fazowe(0) czy miedzyfazowe?(1)")
   if form in ["0","f","F"]:
      U1=input("Napiecie Fazowe:")
   else:
      U1=round(input("Napiecie Miedzyfazowe:")/math.sqrt(3),pres)
   U2=complex(round(U1*math.cos(-2.09),pres),round(U1*math.sin(-2.09),pres))
   U3=complex(round(U1*math.cos(2.09),pres),round(U1*math.sin(2.09),pres))
   R1=input("Opor 1.")
   R2=input("Opor 2.")
   R3=input("Opor 3.")
   R4=input("Opor na przewodzie neutralym: ")
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
   clear()
   print("Napiecie nierownosci: "+str(complex(round(Un.real,pres),round(Un.imag,pres)))+" V, modul: "+str(modul(Un)))
   I1=complex(round((U1/R1).real,pres),round((U1/R1).imag,pres))
   I2=complex(round((U2/R2).real,pres),round((U2/R2).imag,pres))
   I3=complex(round((U3/R3).real,pres),round((U3/R3).imag,pres))
   #deg1=math.atan(I1.real*math.sqrt(3)/I1.imag*math.sqrt(3))
   #deg2=0-deg1
#obliczenie mocy
   S1=complex(round((U1*U1/R1).real,pres),round((U1*U1/R1).imag,pres))
   S2=complex(round((U1*U1/R2).real,pres),round((U1*U1/R2).imag,pres))
   S3=complex(round((U1*U1/R3).real,pres),round((U1*U1/R3).imag,pres))
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
   form=raw_input("Trojkat(0), gwiazda(1) czy moc(2)- zd9.28 ? ")
else:
   form=str(sys.argv[2])

if form in ["trojkat","Trojkat","0","t","T"]:
   trojkat()
elif form in ["2","moc","m","w","p"]:
   moc()
else:
  gwiazda()



# Skrypt by Krzysztof Budzisz 20.05.2020
