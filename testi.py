#---NOLASIT VISUS DATUS NO SAVAS DATNES

datne = open("txt/admin.txt") #noklusesanas metode 'r'
print(datne.read()) #nolasa visu datni
#------------------------------------------
#---NOLASIT 2X 5 SIMBOLUS
print(datne.read(5))
print(datne.read(5))
#------------------------------------------
#---NOLASIT 2X 5 SIMBOLUS ; ATRAST NULLTO SIMBOLU UN NOLASIT VELREIZ 5 SIM

print(datne.read(5))
datne.seek(0) #seek(offset[,from_what])
print(datne.read(5))
#------------------------------------------
#---IZDRUKAT KURSORA ATRASANAS VIETU
print(datne.read(5))
datne.seek(0) #seek(offset[,from_what])
print(datne.read(5))
pos=datne.tell()
print("Kursors atrodas uz",pos,"simbola")
datne.seek(0)
print("Kursors atrodas uz",datne.tell(),"simbola")
#------------------------------------------
#---IELASIT UN IZDRUKAT VISU DATNI, SALIDZINAT ABAS RINADS
viss=datne.readlines()
print("viss=",viss)
#---NOLASI UN IZDRUKA ABAS RINDAS
print(datne.readline())
print(datne.readline())
#------------------------------------------
#---NONEMT ENTER ZIMI IELASITAS RINDAS BEIGAS
print(datne.readline(),end="")
print(datne.readline(),end="")
#------------------------------------------
#--NOLASIT VISU DATNI CIKLA UN AIZVERT DATNI
for rinda in datne:
  print(rinda,end="")
#------------------------------------------
#---IZDRUKAT KATRU IEVADITO RINDINU UN UZVARDU TAJA
sum=0
for rinda in datne:
  print("rinda=",rinda)
  sarakstaDati=rinda.split(" ")
  vards=sarakstaDati[0]
  print("vards=",vards)

#--IZREKINAT ADMIN KOPIGO VECUMU
sum=0
for rinda in datne:
  dati=rinda.split(" ")
  sum += int(dati[3])
print("sum=",sum)
datne.close()
#------------------------------------------
