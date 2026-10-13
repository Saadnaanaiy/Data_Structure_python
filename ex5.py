

poids = int(input("entrer votre poids en (Kg) :"))

taille = int(input("entrer votre taille en (cm) :"))

imc = poids / ((taille / 100)) ** 2

interpretation = ""

if(imc >= 40) :
  interpretation = "Obésité morbide ou massive"
elif(imc >= 35 and imc < 40):
  interpretation = "Obésité severe"
elif(imc >= 30 and imc < 35):
  interpretation = "Obésité moderee"
elif(imc >= 25 and imc < 30):
  interpretation = "surpoids"
elif(imc >= 18.5 and imc < 25):
  interpretation = "Corpulence normale"
elif(imc >= 16.5 and imc < 18.5):
  interpretation = "Maigreur"
else :
  interpretation = "Famine"


print("Votre Poids en Kg : ", poids)
print()
print("Votre Taille en cm : ", poids)
print()
print("imc : ", imc)
print()
print("interpretation : ", interpretation)
