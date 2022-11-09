class Nolasa:
  with open("txt/admin.txt") as datne:
    dati=datne.readline()
    sarakstaDati=dati.split(" ")
    vards=sarakstaDati[0]
    print("sarakstaDati=",sarakstaDati)
    print("vards=",vards)
    for vards in sarakstaDati:
      print(vards)