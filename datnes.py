class Datnes:
  def __init__(self,nosaukums):
    self.nosaukums= "txt/"+'admin.txt'
  
  def nolasaDatus(self,nosaukums):
    print("nosaukums=",self.nosaukums)
    with open(self.nosaukums,'r') as datne:
      dati=datne.readline()
      sarakstaDati=dati.split(" ")
      vards=sarakstaDati[0]
      print("sarakstaDati=",sarakstaDati)
      print("vards=",vards)
      for vards in sarakstaDati:
        print(vards)