

pression = float(input("entrer la pression courant: "))
volume = float(input("entrer la volume courant: "))

pSeuil = 2.3
vSeuil = 7.41

if(pression > pSeuil and volume > vSeuil):
  print("arret immediat")
elif(pression > pSeuil) :
  volume = float(input("augmenter la volume : "))
elif(volume > vSeuil):
  volume = float(input("diminuer la volume : "))
else :
  print("tout va bien")
