#---------------------------------------
datne=open("txt/admin.txt")
sum=0
num=[]
#---------------------------------------
for rinda in datne:
  dati= rinda.split(" ")
  sum += int(dati[2]) #ADMIN SUMMA GADIEM
  vid = sum / 3 #ADMIN APREKINATS VIDEJAIS
  minv=min(dati[:3]) #1 ADMIN MIN GADI
  num.append(minv) #2 ADMIN MIN GADI
  maxv=max(dati[2]) #1 ADMIN MAX GADI
  num.append(maxv) #2 ADMIN MAX GADI
#---------------------------------------
print("sum=",sum)
print("vid=",vid)
print("Jaunakais=",min(num),end="") 
print("Vecakais=",max(num),end="")
#---------------------------------------
print()
print()
#---------------------------------------
from nolasa import *
Nolasa()
#---------------------------------------
#from datnes import *
#Datnes()
#Nestrada, rada TypeError:__init__ missing 1 required positional argument:'nosaukums'
#---------------------------------------
datne.close()
#---------------------------------------
